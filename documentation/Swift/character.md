# Character

**Framework**: Swift  
**Kind**: struct

A single extended grapheme cluster that approximates a user-perceived character.

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
struct Character
```

#### Overview

The `Character` type represents a character made up of one or more Unicode scalar values, grouped by a Unicode boundary algorithm. Generally, a `Character` instance matches what the reader of a string will perceive as a single character. Strings are collections of `Character` instances, so the number of visible characters is generally the most natural way to count the length of a string.

```swift
let greeting = "Hello! 🐥"
print("Length: \(greeting.count)")
// Prints "Length: 8"
```

Because each character in a string can be made up of one or more Unicode scalar values, the number of characters in a string may not match the length of the Unicode scalar value representation or the length of the string in a particular binary representation.

```swift
print("Unicode scalar value count: \(greeting.unicodeScalars.count)")
// Prints "Unicode scalar value count: 8"

print("UTF-8 representation count: \(greeting.utf8.count)")
// Prints "UTF-8 representation count: 11"
```

Every `Character` instance is composed of one or more Unicode scalar values that are grouped together as an . The way these scalar values are grouped is defined by a canonical, localized, or otherwise tailored Unicode segmentation algorithm.

For example, a country’s Unicode flag character is made up of two regional indicator scalar values that correspond to that country’s ISO 3166-1 alpha-2 code. The alpha-2 code for The United States is “US”, so its flag character is made up of the Unicode scalar values `"\u{1F1FA}"` (REGIONAL INDICATOR SYMBOL LETTER U) and `"\u{1F1F8}"` (REGIONAL INDICATOR SYMBOL LETTER S). When placed next to each other in a string literal, these two scalar values are combined into a single grapheme cluster, represented by a `Character` instance in Swift.

```swift
let usFlag: Character = "\u{1F1FA}\u{1F1F8}"
print(usFlag)
// Prints "🇺🇸"
```

For more information about the Unicode terms used in this discussion, see the [`Unicode.org glossary`](https://developer.apple.comhttp://www.unicode.org/glossary/). In particular, this discussion mentions [`extended grapheme clusters`](https://developer.apple.comhttp://www.unicode.org/glossary/#extended_grapheme_cluster) and [`Unicode scalar values`](https://developer.apple.comhttp://www.unicode.org/glossary/#unicode_scalar_value).

## Topics

### Creating a Character
- [init(String)](character/init(_:)-6o1aq.md)
  Creates a character from a single-character string.
### Writing to a Text Stream
- [func write<Target>(to: inout Target)](character/write(to:).md)
  Writes the character into the given output stream.
### Comparing Characters
- [static func == (Character, Character) -> Bool](character/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](character/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Working with a Character’s Unicode Values
- [init(Unicode.Scalar)](character/init(_:)-8hq6x.md)
  Creates a character containing the given Unicode scalar value.
- [var unicodeScalars: Character.UnicodeScalarView](character/unicodescalars.md)
- [Character.UnicodeScalarView](character/unicodescalarview.md)
- [var isASCII: Bool](character/isascii.md)
  A Boolean value indicating whether this is an ASCII character.
- [var asciiValue: UInt8?](character/asciivalue.md)
  The ASCII encoding value of this character, if it is an ASCII character.
### Inspecting a Character
- [var isLetter: Bool](character/isletter.md)
  A Boolean value indicating whether this character is a letter.
- [var isPunctuation: Bool](character/ispunctuation.md)
  A Boolean value indicating whether this character represents punctuation.
- [var isNewline: Bool](character/isnewline.md)
  A Boolean value indicating whether this character represents a newline.
- [var isWhitespace: Bool](character/iswhitespace.md)
  A Boolean value indicating whether this character represents whitespace, including newlines.
- [var isSymbol: Bool](character/issymbol.md)
  A Boolean value indicating whether this character represents a symbol.
- [var isMathSymbol: Bool](character/ismathsymbol.md)
  A Boolean value indicating whether this character represents a symbol that naturally appears in mathematical contexts.
- [var isCurrencySymbol: Bool](character/iscurrencysymbol.md)
  A Boolean value indicating whether this character represents a currency symbol.
### Checking a Character’s Case
- [var isCased: Bool](character/iscased.md)
  A Boolean value indicating whether this character changes under any form of case conversion.
- [var isUppercase: Bool](character/isuppercase.md)
  A Boolean value indicating whether this character is considered uppercase.
- [func uppercased() -> String](character/uppercased.md)
  Returns an uppercased version of this character.
- [var isLowercase: Bool](character/islowercase.md)
  A Boolean value indicating whether this character is considered lowercase.
- [func lowercased() -> String](character/lowercased.md)
  Returns a lowercased version of this character.
### Checking a Character’s Numeric Properties
- [var isNumber: Bool](character/isnumber.md)
  A Boolean value indicating whether this character represents a number.
- [var isWholeNumber: Bool](character/iswholenumber.md)
  A Boolean value indicating whether this character represents a whole number.
- [var wholeNumberValue: Int?](character/wholenumbervalue.md)
  The numeric value this character represents, if it represents a whole number.
- [var isHexDigit: Bool](character/ishexdigit.md)
  A Boolean value indicating whether this character represents a hexadecimal digit.
- [var hexDigitValue: Int?](character/hexdigitvalue.md)
  The numeric value this character represents, if it is a hexadecimal digit.
### Creating a Range Expression
- [static func ... (Self, Self) -> ClosedRange<Self>](character/'...(_:_:).md)
  Returns a closed range that contains both of its bounds.
- [static func ... (Self) -> PartialRangeThrough<Self>](character/'...(_:)-4mm4x.md)
  Returns a partial range up to, and including, its upper bound.
- [static func ... (Self) -> PartialRangeFrom<Self>](character/'...(_:)-6ct59.md)
  Returns a partial range extending upward from a lower bound.
### Describing a Character
- [var description: String](character/description.md)
  A textual representation of this instance.
- [var debugDescription: String](character/debugdescription.md)
  A textual representation of the character, suitable for debugging.
- [var customMirror: Mirror](character/custommirror.md)
  A mirror that reflects the `Character` instance.
- [var customPlaygroundQuickLook: _PlaygroundQuickLook](character/customplaygroundquicklook.md)
  A custom playground Quick Look for the `Character` instance.
- [func hash(into: inout Hasher)](character/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Infrequently Used Functionality
- [init(extendedGraphemeClusterLiteral: Character)](character/init(extendedgraphemeclusterliteral:).md)
  Creates a character with the specified value.
- [init(unicodeScalarLiteral: Self.ExtendedGraphemeClusterLiteralType)](character/init(unicodescalarliteral:).md)
### Instance Properties
- [var utf16: Character.UTF16View](character/utf16.md)
  A UTF-16 encoding of `self`.
- [var utf8: Character.UTF8View](character/utf8.md)
  A UTF-8 encoding of `self`.
### Type Aliases
- [Character.Output](character/output.md)
- [Character.UTF16View](character/utf16view.md)
  A view of a character’s contents as a collection of UTF-16 code units. See String.UTF16View for more information
- [Character.UTF8View](character/utf8view.md)
  A view of a character’s contents as a collection of UTF-8 code units. See String.UTF8View for more information
### Default Implementations
- [Comparable Implementations](character/comparable-implementations.md)
- [CustomDebugStringConvertible Implementations](character/customdebugstringconvertible-implementations.md)
- [CustomReflectable Implementations](character/customreflectable-implementations.md)
- [CustomStringConvertible Implementations](character/customstringconvertible-implementations.md)
- [Equatable Implementations](character/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](character/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](character/expressiblebyunicodescalarliteral-implementations.md)
- [Hashable Implementations](character/hashable-implementations.md)
- [LosslessStringConvertible Implementations](character/losslessstringconvertible-implementations.md)
- [RegexComponent Implementations](character/regexcomponent-implementations.md)
- [TextOutputStreamable Implementations](character/textoutputstreamable-implementations.md)

## Relationships

### Conforms To
- [Comparable](comparable.md)
- [Copyable](copyable.md)
- [CustomDebugStringConvertible](customdebugstringconvertible.md)
- [CustomReflectable](customreflectable.md)
- [CustomStringConvertible](customstringconvertible.md)
- [Equatable](equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByUnicodeScalarLiteral](expressiblebyunicodescalarliteral.md)
- [Hashable](hashable.md)
- [LosslessStringConvertible](losslessstringconvertible.md)
- [RegexComponent](regexcomponent.md)
- [Sendable](sendable.md)
- [TextOutputStreamable](textoutputstreamable.md)

## See Also

- [struct String](string.md)
  A Unicode string value that is a collection of characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/character)*