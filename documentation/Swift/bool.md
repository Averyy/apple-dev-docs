# Bool

**Framework**: Swift  
**Kind**: struct

A value type whose instances are either `true` or `false`.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@frozen
struct Bool
```

#### Overview

`Bool` represents Boolean values in Swift. Create instances of `Bool` by using one of the Boolean literals `true` or `false`, or by assigning the result of a Boolean method or operation to a variable or constant.

```swift
var godotHasArrived = false

let numbers = 1...5
let containsTen = numbers.contains(10)
print(containsTen)
// Prints "false"

let (a, b) = (100, 101)
let aFirst = a < b
print(aFirst)
// Prints "true"
```

Swift uses only simple Boolean values in conditional contexts to help avoid accidental programming errors and to help maintain the clarity of each control statement. Unlike in other programming languages, in Swift, integers and strings cannot be used where a Boolean value is required.

For example, the following code sample does not compile, because it attempts to use the integer `i` in a logical context:

```swift
var i = 5
while i {
    print(i)
    i -= 1
}
// error: Cannot convert value of type 'Int' to expected condition type 'Bool'
```

The correct approach in Swift is to compare the `i` value with zero in the `while` statement.

```swift
while i != 0 {
    print(i)
    i -= 1
}
```

### Using Imported Boolean Values

The C `bool` and `Boolean` types and the Objective-C `BOOL` type are all bridged into Swift as `Bool`. The single `Bool` type in Swift guarantees that functions, methods, and properties imported from C and Objective-C have a consistent type interface.

## Topics

### Comparing Boolean Values
- [static func == (Bool, Bool) -> Bool](bool/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](bool/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Transforming a Boolean
- [func toggle()](bool/toggle.md)
  Toggles the Boolean variable’s value.
- [static func ! (Bool) -> Bool](bool/!(_:).md)
  Performs a logical NOT operation on a Boolean value.
- [static func || (Bool, @autoclosure () throws -> Bool) rethrows -> Bool](bool/__(_:_:).md)
  Performs a logical OR operation on two Boolean values.
- [static func && (Bool, @autoclosure () throws -> Bool) rethrows -> Bool](bool/&&(_:_:).md)
  Performs a logical AND operation on two Boolean values.
### Creating a Random Value
- [static func random() -> Bool](bool/random.md)
  Returns a random Boolean value.
- [static func random<T>(using: inout T) -> Bool](bool/random(using:).md)
  Returns a random Boolean value, using the given generator as a source for randomness.
### Describing a Boolean
- [var description: String](bool/description.md)
  A textual representation of the Boolean value.
### Inspecting a Boolean
- [var customMirror: Mirror](bool/custommirror.md)
  A mirror that reflects the `Bool` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](bool/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Bool` instance.
- [var hashValue: Int](bool/hashvalue.md)
  The hash value.
- [func hash(into: inout Hasher)](bool/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Creating a Boolean From Another Value
- [init(Bool)](bool/init(_:)-25sp9.md)
  Creates an instance equal to the given Boolean value.
- [init?(String)](bool/init(_:)-83vgw.md)
  Creates a new Boolean value from the given string.
### Converting an NSNumber to a Boolean
- [init(NSNumber)](bool/init(_:)-3mody.md)
- [init?(exactly: NSNumber)](bool/init(exactly:).md)
- [init(truncating: NSNumber)](bool/init(truncating:).md)
### Encoding and Decoding
- [init(from: any Decoder) throws](bool/init(from:)-99p2s.md)
  Creates a new instance by decoding from the given decoder.
- [func encode(to: any Encoder) throws](bool/encode(to:).md)
  Encodes this value into the given encoder.
### Using a Boolean as a Data Value
- [init?(from: MLDataValue)](bool/init(from:)-4iol.md)
  Creates an instance of the conforming type from a data value.
- [var dataValue: MLDataValue](bool/datavalue.md)
  The value of the conforming type’s instance wrapped in a data value.
- [static var dataValueType: MLDataValue.ValueType](bool/datavaluetype.md)
  The underlying type the conforming type uses when it wraps itself in a data value.
### Infrequently Used Intializers
- [init()](bool/init.md)
  Creates an instance initialized to `false`.
- [init(booleanLiteral: Bool)](bool/init(booleanliteral:).md)
  Creates an instance initialized to the specified Boolean literal.
### Structures
- [struct IntentDisplayName](bool/intentdisplayname.md)
### Type Aliases
- [typealias Specification](bool/specification.md)
- [typealias UnwrappedType](bool/unwrappedtype.md)
- [typealias ValueType](bool/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: some ResolverSpecification](bool/defaultresolverspecification.md)
### Default Implementations
- [AtomicRepresentable Implementations](bool/atomicrepresentable-implementations.md)
- [ConvertibleFromGeneratedContent Implementations](bool/convertiblefromgeneratedcontent-implementations.md)
- [ConvertibleToGeneratedContent Implementations](bool/convertibletogeneratedcontent-implementations.md)
- [CustomReflectable Implementations](bool/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](bool/customstringconvertible-implementations.md)
- [Decodable Implementations](bool/decodable-implementations.md)
- [Encodable Implementations](bool/encodable-implementations.md)
- [Equatable Implementations](bool/equatable-implementations.md)
- [ExpressibleByBooleanLiteral Implementations](bool/expressiblebybooleanliteral-implementations.md)
- [Generable Implementations](bool/generable-implementations.md)
- [Hashable Implementations](bool/hashable-implementations.md)
- [InstructionsRepresentable Implementations](bool/instructionsrepresentable-implementations.md)
- [LosslessStringConvertible Implementations](bool/losslessstringconvertible-implementations.md)
- [MLDataValueConvertible Implementations](bool/mldatavalueconvertible-implementations.md)
- [PromptRepresentable Implementations](bool/promptrepresentable-implementations.md)

## Relationships

### Conforms To
- [AtomicRepresentable](../synchronization/atomicrepresentable.md)
- [BNNSScalar](../Accelerate/BNNSScalar.md)
- [BindableData](../RealityKit/BindableData.md)
- [BitwiseCopyable](bitwisecopyable.md)
- [CKRecordValueProtocol](../CloudKit/CKRecordValueProtocol.md)
- [CVarArg](cvararg.md)
- [ConvertibleFromGeneratedContent](../FoundationModels/ConvertibleFromGeneratedContent.md)
- [ConvertibleToGeneratedContent](../FoundationModels/ConvertibleToGeneratedContent.md)
- [Copyable](copyable.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [ExpressibleByBooleanLiteral](expressiblebybooleanliteral.md)
- [Generable](../FoundationModels/Generable.md)
- [Hashable](hashable.md)
- [InstructionsRepresentable](../FoundationModels/InstructionsRepresentable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [MLDataValueConvertible](../CreateML/MLDataValueConvertible.md)
- [MLTensorScalar](../CoreML/MLTensorScalar.md)
- [MusicLibraryRequestFilterValueEquatable](../MusicKit/MusicLibraryRequestFilterValueEquatable.md)
- [PDFObjectType](../CoreGraphics/PDFObjectType.md)
- [PromptRepresentable](../FoundationModels/PromptRepresentable.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/bool)*