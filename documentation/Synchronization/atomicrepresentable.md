# AtomicRepresentable

**Framework**: Synchronization  
**Kind**: protocol

A type that supports atomic operations through a separate atomic storage representation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
protocol AtomicRepresentable
```

#### Overview

Types that conform to the `AtomicRepresentable` protocol can be used as the `Value` type parameter with the `Atomic` type. Conformances that utilize existing atomic storage representations as their own representation will get the primitive atomic operations available on `Atomic` for free. Such operations include `load`, `store`, `exchange`, `compareExchange`, and `weakCompareExchange`.

#### Conforming to the Atomicrepresentable Protocol

Conforming your own custom types allow them to be used in the `Atomic` type and get access to all of the primitive atomic operations explained above. There are two main ways to conform your type to `AtomicRepresentable`:

1. Using a predefined `RawRepresentable` conformance
2. Manually conforming to `AtomicRepresentable`

If you custom type already conforms to `RawRepresentable`, then adding the `AtomicRepresentable` conformance may be really simple! If the `RawValue` associated type of your type is already itself an `AtomicRepresentable`, then all you need to do is add the conformance and you’re done!

```swift
enum TrafficLight: UInt8 {
  case red
  case yellow
  case green
}

extension TrafficLight: AtomicRepresentable {}
```

And that’s it! Here, we’re utilizing Swift’s automatic `RawRepresentable` conformance synthesis for enums by declaring our “raw value” to be a `UInt8`. By adding the `AtomicRepresentable` conformance, we automatically figure out how to do the conformance from the `RawRepresentable` implementation and do all of th necessary work for you. However, it is still possible to customize this behavior using the manual method explained below.

Defining your own `AtomicRepresentable` conformance is pretty simple. All you have to do is decide what atomic storage representation fits best for your type, and create the bidirectional relationship between the two.

```swift
// A point in an x-y coordinate system.
struct GridPoint {
  var x: Int
  var y: Int
}

extension GridPoint: AtomicRepresentable {
  typealias AtomicRepresentation = WordPair.AtomicRepresentation

  static func encodeAtomicRepresentation(
    _ value: consuming GridPoint
  ) -> AtomicRepresentation {
    let wordPair = WordPair(
      first: UInt(bitPattern: value.x),
      second: UInt(bitPattern: value.y)
    )

    return WordPair.encodeAtomicRepresentation(wordPair)
  }

  static func decodeAtomicRepresentation(
    _ representation: consuming AtomicRepresentation
  ) -> GridPoint {
    let wordPair = WordPair.decodeAtomicRepresentation(representation)

    return GridPoint(
      x: Int(bitPattern: wordPair.first),
      y: Int(bitPattern: wordPair.second)
    )
  }
}
```

Here, we’re going to select `WordPair`’s atomic storage representation as our own. This is very important because we only get the atomic operations like `load` and `store` if our representation is one of the  storage representations. Luckily for us, `WordPair` does use one of these types as its storage type.

In addition to selecting what storage representation our type will use, we define two static functions that go from both our custom type to its representation and the representation back to our own type. Because our representation is the same as `WordPair.AtomicRepresentation`, we will actually go through `WordPair`’s `AtomicRepresentable` conformance to help define our own.

This is all you need to do to conform your custom type to the `AtomicRepresentable` protocol. From here, you can use this type in all of the primitive atomic operations like shown below:

```swift
func atomicGridPoint(_ gridPoint: Atomic<GridPoint>) {
  let newGridPoint = GridPoint(x: 123, y: -456)

  let oldGridPoint1 = gridPoint.load(ordering: .relaxed)

  gridPoint.store(newGridPoint, ordering: .releasing)

  let oldGridPoint2 = gridPoint.exchange(
    desired: oldGridPoint1,
    ordering: .acquiringAndReleasing
  )

  let (exchanged1, oldGridPoint2) = gridPoint.compareExchange(
    expected: oldGridPoint1,
    desired: newGridPoint,
    ordering: .sequentiallyConsistent
  )

  let (exchanged2, oldGridPoint3) = gridPoint.weakCompareExchange(
    expected: newGridPoint,
    desired: oldGridPoint2,
    ordering: .relaxed
  )
}
```

#### List of Fundamental Atomic Representations

When defining your own `AtomicRepresentable` conformance, it is critical that your custom type should choose from the following list of types as its own `AtomicRepresentation`:

- `UInt8.AtomicRepresentation`
- `UInt16.AtomicRepresentation`
- `UInt32.AtomicRepresentation`
- `UInt64.AtomicRepresentation`
- `UInt.AtomicRepresentation`
- `Int8.AtomicRepresentation`
- `Int16.AtomicRepresentation`
- `Int32.AtomicRepresentation`
- `Int64.AtomicRepresentation`
- `Int.AtomicRepresentation`
- `WordPair.AtomicRepresentation`

> **Note**: `Int8.AtomicRepresentation` is the same type as `UInt8.AtomicRepresentation` and the same is true for all of the same sized integer types. If your type wraps an unsigned integer, you should prefer to use an unsigned integer’s atomic representation instead of a signed ones and vice versa. `Int` and `UInt`’s representation will be 64 bits wide on 64 bit systems and 32 bit wide on 32 bit systems. `Int64` and `UInt64` always conform to `AtomicRepresentable` on 64 bit systems, but on 32 bit systems they will only conform if the platform supports double wide atomics. `WordPair` will only conform to `AtomicRepresentable` on platforms that support double wide atomics, but if they do it will be 128 bits wide on 64 bit systems and 64 bits wide on 32 bit systems.

## Topics

### Associated Types
- [associatedtype AtomicRepresentation : BitwiseCopyable](atomicrepresentable/atomicrepresentation.md)
  The storage representation type that `Self` encodes to and decodes from which is a suitable type when used in atomic operations.
### Type Methods
- [static func decodeAtomicRepresentation(consuming Self.AtomicRepresentation) -> Self](atomicrepresentable/decodeatomicrepresentation(_:).md)
  Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [static func encodeAtomicRepresentation(consuming Self) -> Self.AtomicRepresentation](atomicrepresentable/encodeatomicrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.

## Relationships

### Inherited By
- [AtomicOptionalRepresentable](atomicoptionalrepresentable.md)
### Conforming Types
- [Bool](../swift/bool.md)
- [Double](../swift/double.md)
- [Duration](../swift/duration.md)
- [Float](../swift/float.md)
- [Float16](../swift/float16.md)
- [Int](../swift/int.md)
- [Int128](../swift/int128.md)
- [Int16](../swift/int16.md)
- [Int32](../swift/int32.md)
- [Int64](../swift/int64.md)
- [Int8](../swift/int8.md)
- [Never](../swift/never.md)
- [ObjectIdentifier](../swift/objectidentifier.md)
- [OpaquePointer](../swift/opaquepointer.md)
- [Optional](../swift/optional.md)
- [UInt](../swift/uint.md)
- [UInt128](../swift/uint128.md)
- [UInt16](../swift/uint16.md)
- [UInt32](../swift/uint32.md)
- [UInt64](../swift/uint64.md)
- [UInt8](../swift/uint8.md)
- [Unmanaged](../swift/unmanaged.md)
- [UnsafeBufferPointer](../swift/unsafebufferpointer.md)
- [UnsafeMutableBufferPointer](../swift/unsafemutablebufferpointer.md)
- [UnsafeMutablePointer](../swift/unsafemutablepointer.md)
- [UnsafeMutableRawBufferPointer](../swift/unsafemutablerawbufferpointer.md)
- [UnsafeMutableRawPointer](../swift/unsafemutablerawpointer.md)
- [UnsafePointer](../swift/unsafepointer.md)
- [UnsafeRawBufferPointer](../swift/unsaferawbufferpointer.md)
- [UnsafeRawPointer](../swift/unsaferawpointer.md)
- [WordPair](wordpair.md)

## See Also

- [struct Atomic](atomic.md)
  An atomic value.
- [struct AtomicLazyReference](atomiclazyreference.md)
  A lazily initializable atomic strong reference.
- [struct WordPair](wordpair.md)
  A pair of two word sized `UInt`s.
- [protocol AtomicOptionalRepresentable](atomicoptionalrepresentable.md)
  An atomic value that also supports atomic operations when wrapped in an `Optional`. Atomic optional representable types come with a standalone atomic representation for their optional-wrapped variants.


---

*[View on Apple Developer](https://developer.apple.com/documentation/synchronization/atomicrepresentable)*