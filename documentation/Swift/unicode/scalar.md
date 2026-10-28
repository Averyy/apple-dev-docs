# Unicode.Scalar

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

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

## Overview

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
- [init(UInt8)](./scalar/init%28_%29-2oo2e.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(Unicode.Scalar)](./scalar/init%28_%29-5d6us.md)
  Creates a duplicate of the given Unicode scalar.
- [init?(UInt32)](./scalar/init%28_%29-9eo1y.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(UInt16)](./scalar/init%28_%29-18u1m.md)
  Creates a Unicode scalar with the specified numeric value.
- [init?(Int)](./scalar/init%28_%29-96l5f.md)
  Creates a Unicode scalar with the specified numeric value.
- [init(unicodeScalarLiteral: Unicode.Scalar)](./scalar/init%28unicodescalarliteral%29.md)
  Creates a Unicode scalar with the specified value.
- [init?(String)](./scalar/init%28_%29-4p868.md)
  Instantiates an instance of the conforming type from a string representation.
### Inspecting a Scalar
- [var value: UInt32](./scalar/value.md)
  A numeric representation of the Unicode scalar.
- [var properties: Unicode.Scalar.Properties](./scalar/properties-swift.property.md)
  Properties of this scalar defined by the Unicode standard.
- [Unicode.Scalar.Properties](./scalar/properties-swift.struct.md)
  A value that provides access to properties of a Unicode scalar that are defined by the Unicode standard.
- [func hash(into: inout Hasher)](./scalar/hash%28into%29.md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var isASCII: Bool](./scalar/isascii.md)
  A Boolean value indicating whether the Unicode scalar is an ASCII character.
### Printing and Displaying a Scalar
- [var description: String](./scalar/description.md)
  A textual representation of the Unicode scalar.
- [func write<Target>(to: inout Target)](./scalar/write%28to%29.md)
  Writes the textual representation of the Unicode scalar into the given output stream.
- [func escaped(asASCII: Bool) -> String](./scalar/escaped%28asascii%29.md)
  Returns a string representation of the Unicode scalar.
- [var utf16: Unicode.Scalar.UTF16View](./scalar/utf16.md)
- [Unicode.Scalar.UTF16View](./scalar/utf16view.md)
- [var debugDescription: String](./scalar/debugdescription.md)
  An escaped textual representation of the Unicode scalar, suitable for debugging.
- [var customMirror: Mirror](./scalar/custommirror.md)
  A mirror that reflects the `Unicode.Scalar` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](./scalar/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Unicode.Scalar` instance.
### Comparing Scalars
- [static func == (Unicode.Scalar, Unicode.Scalar) -> Bool](./scalar/eqeq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (borrowing Self, borrowing Self) -> Bool](./scalar/noteq%28_,_%29.md)
  Returns a Boolean value indicating whether two values are not equal.
- [static func < (Unicode.Scalar, Unicode.Scalar) -> Bool](./scalar/op%28_,_%29.md)
  Returns a Boolean value indicating whether the value of the first argument is less than that of the second argument.
### Creating Ranges of Scalars
- [static func ... (Self) -> PartialRangeFrom<Self>](./scalar/dotdotdot%28_%29-9u9rz.md)
  Returns a partial range extending upward from a lower bound.
- [static func ... (Self) -> PartialRangeThrough<Self>](./scalar/dotdotdot%28_%29-7lhvp.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self, Self) -> ClosedRange<Self>](./scalar/dotdotdot%28_,_%29.md)
  Returns a closed range that contains both of its bounds.
- [static func ..< (Self) -> PartialRangeUpTo<Self>](./scalar/dotdotop%28_%29.md)
  Returns a partial range up to, but not including, its upper bound.
- [static func ..< (Self, Self) -> Range<Self>](./scalar/dotdotop%28_,_%29.md)
  Returns a half-open range that contains its lower bound but not its upper bound.
### Structures
- [Unicode.Scalar.UTF8View](./scalar/utf8view.md)
### Instance Properties
- [var utf8: Unicode.Scalar.UTF8View](./scalar/utf8.md)
### Type Aliases
- [Unicode.Scalar.Output](./scalar/output.md)
### Default Implementations
- [Comparable Implementations](./scalar/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](./scalar/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](./scalar/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](./scalar/customstringconvertible-implementations.md)
- [Equatable Implementations](./scalar/equatable-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](./scalar/expressiblebyunicodescalarliteral-implementations.md)
- [Hashable Implementations](./scalar/hashable-implementations.md)
- [LosslessStringConvertible Implementations](./scalar/losslessstringconvertible-implementations.md)
- [TextOutputStreamable Implementations](./scalar/textoutputstreamable-implementations.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../bitwisecopyable.md)
- [Comparable](../comparable.md)
- [Copyable](../copyable.md)
- [CustomDebugStringConvertible](../customdebugstringconvertible.md)
- [CustomReflectable](../customreflectable.md)
- [CustomStringConvertible](../customstringconvertible.md)
- [Equatable](../equatable.md)
- [Escapable](../escapable.md)
- [ExpressibleByUnicodeScalarLiteral](../expressiblebyunicodescalarliteral.md)
- [Hashable](../hashable.md)
- [LosslessStringConvertible](../losslessstringconvertible.md)
- [RegexComponent](../regexcomponent.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)
- [TextOutputStreamable](../textoutputstreamable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unicode/scalar)*