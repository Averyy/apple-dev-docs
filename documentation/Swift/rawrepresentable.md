# RawRepresentable

**Framework**: Swift  
**Kind**: protocol

A type that can be converted to and from an associated raw value.

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
protocol RawRepresentable<RawValue>
```

#### Overview

With a `RawRepresentable` type, you can switch back and forth between a custom type and an associated `RawValue` type without losing the value of the original `RawRepresentable` type. Using the raw value of a conforming type streamlines interoperation with Objective-C and legacy APIs and simplifies conformance to other protocols, such as `Equatable`, `Comparable`, and `Hashable`.

The `RawRepresentable` protocol is seen mainly in two categories of types: enumerations with raw value types and option sets.

### Enumerations with Raw Values

For any enumeration with a string, integer, or floating-point raw type, the Swift compiler automatically adds `RawRepresentable` conformance. When defining your own custom enumeration, you give it a raw type by specifying the raw type as the first item in the enumeration’s type inheritance list. You can also use literals to specify values for one or more cases.

For example, the `Counter` enumeration defined here has an `Int` raw value type and gives the first case a raw value of `1`:

```swift
enum Counter: Int {
    case one = 1, two, three, four, five
}
```

You can create a `Counter` instance from an integer value between 1 and 5 by using the `init?(rawValue:)` initializer declared in the `RawRepresentable` protocol. This initializer is failable because although every case of the `Counter` type has a corresponding `Int` value, there are many `Int` values that  correspond to a case of `Counter`.

```swift
for i in 3...6 {
    print(Counter(rawValue: i))
}
// Prints "Optional(Counter.three)"
// Prints "Optional(Counter.four)"
// Prints "Optional(Counter.five)"
// Prints "nil"
```

### Option Sets

Option sets all conform to `RawRepresentable` by inheritance using the `OptionSet` protocol. Whether using an option set or creating your own, you use the raw value of an option set instance to store the instance’s bitfield. The raw value must therefore be of a type that conforms to the `FixedWidthInteger` protocol, such as `UInt8` or `Int`. For example, the `Direction` type defines an option set for the four directions you can move in a game.

```swift
struct Directions: OptionSet {
    let rawValue: UInt8

    static let up    = Directions(rawValue: 1 << 0)
    static let down  = Directions(rawValue: 1 << 1)
    static let left  = Directions(rawValue: 1 << 2)
    static let right = Directions(rawValue: 1 << 3)
}
```

Unlike enumerations, option sets provide a nonfailable `init(rawValue:)` initializer to convert from a raw value, because option sets don’t have an enumerated list of all possible cases. Option set values have a one-to-one correspondence with their associated raw values.

In the case of the `Directions` option set, an instance can contain zero, one, or more of the four defined directions. This example declares a constant with three currently allowed moves. The raw value of the `allowedMoves` instance is the result of the bitwise OR of its three members’ raw values:

```swift
let allowedMoves: Directions = [.up, .down, .left]
print(allowedMoves.rawValue)
// Prints "7"
```

Option sets use bitwise operations on their associated raw values to implement their mathematical set operations. For example, the `contains()` method on `allowedMoves` performs a bitwise AND operation to check whether the option set contains an element.

```swift
print(allowedMoves.contains(.right))
// Prints "false"
print(allowedMoves.rawValue & Directions.right.rawValue)
// Prints "0"
```

## Topics

### Creating a Value
- [init?(rawValue: Self.RawValue)](rawrepresentable/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
### Accessing the Raw Value
- [var rawValue: Self.RawValue](rawrepresentable/rawvalue-swift.property.md)
  The corresponding value of the raw type.
- [associatedtype RawValue](rawrepresentable/rawvalue-swift.associatedtype.md)
  The raw type that can be used to represent all values of the conforming type.
### Comparing Values
- [func == <T>(T, T) -> Bool](==(_:_:)-9hu5c.md)
  Returns a Boolean value indicating whether the two arguments are equal.
- [func != <T>(T, T) -> Bool](!=(_:_:)-9wy5n.md)
  Returns a Boolean value indicating whether the two arguments are not equal.
- [func != <T>(T, T) -> Bool](!=(_:_:)-8pggn.md)
  Returns a Boolean value indicating whether the two arguments are not equal.
### Decoding a Value
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-5auil.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `String`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-5ar5m.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Bool`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-417i8.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Double`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-9u9tp.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Float`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-4ibll.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-3hvw1.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-5ktev.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int8`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-2hvc0.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int16`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-114vz.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int32`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-29lhi.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int64`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-94955.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt8`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-6z4x4.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt16`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-3arr3.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt32`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-812cy.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt64`.
### Encoding a Value
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-4evma.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `String`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-5igsi.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Bool`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-4tbh4.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Double`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-21ma8.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Float`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-8horh.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-78oqu.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-4pavm.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int8`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-86dqn.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int16`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-7dyeb.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int32`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-4gohs.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int64`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-9u5rt.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt8`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-cla3.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt16`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-27waz.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt32`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-16ame.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt64`.
### Initializers
- [init?<T>(codingKey: T)](rawrepresentable/init(codingkey:)-3mxjn.md)
- [init?<T>(codingKey: T)](rawrepresentable/init(codingkey:)-9gih0.md)
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-6yajb.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `UInt128`.
- [init(from: any Decoder) throws](rawrepresentable/init(from:)-8fm8i.md)
  Creates a new instance by decoding from the given decoder, when the type’s `RawValue` is `Int128`.
### Instance Properties
- [var codingKey: any CodingKey](rawrepresentable/codingkey-2f0gm.md)
- [var codingKey: any CodingKey](rawrepresentable/codingkey-xnw1.md)
- [var hashValue: Int](rawrepresentable/hashvalue.md)
### Instance Methods
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-172ut.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `Int128`.
- [func encode(to: any Encoder) throws](rawrepresentable/encode(to:)-3ahar.md)
  Encodes this value into the given encoder, when the type’s `RawValue` is `UInt128`.
- [func hash(into: inout Hasher)](rawrepresentable/hash(into:).md)
### Type Aliases
- [RawRepresentable.AtomicOptionalRepresentation](rawrepresentable/atomicoptionalrepresentation.md)
  The storage representation type that encodes to and decodes from `Optional<Self>` which is a suitable type when used in atomic operations on `Optional`.
- [RawRepresentable.AtomicRepresentation](rawrepresentable/atomicrepresentation.md)
  The storage representation type that `Self` encodes to and decodes from which is a suitable type when used in atomic operations.
### Type Methods
- [static func decodeAtomicOptionalRepresentation(consuming Self.RawValue.AtomicOptionalRepresentation) -> Self?](rawrepresentable/decodeatomicoptionalrepresentation(_:).md)
  Recovers the logical atomic type `Self?` by destroying some `AtomicOptionalRepresentation` storage instance returned from an atomic operation on `Optional`.
- [static func decodeAtomicRepresentation(consuming Self.RawValue.AtomicRepresentation) -> Self](rawrepresentable/decodeatomicrepresentation(_:).md)
  Recovers the logical atomic type `Self` by destroying some `AtomicRepresentation` storage instance returned from an atomic operation.
- [static func encodeAtomicOptionalRepresentation(consuming Self?) -> Self.RawValue.AtomicOptionalRepresentation](rawrepresentable/encodeatomicoptionalrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicOptionalRepresentation` storage type to be used for atomic operations on `Optional`.
- [static func encodeAtomicRepresentation(consuming Self) -> Self.RawValue.AtomicRepresentation](rawrepresentable/encodeatomicrepresentation(_:).md)
  Destroys a value of `Self` and prepares an `AtomicRepresentation` storage type to be used for atomic operations.

## Relationships

### Inherited By
- [OptionSet](optionset.md)
### Conforming Types
- [CodingUserInfoKey](codinguserinfokey.md)
- [FloatingPointSign](floatingpointsign.md)
- [String.Encoding](string/encoding.md)
- [TaskPriority](taskpriority.md)
- [Unicode.CanonicalCombiningClass](unicode/canonicalcombiningclass.md)

## See Also

- [protocol CaseIterable](caseiterable.md)
  A type that provides a collection of all of its values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/rawrepresentable)*