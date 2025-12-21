# Unicode.Scalar

**Framework**: Swift  
**Kind**: struct

A Unicode scalar value.

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
struct Scalar
```

#### Overview

The `Unicode.Scalar` type, representing a single Unicode scalar value, is the element type of a string’s `unicodeScalars` collection.

You can create a `Unicode.Scalar` instance by using a string literal that contains a single character representing exactly one Unicode scalar value.

```swift
let letterK: Unicode.Scalar = "K"
let kim: Unicode.Scalar = "김"
print(letterK, kim)
// Prints "K 김"
```

You can also create Unicode scalar values directly from their numeric representation.

```swift
let airplane = Unicode.Scalar(9992)!
print(airplane)
// Prints "✈︎"
```

## Topics

### Creating a Scalar
- [init(UInt8)](unicode/scalar/init(_:)-2oo2e.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(Unicode.Scalar)](unicode/scalar/init(_:)-5d6us.md)
  Creates a duplicate of the given Unicode scalar.
- [init?(UInt32)](unicode/scalar/init(_:)-9eo1y.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(UInt16)](unicode/scalar/init(_:)-18u1m.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(Int)](unicode/scalar/init(_:)-96l5f.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(unicodeScalarLiteral: Unicode.Scalar)](unicode/scalar/init(unicodescalarliteral:).md)
  Creates a Unicode scalar with the specified value.
- [init?(String)](unicode/scalar/init(_:)-4p868.md)
  Instantiates an instance of the conforming type from a string representation.
### Inspecting a Scalar
- [var value: UInt32](unicode/scalar/value.md)
  A numeric representation of the Unicode scalar.
- [var properties: Unicode.Scalar.Properties](unicode/scalar/properties-swift.property.md)
  Properties of this scalar defined by the Unicode standard.
- [Unicode.Scalar.Properties](unicode/scalar/properties-swift.struct.md)
  A value that provides access to properties of a Unicode scalar that are defined by the Unicode standard.
- [func hash(into: inout Hasher)](unicode/scalar/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var isASCII: Bool](unicode/scalar/isascii.md)
  A Boolean value indicating whether the Unicode scalar is an ASCII character.
### Printing and Displaying a Scalar
- [var description: String](unicode/scalar/description.md)
  A textual representation of the Unicode scalar.
- [func write<Target>(to: inout Target)](unicode/scalar/write(to:).md)
  Writes the textual representation of the Unicode scalar into the given output stream.
- [func escaped(asASCII: Bool) -> String](unicode/scalar/escaped(asascii:).md)
  Returns a string representation of the Unicode scalar.
- [var utf16: Unicode.Scalar.UTF16View](unicode/scalar/utf16.md)
- [Unicode.Scalar.UTF16View](unicode/scalar/utf16view.md)
- [var debugDescription: String](unicode/scalar/debugdescription.md)
  An escaped textual representation of the Unicode scalar, suitable for debugging.
- [var customMirror: Mirror](unicode/scalar/custommirror.md)
  A mirror that reflects the `Unicode.Scalar` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](unicode/scalar/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Unicode.Scalar` instance.
### Comparing Scalars
- [static func == (Unicode.Scalar, Unicode.Scalar) -> Bool](unicode/scalar/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](unicode/scalar/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func < (Unicode.Scalar, Unicode.Scalar) -> Bool](unicode/scalar/_(_:_:).md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
- [static func <= (Self, Self) -> Bool](unicode/scalar/_=(_:_:)-13yar.md)
  Returns a Boolean value indicating whether the value of the first argument is less than or equal to that of the second argument.
- [static func > (Self, Self) -> Bool](unicode/scalar/_(_:_:)-1xeim.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than that of the second argument.
- [static func >= (Self, Self) -> Bool](unicode/scalar/_=(_:_:)-7oywq.md)
  Returns a Boolean value indicating whether the value of the first argument is greater than or equal to that of the second argument.
### Creating Ranges of Scalars
- [static func ... (Self) -> PartialRangeFrom<Self>](unicode/scalar/'...(_:)-9u9rz.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](unicode/scalar/'...(_:)-7lhvp.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](unicode/scalar/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [static func ..< (Self) -> PartialRangeUpTo<Self>](unicode/scalar/'.._(_:).md)
  Returns a partial range up to, but not including, its upper bound.
- [static func ..< (Self, Self) -> Range<Self>](unicode/scalar/'.._(_:_:).md)
  Returns a half-open range that contains its lower bound but not its upper bound.
### Structures
- [Unicode.Scalar.UTF8View](unicode/scalar/utf8view.md)
### Instance Properties
- [var utf8: Unicode.Scalar.UTF8View](unicode/scalar/utf8.md)
### Type Aliases
- [Unicode.Scalar.Output](unicode/scalar/output.md)
### Default Implementations
- [Comparable Implementations](unicode/scalar/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](unicode/scalar/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](unicode/scalar/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](unicode/scalar/customstringconvertible-implementations.md)
- [Equatable Implementations](unicode/scalar/equatable-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](unicode/scalar/expressiblebyunicodescalarliteral-implementations.md)
- [Hashable Implementations](unicode/scalar/hashable-implementations.md)
- [LosslessStringConvertible Implementations](unicode/scalar/losslessstringconvertible-implementations.md)
- [TextOutputStreamable Implementations](unicode/scalar/textoutputstreamable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](bitwisecopyable.md)
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md)
- [Hashable](hashable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [RegexComponent](regexcomponent.md)
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
- [TextOutputStreamable](textoutputstreamable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar)*