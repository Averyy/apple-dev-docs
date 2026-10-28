---
url: "https://docs.swift.org/latest/documentation/swiftjavadocumentation/featuresjextract"
framework: "Swift-Org/SwiftJavaDocumentation"
---

# Features: jextract

**Framework**: Swift-Org/SwiftJavaDocumentation  
**Role**: Article

Detailed feature documentation for calling Swift from Java using jextract.

## Overview

The following sections describe each feature supported by jextract, with Swift definitions alongside the generated Java API for both JNI and FFM modes.

For guidance on choosing between JNI and FFM mode, see [Features Overview](./featuresoverview.md).

### Initializers

**Swift**:

```symlink
public init(x: Int64, y: Int64) {
  self.x = x
  self.y = y
}

public init() {
  self.x = 10
  self.y = 5
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    MySwiftClass c = MySwiftClass.init(20, 10, arena);
    assertEquals(30, c.sum());
}
```

**Java (FFM)**:

```java
try (var arena = AllocatingSwiftArena.ofConfined()) {
    MySwiftClass c = MySwiftClass.init(20, 10, arena);
    assertEquals(30, c.sum());
}
```

Classes and structs can both have initializers imported.

### Class members

Swift `class` methods and computed properties are imported as `static` methods on the generated Java wrapper type.

**Swift**:

```symlink
public class func classMethod(x: Int64) -> Int64 {
  x * 2
}

public class var classVariable: Int64 {
  42
}
```

**Java (JNI)**:

```java
assertEquals(24, MySwiftClass.classMethod(12));
assertEquals(42, MySwiftClass.getClassVariable());
```

**Java (FFM)**:

```java
assertEquals(24, MySwiftClass.classMethod(12));
assertEquals(42, MySwiftClass.getClassVariable());
```

### Optional initializers / Throwing initializers

Optional and throwing initializers are supported in JNI mode.

**Swift**:

```symlink
convenience public init(throwing: Bool) throws {
  if throwing {
    throw MySwiftError.swiftError
  } else {
    self.init()
  }
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    Exception exception = assertThrows(Exception.class, () -> MySwiftClass.init(true, arena));
    assertEquals("swiftError", exception.getMessage());

    MySwiftClass c = assertDoesNotThrow(() -> MySwiftClass.init(false, arena));
    assertNotNull(c);
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Deinitializers

Classes and structs are automatically cleaned up when the enclosing arena is closed (`SwiftArena` in JNI mode, `AllocatingSwiftArena` in FFM mode). No explicit deinitialization calls are needed on the Java side.

### Enums

Swift enums with associated values are extracted into a corresponding Java `class`. Each case becomes a static factory method, and associated values are accessed via `getAsX` methods that return `Optional` records.

**Swift**:

```symlink
public enum Vehicle {
  case bicycle
  case car(String, trailer: String?)
  case motorbike(String, horsePower: Int64, helmets: Int32?)
  indirect case transformer(front: Vehicle, back: Vehicle)
  case boat(passengers: Int32?, length: Int16?)

  public init?(name: String) {
    switch name {
    case "bicycle": self = .bicycle
    case "car": self = .car("Unknown", trailer: nil)
    case "motorbike": self = .motorbike("Unknown", horsePower: 0, helmets: nil)
    case "boat": self = .boat(passengers: nil, length: nil)
    default: return nil
    }
  }

  public var name: String {
    switch self {
    case .bicycle: "bicycle"
    case .car: "car"
    case .motorbike: "motorbike"
    case .transformer: "transformer"
    case .boat: "boat"
    }
  }

  public func isFasterThan(other: Vehicle) -> Bool {
    switch (self, other) {
    case (.bicycle, .bicycle), (.bicycle, .car), (.bicycle, .motorbike), (.bicycle, .transformer): false
    case (.car, .bicycle): true
    case (.car, .motorbike), (.car, .transformer), (.car, .car): false
    case (.motorbike, .bicycle), (.motorbike, .car): true
    case (.motorbike, .motorbike), (.motorbike, .transformer): false
    case (.transformer, .bicycle), (.transformer, .car), (.transformer, .motorbike): true
    case (.transformer, .transformer): false
    default: false
    }
  }

  public mutating func upgrade() {
    switch self {
    case .bicycle: self = .car("Unknown", trailer: nil)
    case .car: self = .motorbike("Unknown", horsePower: 0, helmets: nil)
    case .motorbike: self = .transformer(front: .car("BMW", trailer: nil), back: self)
    case .transformer, .boat: break
    }
  }
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    Vehicle vehicle = Vehicle.car("BMW", Optional.empty(), arena);
    Vehicle.Case.Car car = vehicle.getAsCar().orElseThrow();
    assertEquals("BMW", car.arg0());

    vehicle = Vehicle.car("BMW", Optional.of("Long trailer"), arena);
    car = vehicle.getAsCar().orElseThrow();
    assertEquals("Long trailer", car.trailer().orElseThrow());
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

#### Switching and pattern matching

Use `getDiscriminator()` for simple switching without accessing associated values:

```java
assertEquals(Vehicle.Discriminator.BICYCLE, Vehicle.bicycle(arena).getDiscriminator());
assertEquals(Vehicle.Discriminator.CAR, Vehicle.car("BMW", Optional.empty(), arena).getDiscriminator());
assertEquals(Vehicle.Discriminator.MOTORBIKE, Vehicle.motorbike("Yamaha", 750, OptionalInt.empty(), arena).getDiscriminator());
assertEquals(Vehicle.Discriminator.TRANSFORMER, Vehicle.transformer(Vehicle.bicycle(arena), Vehicle.bicycle(arena), arena).getDiscriminator());
```

For Java 21+, `getCase(arena)` returns a `Vehicle.Case` value that works with [pattern matching for switch](https://openjdk.org/jeps/441), which lets you bind the associated values of each case directly:

```java
try (var arena = SwiftArena.ofConfined()) {
    Vehicle vehicle = Vehicle.car("BMW", Optional.empty(), arena);
    switch (vehicle.getCase(arena)) {
        case Vehicle.Case.Bicycle b:
            fail("Was bicycle");
            break;
        case Vehicle.Case.Car car:
            assertEquals("BMW", car.arg0());
            break;
        case Vehicle.Case.Motorbike motorbike:
            fail("Was motorbike");
            break;
        case Vehicle.Case.Transformer transformer:
            fail("Was transformer");
            break;
        case Vehicle.Case.Boat b:
            fail("Was boat");
            break;
    }
}
```

Each nested `Vehicle.Case.*` type is a `record`, so on Java 21+ you can also destructure it positionally (`case Vehicle.Case.Car(var name, var trailer)`), and on Java 16+ reach the same values with [pattern matching for instanceof](https://openjdk.org/jeps/394).

### RawRepresentable enums

jextract supports extracting enums that conform to `RawRepresentable`, giving access to an optional initializer and the `rawValue` property.

**Swift**:

```symlink
public enum Alignment: String {
  case horizontal
  case vertical
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    Optional<Alignment> invalid = Alignment.init("invalid", arena);
    assertFalse(invalid.isPresent());

    Optional<Alignment> horizontal = Alignment.init("horizontal", arena);
    assertTrue(horizontal.isPresent());
    assertEquals("horizontal", horizontal.get().getRawValue());

    Optional<Alignment> vertical = Alignment.init("vertical", arena);
    assertTrue(vertical.isPresent());
    assertEquals("vertical", vertical.get().getRawValue());
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Global functions

Global Swift functions are imported as static methods on the generated library class.

### Member functions

Class and struct member functions are imported as instance methods on the generated Java wrapper type.

**Swift**:

```symlink
public func getCapacity() -> Int64 {
  self.cap
}

public mutating func increaseCap(by value: Int64) -> Int64 {
  precondition(value > 0)
  self.cap += value
  return self.cap
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    MySwiftStruct s = MySwiftStruct.init(1337, 42, arena);
    assertEquals(1337, s.getCapacity());

    long newCap = s.increaseCap(10);
    assertEquals(1347, newCap);
    assertEquals(1347, s.getCapacity());
}
```

**Java (FFM)**:

```java
try (var arena = AllocatingSwiftArena.ofConfined()) {
    MySwiftStruct s = MySwiftStruct.init(1337, 42, arena);
    assertEquals(1337, s.getCapacity());

    long newCap = s.increaseCap(10);
    assertEquals(1347, newCap);
    assertEquals(1347, s.getCapacity());
}
```

### Throwing functions

Throwing Swift functions are imported as Java methods that throw exceptions. In FFM mode the exception type is `SwiftJavaErrorException`. In JNI mode the thrown exception depends on the Swift error, as described below.

**Swift**:

```symlink
public func throwString(input: String) throws -> String {
  if input.isEmpty {
    throw MySwiftError.swiftError
  }
  return input
}
```

**Java (JNI)**:

```java
Exception exception = assertThrows(Exception.class, () -> {
    MySwiftLibrary.throwString("");
});
assertNotNull(exception.getMessage());
assertTrue(exception.getMessage().contains("swiftError"));
```

**Java (FFM)**:

```java
SwiftJavaErrorException exception = assertThrows(SwiftJavaErrorException.class, () -> {
    MySwiftLibrary.throwString("");
});
assertNotNull(exception.getMessage());
assertTrue(exception.getMessage().contains("swiftError"));
```

#### Errors in JNI mode

In JNI mode, extracted Swift types that conform to `Error` or `LocalizedError` are generated as Java classes extending `org.swift.swiftkit.core.SwiftError`, which is a `java.lang.Exception`. `getMessage()` returns the Swift `String(describing:)` of the error.

When a Swift function throws such an error, Java receives that exact class. Errors whose type was not extracted (for example a non-public error type) are thrown as `org.swift.swiftkit.core.SwiftErrorException`, which is also a `SwiftError`.

Swift typed throws (`throws(MyError)`) become a checked `throws MyError` in Java, while untyped `throws` stays `throws Exception`. Async throwing functions return a `CompletableFuture` that completes exceptionally with the same exception, available as the cause of the `ExecutionException` thrown by `get()`.

```java
try {
    MySwiftLibrary.throwTyped("");
} catch (MySwiftError e) {
    switch (e.getCase()) {
        case MySwiftError.Case.SwiftError _ -> System.out.println("swift error");
        case MySwiftError.Case.InvalidInput(var reason) -> System.out.println(reason);
    }
}
```

### Stored properties

Stored `var` and `let` properties are imported as getter/setter methods. Properties with `willSet` and `didSet` observers work transparently.

### private(set) properties

In JNI mode, properties declared `public private(set) var` are imported with only a getter on the Java side; the setter is omitted so the property’s write-access restriction is preserved across the language boundary. FFM mode does not yet apply this restriction.

**Swift**:

```symlink
public private(set) var privateSetCounter: Int64 = 7
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    MySwiftClass c = MySwiftClass.init(20, 10, arena);
    assertEquals(7, c.getPrivateSetCounter());
}

// The setter must not be exposed to Java for `public private(set) var`
Method getter = MySwiftClass.class.getMethod("getPrivateSetCounter");
assertNotNull(getter);
assertThrows(NoSuchMethodException.class, () -> MySwiftClass.class.getMethod("setPrivateSetCounter", long.class));
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Computed properties

Computed properties are imported the same way as stored properties: as getter (and optionally setter) methods. Throwing computed properties are supported in JNI mode but not yet in FFM mode.

**Swift**:

```symlink
public var product: Int64 {
  x * y
}
public var throwingVariable: Int64 {
  get throws {
    throw MySwiftClassError.swiftError
  }
}
public var mutableDividedByTwo: Int64 {
  get {
    mutable / 2
  }
  set {
    mutable = newValue * 2
  }
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    MySwiftClass c = MySwiftClass.init(20, 10, arena);
    assertEquals(0, c.getMutableDividedByTwo());
    c.setMutable(20);
    assertEquals(10, c.getMutableDividedByTwo());
    c.setMutableDividedByTwo(5);
    assertEquals(10, c.getMutable());
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Async functions

Asynchronous functions are imported as Future-type returning Java functions.

There are two modes of extracting them, configurable using the `asyncFuncMode` setting in `swift-java.config`, or using the equivalent `--async-func-mode` command line option:

- **`completableFuture` (default)**: `async` functions return `java.util.concurrent.CompletableFuture`
- **`legacyFuture`**: for platforms (e.g. Android 23 and below) where `CompletableFuture` is not available, `async` functions return `java.util.concurrent.Future`

**Swift**:

```symlink
public func asyncSum(i1: Int64, i2: Int64) async -> Int64 {
  i1 + i2
}

public func asyncSleep() async throws {
  try await Task.sleep(for: .milliseconds(500))
}
```

**Java (JNI)**:

```java
Future<Long> future = MySwiftLibrary.asyncSum(10, 12);

Long result = future.get();
assertEquals(22, result);
```

**Java (FFM): not supported**:

```java
// not supported yet
```

#### Asynchronous functions and Kotlin async/await

Because Kotlin offers extension `suspending fun` methods on Future types, it is possible to `.await()` on such Swift extracted `async` function in Kotlin, like so:

```kotlin
import com.example.swift.MySwiftLibrary
import kotlinx.coroutines.future.await

suspend fun useAsyncSum() {
  // MySwiftLibrary.asyncSum returns a java.util.concurrent.CompletableFuture<Long>
  val result: Long = MySwiftLibrary.asyncSum(10, 12).await()
  println("result = $result")
}
```

This relies on the Kotlin `kotlinx-coroutines-jdk8` library which adds the `await()` extension function on `java.util.concurrent.CompletableFuture`.

### Collections

Arrays are copied across the boundary. Dictionaries and sets are handed to Java as a wrapper over the live Swift value.

#### Arrays

Arrays of primitives (`[UInt8]`, `[Int32]`, `[Double]`, `[String]`) are supported in both JNI and FFM modes and map to the corresponding Java array types (`byte[]`, `int[]`, `double[]`, `String[]`).

**Swift**:

```symlink
public func byteArray(array: [UInt8]) -> [UInt8] {
  array
}

public func intArray(array: [Int32]) -> [Int32] {
  array
}

public func doubleArray(array: [Double]) -> [Double] {
  array
}

public func stringArray(array: [String]) -> [String] {
  array
}
```

**Java (JNI)**:

```java
byte[] input = new byte[] { 10, 20, 30, 40 };
assertArrayEquals(input, MySwiftLibrary.byteArray(input));
```

**Java (FFM)**:

```java
byte[] input = new byte[] { 10, 20, 30, 40 };
assertArrayEquals(input, MySwiftLibrary.byteArray(input));
```

Arrays of user-defined jextract-imported types (`[MySwiftClass]`) and nested arrays (`[[UInt8]]`, `[[String]]`) are supported in JNI mode.

**Swift**:

```symlink
public func objectArray(array: [MySwiftClass]) -> [MySwiftClass] {
  array
}

public func nestedByteArray(array: [[UInt8]]) -> [[UInt8]] {
  array
}

public func nestedStringArray(array: [[String]]) -> [[String]] {
  array
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    MySwiftClass[] input = new MySwiftClass[]{
        MySwiftClass.init(arena),
        MySwiftClass.init(arena),
        MySwiftClass.init(arena)
    };
    assertEquals(3, MySwiftLibrary.objectArray(input, arena).length);
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

#### InlineArray

Fixed-size inline arrays (Swift’s `InlineArray<N, T>`, sugar `[N of T]`) are recognized when parsing Swift sources, but are not yet extracted in either mode. Declarations using them are skipped.

#### Dictionaries

Swift dictionaries (`[Key: Value]`) are imported using the `SwiftDictionaryMap<Key, Value>` Java wrapper type. Creating the wrapper does not copy the dictionary; it implements `java.util.Map` by making a JNI downcall into the Swift value for each operation. Use `SwiftDictionaryMap::toJavaMap` to copy into a `java.util.Map` on the Java heap.

**Swift**:

```symlink
public func makeStringToLongDictionary() -> [String: Int64] {
  [
    "hello": 1,
    "world": 2,
  ]
}

public func stringToLongDictionary(dict: [String: Int64]) -> [String: Int64] {
  dict
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    SwiftDictionaryMap<String, Long> dict = MySwiftLibrary.makeStringToLongDictionary(arena);
    assertEquals(2, dict.size());
    assertEquals(1L, dict.get("hello"));
    assertEquals(2L, dict.get("world"));
    assertTrue(dict.containsKey("hello"));
    assertFalse(dict.containsKey("missing"));
    assertNull(dict.get("missing"));
    assertNull(dict.get(99999L), "Java's Map accepts keys of different types");
    assertFalse(dict.containsKey(99999L), "Java's Map accepts keys of different types");
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

#### Sets

Swift sets (`Set<Element>`) are imported using the `SwiftSet<Element>` Java wrapper. Like dictionaries, creating the wrapper does not copy, and each operation is a JNI downcall. Use `SwiftSet::toJavaSet` to copy into a `java.util.Set` on the Java heap.

**Swift**:

```symlink
public func makeStringSet() -> Set<String> {
  ["hello", "world"]
}

public func stringSet(set: Set<String>) -> Set<String> {
  set
}

public func insertIntoStringSet(set: Set<String>, element: String) -> Set<String> {
  var copy = set
  copy.insert(element)
  return copy
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    SwiftSet<String> set = MySwiftLibrary.makeStringSet(arena);
    assertEquals(2, set.size());
    assertTrue(set.contains("hello"));
    assertTrue(set.contains("world"));
    assertFalse(set.contains("missing"));
    assertFalse(set.contains(99999L), "Java's Set accepts keys of different types");
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Bytes and buffers

There are several ways to pass raw bytes, differing in whether the bytes are copied or viewed in place.

#### Byte arrays

`[UInt8]` maps to Java’s `byte[]` in both modes by copying.

Note that Java’s `byte` is signed, so a Swift `UInt8` of `200` reads as `-56` on the Java side; see [Primitive and unsigned types](./featuresjextract.md#Primitive-and-unsigned-types).

**Swift**:

```symlink
public func byteArray(array: [UInt8]) -> [UInt8] {
  array
}

public func intArray(array: [Int32]) -> [Int32] {
  array
}

public func doubleArray(array: [Double]) -> [Double] {
  array
}

public func stringArray(array: [String]) -> [String] {
  array
}
```

**Java (JNI)**:

```java
byte[] input = new byte[] { 10, 20, 30, 40 };
assertArrayEquals(input, MySwiftLibrary.byteArray(input));
```

**Java (FFM)**:

```java
byte[] input = new byte[] { 10, 20, 30, 40 };
assertArrayEquals(input, MySwiftLibrary.byteArray(input));
```

Nested byte arrays (`[[UInt8]]`) are also supported in JNI mode.

#### Raw byte buffers

A Swift function taking `UnsafeRawBufferPointer` is callable from both modes, with the buffer surfacing differently on the Java side.

In JNI mode it is a plain `byte[]`. jextract obtains the array’s elements for the duration of the call (via JNI’s `GetByteArrayElements`) and hands Swift a buffer over them; whether that memory is the array itself or a copy is up to the JVM.

In FFM mode it is a `MemorySegment`, which Swift reads in place without any copy. In both modes the buffer is only valid for the duration of the call, so the Swift side must not store it.

`UnsafeMutableRawBufferPointer` is supported the same way:

**Swift**:

```symlink
/// Sum all bytes in the buffer
public func sumOfBytes(data: UnsafeRawBufferPointer) -> Int64 {
  var sum: Int64 = 0
  for byte in data {
    sum += Int64(byte)
  }
  return sum
}

/// Return the count of bytes in the buffer
public func bufferCount(data: UnsafeRawBufferPointer) -> Int64 {
  Int64(data.count)
}
```

**Java (JNI)**:

```java
byte[] input = new byte[] { 1, 2, 3, 4, 5 };
assertEquals(15, MySwiftLibrary.sumOfBytes(input));
```

**Java (FFM)**:

```java
try (var arena = AllocatingSwiftArena.ofConfined()) {
    byte[] input = new byte[] { 1, 2, 3, 4, 5 };
    MemorySegment buffer = arena.allocateFrom(ValueLayout.JAVA_BYTE, input);

    assertEquals(15, MySwiftLibrary.sumOfBytes(buffer));
}
```

It is also possible to write closures which accept a buffer from the Swift side, like this:

**Swift**:

```symlink
public func withBuffer(body: (UnsafeRawBufferPointer) -> Void) {
  body(globalBuffer)
}
```

**Java (FFM)**:

```java
AtomicLong bufferSize = new AtomicLong();
MySwiftLibrary.withBuffer((buf) -> {
    CallTraces.trace("withBuffer{$0.byteSize()}=" + buf.byteSize());
    bufferSize.set(buf.byteSize());
});

assertEquals(124, bufferSize.get());
```

#### Java ByteBuffer

In FFM mode the generated `Data` wrapper converts to and from `java.nio.ByteBuffer`. Bringing bytes in:

```java
try (var arena = AllocatingSwiftArena.ofConfined()) {
    byte[] original = new byte[] { 1, 2, 3, 4, 5 };
    ByteBuffer buffer = ByteBuffer.wrap(original);
    var data = Data.fromByteBuffer(buffer, arena);
    assertEquals(5, data.getCount());
}
```

and getting them back out:

```java
try (var arena = AllocatingSwiftArena.ofConfined()) {
    byte[] original = new byte[] { 10, 20, 30, 40 };
    var data = Data.fromByteArray(original, arena);
    var buffer = data.toByteBuffer(arena);

    assertEquals(original.length, buffer.capacity());
    for (int i = 0; i < original.length; i++) {
        assertEquals(original[i], buffer.get(i));
    }
}
```

In JNI mode, `Data.toByteArray()` is the way to copy bytes out. For the `Data` type itself see [Data](./featuresjextract.md#Data).

#### Java MemorySegment (FFM only)

`Data.toMemorySegment(arena)` copies the bytes into memory allocated in the given arena and returns it as a `java.lang.foreign.MemorySegment`. This is one copy, and the JVM then reads that native memory without a second copy onto the Java heap. To read the bytes without copying at all, use `withUnsafeBytes` (see below).

> ❗ **Important**: `MemorySegment` is part of the Foreign Function & Memory API ([JEP 454](https://openjdk.org/jeps/454)), final since JDK 22. It is available in FFM mode only; there is no `MemorySegment` equivalent in JNI mode.

```java
try (var arena = AllocatingSwiftArena.ofConfined()) {
    byte[] original = new byte[] { 10, 20, 30, 40 };
    var data = Data.fromByteArray(original, arena);
    var segment = data.toMemorySegment(arena);

    assertEquals(original.length, segment.byteSize());
    for (int i = 0; i < original.length; i++) {
        assertEquals(original[i], segment.get(ValueLayout.JAVA_BYTE, i));
    }
}
```

### Generic types

Support for generic types is work-in-progress and limited. Members containing type parameters (such as `T`) are not exported.

**Swift**:

```symlink
public struct MyID<T: Hashable>: Hashable {
  public var rawValue: T
  public init(_ rawValue: T) {
    self.rawValue = rawValue
  }
  public var description: String {
    "\(rawValue)"
  }
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    MyID<String> stringId = MyIDs.makeStringID("Java", arena);
    assertEquals("Java", stringId.getDescription());
    assertEquals("Java", MyIDs.takeStringValue(stringId));

    MyID<Long> intId = MyIDs.makeIntID(42, arena);
    assertEquals("42", intId.getDescription());
    assertEquals(42, MyIDs.takeIntValue(intId));

    Tuple2<MyID<String>, MyID<Long>> ids = MyIDs.makeIDs("Java", 42, arena);
    assertEquals("Java", ids.$0.getDescription());
    assertEquals("42", ids.$1.getDescription());
    assertEquals("Java", MyIDs.takeValuesFromTuple(ids).$0);
    assertEquals(42, MyIDs.takeValuesFromTuple(ids).$1);

    Optional<MyID<Double>> doubleIdOptional = MyIDs.makeDoubleIDOptional(42.195, arena);
    assertTrue(doubleIdOptional.isPresent());
    assertEquals(42.195, MyIDs.takeDoubleValueOptional(doubleIdOptional).getAsDouble());
    assertEquals(42.195, MyIDs.takeDoubleValue(doubleIdOptional.get())); // ensure wrapped value is alive

    MyID<Optional<String>> optionalStringId = MyIDs.makeOptionalStringID(Optional.of("Java"), arena);
    assertEquals("Optional(\"Java\")", optionalStringId.getDescription());
    assertEquals("Java", MyIDs.takeOptionalStringValue(optionalStringId).get());
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Generic type specialization

Conditional/constrained extensions on types (e.g. `extension Box where Element == Fish`) cannot be safely exposed on the generic Java wrapper. Instead, jextract detects typealiases like `typealias FishBox = Box<Fish>` and performs *specialization* - exposing a dedicated `FishBox` Java class with all matching extensions applied.

**Swift**:

```symlink
public struct Box<Element>: Hashable {
  public var count: Int64

  public init(count: Int64) {
    self.count = count
  }

  public static func describeElement() -> String {
    String(describing: Element.self)
  }
}

public struct Fish: Hashable {
  public var name: String

  public init(name: String) {
    self.name = name
  }
}

extension Box where Element == Fish {
  public func describeFish() -> String {
    "A box of \(count) fish"
  }
}

public typealias FishBox = Box<Fish>
```

**Java (JNI)**:

```java
assertEquals("Fish", FishBox.describeElement());
```

**Java (FFM): not supported**:

```java
// not supported yet
```

`FishBox` carries the constrained extension’s `describeFish()` in addition to `Box`’s own members, and unlike the generic `Box` it has no Java type parameter.

#### Specializing via swift-java.config

The `typealias` above works when you control the Swift source being wrapped. If you don’t, for example you are running jextract against a dependency you can’t edit, the same specialization can be requested from `swift-java.config` using the `specialize` key, without touching the Swift source at all:

```json
{
  "specialize": {
    "FishBox": {
      "base": "Box",
      "typeArgs": {"Element": "Fish"}
    }
  }
}
```

This produces the same `FishBox` Java class, with the same constrained extension members applied, as the `typealias FishBox = Box<Fish>` approach. See [specialize](./swiftjavaconfigfile.md#specialize) for the full field reference.

### Tuples

Tuples are imported as `Tuple2`, `Tuple3`, etc. types with positional `$0`, `$1` accessors.

**Swift**:

```symlink
public func returnIntPair() -> (Int32, Int64) {
  (42, 43)
}

public func sumIntPair(pair: (Int32, Int64)) -> Int64 {
  Int64(pair.0) + pair.1
}
```

**Java (JNI)**:

```java
Tuple2<Integer, Long> result = MySwiftLibrary.returnIntPair();
assertEquals(42, result.$0);
assertEquals(43L, result.$1);
```

**Java (FFM)**:

```java
Tuple2<Integer, Long> result = MySwiftLibrary.returnIntPair();
assertEquals(42, result.$0);
assertEquals(43L, result.$1);
```

In JNI mode tuple elements may also be `String` or wrapper types, and labeled tuples get named accessors in addition to the positional ones. FFM mode currently supports tuples of primitive elements only.

**Swift**:

```symlink
public func returnPair() -> (Int64, String) {
  (42, "hello")
}

public func takePair(pair: (Int64, String)) -> String {
  "\(pair.0):\(pair.1)"
}

public func labeledTuple() -> (x: Int32, y: Int32) {
  (x: 10, y: 20)
}
```

**Java (JNI)**:

```java
Tuple2<Long, String> result = MySwiftLibrary.returnPair();
assertEquals(42L, result.$0);
assertEquals("hello", result.$1);
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Protocols

Swift `protocol` types are imported as Java `interface`s. Concrete types wrapping a Swift instance can be passed to protocol-typed parameters.

> **Note**: `any DataProtocol` is handled as `Foundation.Data` in FFM mode; see below.

**Swift**:

```symlink
public protocol ProtocolA {
  var constantA: Int64 { get }
  var mutable: Int64 { get set }

  func name() -> String
  func makeClass() -> MySwiftClass
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    JavaStorage storage = new JavaStorage(null);
    MySwiftLibrary.saveWithStorage(StorageItem.init(10, arena), storage);
    assertEquals(10, MySwiftLibrary.loadWithStorage(storage, arena).getValue());
    MySwiftLibrary.saveWithStorage(StorageItem.init(7, arena), storage);
    MySwiftLibrary.saveWithStorage(StorageItem.init(5, arena), storage);
    assertEquals(5, MySwiftLibrary.loadWithStorage(storage, arena).getValue());
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

Protocol parameters using `any`, `some`, or generics are all imported as Java generics:

**Swift**:

```symlink
public func takeProtocol(_ proto1: any ProtocolA, _ proto2: some ProtocolA) -> Int64 {
  proto1.constantA + proto2.constantA
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    ConcreteProtocolAB proto1 = ConcreteProtocolAB.init(10, 5, arena);
    ConcreteProtocolAB proto2 = ConcreteProtocolAB.init(20, 1, arena);
    assertEquals(30, MySwiftLibrary.takeProtocol(proto1, proto2));
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Existential and opaque parameters

In JNI mode, existential (`any SomeProtocol`, `any (A & B)`) and opaque (`some Builder`) parameters are all imported as Java generics with appropriate bounds. Not yet supported in FFM mode.

For example:

```swift
func f<S: A & B>(x: S, y: any C, z: some D)
```

becomes:

```java
<S extends A & B, T1 extends C, T2 extends D> void f(S x, T1 y, T2 z)
```

Only Swift-backed instances may be passed; this enables passing concrete jextract-generated types that conform to a given Swift protocol.

### Returning protocol types

Functions that return an existential (`any SomeProtocol`) or opaque (`some SomeProtocol`) value of a single protocol are supported. The returned value is wrapped in a generated *existential box*: a Java class named `<Protocol>Box` that implements the protocol’s Java `interface`. The box carries the concrete value together with its type metadata, and dispatches each protocol requirement through a dedicated native thunk that reconstructs the existential from that value.

**Swift**:

```symlink
public func makeEnglishGreeter(name: String) -> any Greeter {
  EnglishGreeter(name: name)
}

public func makeDanishGreeter(name: String) -> any Greeter {
  DanishGreeter(name: name)
}

public func makeOpaqueGreeter(name: String) -> some Greeter {
  EnglishGreeter(name: name)
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    Greeter greeter = MySwiftLibrary.makeEnglishGreeter("World", arena);
    assertEquals("Hello, World!", greeter.greeting());
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

Using the returned value works like using any other imported interface: its requirements are callable through the box, it can be passed back into functions that accept the protocol (including generic and opaque parameters), and refined protocols expose both their own and their inherited requirements.

> **Note**: Static requirements (`static func`, `init`) and returning a *composite* existential (`any (A & B)`) are not currently supported.

### Foundation types

A handful of Foundation value types are recognized by name and bridged to a matching Java representation, rather than being treated as opaque Swift values.

#### Data

Swift methods accepting or returning `Foundation.Data` are extracted using the Java `Data` wrapper type.

In **FFM mode**, the generated wrapper offers zero-copy access via `withUnsafeBytes`, as well as `toByteArray`, `toByteBuffer`, and `toMemorySegment(arena)` for copying to JVM-managed memory.

In **JNI mode**, use `Data.toByteArray()` to copy the underlying native data into a Java byte array. A true zero-copy `withUnsafeBytes` is not available in JNI mode.

**Swift**:

```symlink
public func echoData(_ data: Data) -> Data {
  data
}

public func makeData() -> Data {
  Data([0x01, 0x02, 0x03, 0x04])
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    byte[] bytes = new byte[] { 1, 2, 3, 4 };
    var data = Data.fromByteArray(bytes, arena);

    var echoed = MySwiftLibrary.echoData(data, arena);
    assertArrayEquals(bytes, echoed.toByteArray());
}
```

**Java (FFM)**:

```java
try (var arena = AllocatingSwiftArena.ofConfined()) {
    byte[] bytes = new byte[] { 1, 2, 3, 4 };
    var data = Data.fromByteArray(bytes, arena);

    var echoed = MySwiftLibrary.echoData(data, arena);
    assertArrayEquals(bytes, echoed.toByteArray());
}
```

In FFM mode the returned bytes can also be read without copying them into the JVM at all:

```java
try (var arena = AllocatingSwiftArena.ofConfined()) {
    byte[] bytes = new byte[] { 1, 2, 3, 4 };
    var data = Data.fromByteArray(bytes, arena);

    var echoed = MySwiftLibrary.echoData(data, arena);
    echoed.withUnsafeBytes((segment) -> {
        assertEquals(4, segment.byteSize());
        assertEquals(1, segment.get(ValueLayout.JAVA_BYTE, 0));
    });
}
```

#### Date

In JNI mode, `Foundation.Date` is imported as a generated `Date` wrapper class. It converts to and from `java.time.Instant` via `toInstant()` and `Date.fromInstant(instant, arena)`, and exposes `getTimeIntervalSince1970()`. Not yet supported in FFM mode.

**Swift**:

```symlink
public func compareDates(date1: Date, date2: Date) -> Bool {
  date1 == date2
}

public func dateFromSeconds(_ seconds: Double) -> Date {
  Date(timeIntervalSince1970: seconds)
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    var date = MySwiftLibrary.dateFromSeconds(1000.50, arena);
    assertEquals(1000.5, date.getTimeIntervalSince1970());

    var date2 = Date.init(1000.5, arena);
    assertTrue(MySwiftLibrary.compareDates(date, date2));

    var date3 = Date.init(1000.49, arena);
    assertFalse(MySwiftLibrary.compareDates(date, date3));
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

#### UUID

In JNI mode, `Foundation.UUID` maps directly to `java.util.UUID`, so UUIDs can be passed in either direction without a wrapper type. Not yet supported in FFM mode.

**Swift**:

```symlink
public func echoUUID(_ uuid: UUID) -> UUID {
  uuid
}

public func makeUUID() -> UUID {
  UUID()
}
```

**Java (JNI)**:

```java
var uuid = UUID.randomUUID();
assertEquals(uuid, MySwiftLibrary.echoUUID(uuid));
```

**Java (FFM): not supported**:

```java
// not supported yet
```

#### URL

Both `Foundation.URL` and `FoundationEssentials.URL` are recognized and imported. On the Java side they surface as a generated `URL` wrapper class backed by the Swift value, so URLs can flow across the boundary without manual string conversion. Because Swift’s `URL(string:)` is failable, constructing one from Java returns an `Optional<URL>`.

**Swift**:

```symlink
public func echoURL(_ url: URL) -> URL {
  url
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    var url = URL.init("http://example.com", arena);
    assertDoesNotThrow(() -> {
        var unwrapped = url.orElseThrow();
        assertEquals("http://example.com", unwrapped.getAbsoluteString());
    });
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Optional parameters and return types

Optional primitives use Java’s `OptionalLong`, `OptionalInt`, etc. Optional objects use `java.util.Optional<T>`. Optional parameters work in both modes:

**Swift**:

```symlink
public func optionalLongOrZero(input: Int64?) -> Int64 {
  input ?? 0
}
```

**Java (JNI)**:

```java
assertEquals(0, MySwiftLibrary.optionalLongOrZero(OptionalLong.empty()));
assertEquals(999, MySwiftLibrary.optionalLongOrZero(OptionalLong.of(999)));
```

**Java (FFM)**:

```java
assertEquals(0, MySwiftLibrary.optionalLongOrZero(OptionalLong.empty()));
assertEquals(999, MySwiftLibrary.optionalLongOrZero(OptionalLong.of(999)));
```

Optional *return* types are supported in JNI mode only:

**Swift**:

```symlink
public func optionalLong(input: Int64?) -> Int64? {
  input
}

public func optionalFloat(input: Float?) -> Float? {
  input
}

public func optionalDouble(input: Double?) -> Double? {
  input
}

public func optionalString(input: String?) -> String? {
  input
}

public func optionalClass(input: MySwiftClass?) -> MySwiftClass? {
  input
}

public func optionalDate(input: Date?) -> Date? {
  input
}

public func optionalData(input: Data?) -> Data? {
  input
}
```

**Java (JNI)**:

```java
assertEquals(OptionalLong.empty(), MySwiftLibrary.optionalLong(OptionalLong.empty()));
assertEquals(OptionalLong.of(999), MySwiftLibrary.optionalLong(OptionalLong.of(999)));
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Primitive and unsigned types

Java does not support unsigned numbers (other than the 16-bit wide `char`), so Swift’s unsigned integer types are mapped as their bit-width equivalents. This is potentially dangerous - for example `200` stored in a `UInt8` would be interpreted as a `byte` of value `-56` in Java.

| Swift type | Java type |
| --- | --- |
| `Int8` | `byte` |
| `UInt8` | `byte` (lossy) |
| `Int16` | `short` |
| `UInt16` | `char` |
| `Int32` | `int` |
| `UInt32` | `int` (lossy) |
| `Int64` | `long` |
| `UInt64` | `long` (lossy) |
| `Float` | `float` |
| `Double` | `double` |

#### The @Unsigned annotation

Because the Java type alone cannot express that a value was unsigned in Swift, jextract marks every such value with the `@Unsigned` annotation from `org.swift.swiftkit.core.annotations`. The annotation does not enforce anything at runtime; it records that a negative Java value should be read as a large positive one, and gives static analysis tools something to check against. It is retained at runtime, so it is also visible through reflection.

The annotation is placed on parameters directly, and on the method itself when it is the *return* type that is unsigned:

```swift
// Swift
public func takeUnsignedLong(arg: UInt64)
public func returnUnsignedLong() -> UInt64
public func unsignedLong(first: UInt64, second: UInt32) -> UInt32
```

generates:

```java
// Java (generated)
public static void takeUnsignedLong(@Unsigned long arg) { ... }

@Unsigned
public static long returnUnsignedLong() { ... }

@Unsigned
public static int unsignedLong(@Unsigned long first, @Unsigned int second) { ... }
```

Collections of unsigned elements are annotated as a whole, rather than per element:

```swift
// Swift
public func acceptArray(array: [UInt8])
public func returnArray() -> [UInt8]
```

```java
// Java (generated)
public static void acceptArray(@Unsigned byte[] array) { ... }

@Unsigned
public static byte[] returnArray() { ... }
```

The same applies to `Set` and `Dictionary`, where an unsigned key *or* value is enough for the annotation to appear, and it is applied recursively so that `[[UInt8]]` is annotated too.

> **Note**: `UInt16` is annotated as well, even though `char` is itself an unsigned 16-bit type and the conversion is lossless. The annotation records the Swift type faithfully in every case.

Swift’s word-sized `Int` and `UInt` are imported as `long`, which is wide enough for a 64-bit Swift `Int`. Where the Swift side may be 32-bit the generated Java range-checks arguments and return values, throwing `SwiftIntegerOverflowException` for values that would not fit.

### Strings

Strings are passed by copying data across the language boundary. A Swift `String` becomes a Java `String`, both as a parameter and as a return type, in both modes.

**Swift**:

```symlink
public func globalWriteString(string: String) -> Int64 {
  Int64(string.count)
}
```

**Java (JNI)**:

```java
var string = "Hello Swift!";
long reply = MySwiftLibrary.globalWriteString(string);

assertEquals(string.length(), reply);
```

**Java (FFM)**:

```java
var string = "Hello Swift!";
long reply = MySwiftLibrary.globalWriteString(string);

assertEquals(string.length(), reply);
```

### Subscripts

Swift subscripts are imported as `getSubscript`/`setSubscript` methods. Subscripts taking parameters keep them on the generated Java methods.

**Swift**:

```symlink
public subscript() -> Int64 {
  get { subscriptValue }
  set { subscriptValue = newValue }
}

public subscript(index: Int64) -> Int64 {
  get { subscriptArray[Int(index)] }
  set { subscriptArray[Int(index)] = newValue }
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    MySwiftStruct s = MySwiftStruct.init(1337, 42, arena);
    long currentValue = s.getSubscript(1);
    s.setSubscript(1, 66);
    assertEquals(20, currentValue);
    assertEquals(66, s.getSubscriptArrayValue(1));
}
```

**Java (FFM)**:

```java
try (var arena = AllocatingSwiftArena.ofConfined()) {
    MySwiftStruct s = MySwiftStruct.init(1337, 42, arena);
    long currentValue = s.getSubscript(1);
    s.setSubscript(1, 66);
    assertEquals(20, currentValue);
    assertEquals(66, s.getSubscriptArrayValue(1));
}
```

### Closures

Swift closure parameters become Java functional interfaces that can be implemented with a lambda expression.

#### Non-escaping closures

Non-escaping closures with `Void` return or primitive arguments/results are supported in both modes.

> **Note**: In FFM mode, closures that return a value (such as `() -> Bool`) work, but `Void`-returning upcalls are not yet implemented.

**Swift**:

```symlink
public func emptyClosure(closure: () -> Void) {
  closure()
}

public func closureWithInt(input: Int64, closure: (Int64) -> Int64) -> Int64 {
  closure(input)
}

public func globalCallMeBooleanSupplier(run: () -> Bool) -> Bool {
  run()
}

public func globalCallMeIntSupplier(run: () -> Int32) -> Int32 {
  run()
}

public func globalCallMeLongSupplier(run: () -> Int64) -> Int64 {
  run()
}

public func globalCallMeDoubleSupplier(run: () -> Double) -> Double {
  run()
}

public func globalCallMeIntConsumer(run: (Int32) -> Void) {
  run(1)
}

public func globalCallMeLongConsumer(run: (Int64) -> Void) {
  run(1)
}

public func globalCallMeDoubleConsumer(run: (Double) -> Void) {
  run(1.0)
}

public func globalCallMeIntPredicate(run: (Int32) -> Bool) -> Bool {
  run(1)
}

public func globalCallMeLongPredicate(run: (Int64) -> Bool) -> Bool {
  run(1)
}

public func globalCallMeDoublePredicate(run: (Double) -> Bool) -> Bool {
  run(1.0)
}

public func globalCallMeIntUnaryOperator(run: (Int32) -> Int32) -> Int32 {
  run(1)
}

public func globalCallMeLongUnaryOperator(run: (Int64) -> Int64) -> Int64 {
  run(1)
}

public func globalCallMeDoubleUnaryOperator(run: (Double) -> Double) -> Double {
  run(1.0)
}

public func globalCallMeIntBinaryOperator(run: (Int32, Int32) -> Int32) -> Int32 {
  run(1, 2)
}

public func globalCallMeLongBinaryOperator(run: (Int64, Int64) -> Int64) -> Int64 {
  run(1, 2)
}

public func globalCallMeDoubleBinaryOperator(run: (Double, Double) -> Double) -> Double {
  run(1.0, 2.0)
}

public func globalCallMeDoubleToIntFunction(run: (Double) -> Int32) -> Int32 {
  run(1.0)
}

public func globalCallMeLongToIntFunction(run: (Int64) -> Int32) -> Int32 {
  run(1)
}

public func globalCallMeDoubleToLongFunction(run: (Double) -> Int64) -> Int64 {
  run(1.0)
}

public func globalCallMeIntToLongFunction(run: (Int32) -> Int64) -> Int64 {
  run(1)
}

public func globalCallMeIntToDoubleFunction(run: (Int32) -> Double) -> Double {
  run(1)
}

public func globalCallMeLongToDoubleFunction(run: (Int64) -> Double) -> Double {
  run(1)
}

public func closureMultipleArguments(
  input1: Int64,
  input2: Int64,
  closure: (Int64, Int64) -> Int64
) -> Int64 {
  closure(input1, input2)
}
```

**Java (JNI)**:

```java
boolean result = MySwiftLibrary.globalCallMeBooleanSupplier(() -> true);
assertEquals(true, result);
```

**Java (FFM)**:

```java
boolean result = MySwiftLibrary.globalCallMeBooleanSupplier(() -> true);
assertEquals(true, result);
```

#### Escaping closures

`@escaping` closures with `Void` return or primitive arguments/results are supported. The closure is stored on the Swift side and can be triggered multiple times.

**Swift**:

```symlink
public class CallbackManager {
  private var callback: (() -> Void)?
  private var intCallback: ((Int64) -> Int64)?

  public init() {}

  public func setCallback(callback: @escaping () -> Void) {
    self.callback = callback
  }

  public func triggerCallback() {
    callback?()
  }

  public func clearCallback() {
    callback = nil
  }

  public func setIntCallback(callback: @escaping (Int64) -> Int64) {
    self.intCallback = callback
  }

  public func triggerIntCallback(value: Int64) -> Int64? {
    intCallback?(value)
  }
}
```

**Java (JNI)**:

```java
try (var arena = SwiftArena.ofConfined()) {
    CallbackManager manager = CallbackManager.init(arena);

    AtomicBoolean wasCalled = new AtomicBoolean(false);

    // Create an escaping closure (no try-with-resources needed - cleanup is automatic via Swift ARC)
    CallbackManager.setCallback.callback callback = () -> {
        wasCalled.set(true);
    };

    // Set the callback
    manager.setCallback(callback);

    // Trigger it
    manager.triggerCallback();
    assertTrue(wasCalled.get(), "Callback should have been called");

    // Trigger again to ensure it's still stored
    wasCalled.set(false);
    manager.triggerCallback();
    assertTrue(wasCalled.get(), "Callback should be called multiple times");

    // Clear the callback - this releases the closure on Swift side, triggering GlobalRef cleanup
    manager.clearCallback();
}
```

**Java (FFM): not supported**:

```java
// not supported yet
```

### Type extensions

Swift type extensions (e.g. `extension String { ... }`) are supported in both modes. Extended methods appear on the generated Java wrapper type.

### Nested types

Nested types (e.g. `struct Hello { struct World {} }`) are supported in JNI mode. Not yet supported in FFM mode.

### ARC and lifetime safety

Class instances are reference-counted using Swift’s Automatic Reference Counting (ARC). The Java arena (`SwiftArena` in JNI, `AllocatingSwiftArena` in FFM) manages lifetimes - when the arena is closed, all instances allocated within it are released.

### Sendable and thread safety

Swift types conforming to `Sendable` are surfaced on the Java side with the `@ThreadSafe` annotation on the generated wrapper class, communicating to Java callers that the wrapped Swift value is safe to share across threads. This translation is applied by both JNI and FFM modes.

> **Note**: `@Sendable` as a closure-parameter attribute is not yet supported; the environment captured inside the closure would need special handling.

## See Also

### Supported Features
- [Features Overview](./featuresoverview.md)
  Choosing the right swift-java tool for your interop task.
- [Features: JavaKit macros](./featuresjavakitmacros.md)
  Detailed feature documentation for calling Java from Swift using JavaKit macros (`@JavaClass`, `@JavaMethod`, `@JavaField`, `@JavaImplementation`, …).


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/swiftjavadocumentation/featuresjextract)*