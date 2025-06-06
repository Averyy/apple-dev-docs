# LanguageTag

**Framework**: PackageDescription  
**Kind**: struct

A wrapper around an IETF language tag.

## Declaration

```swift
struct LanguageTag
```

#### Overview

To learn more about the IETF worldwide standard for language tags, see [`RFC5646`](https://developer.apple.comhttps://tools.ietf.org/html/rfc5646).

## Topics

### Creating a Language Tag
- [init(extendedGraphemeClusterLiteral: String)](languagetag/init(extendedgraphemeclusterliteral:).md)
  Creates an instance initialized to the given value.
- [init(stringLiteral: String)](languagetag/init(stringliteral:).md)
  Creates an instance initialized to the given value.
- [init(unicodeScalarLiteral: String)](languagetag/init(unicodescalarliteral:).md)
  Creates an instance initialized to the given value.
- [init?(rawValue: String)](languagetag/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: String](languagetag/rawvalue-swift.property.md)
  The corresponding value of the raw type.
### Describing a Language Tag
- [var description: String](languagetag/description.md)
  A textual representation of the language tag.
### Hashing
- [func hash(into: inout Hasher)](languagetag/hash(into:).md)
  Hashes the language tag by feeding the item into the given hasher.
- [var hashValue: Int](languagetag/hashvalue.md)
  The hash value for language tag.
### Operator Functions
- [static func != (Self, Self) -> Bool](languagetag/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Identifying Related Types
- [LanguageTag.ExtendedGraphemeClusterLiteralType](languagetag/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [LanguageTag.RawValue](languagetag/rawvalue-swift.typealias.md)
  The raw type that can be used to represent all values of the conforming type.
- [LanguageTag.StringLiteralType](languagetag/stringliteraltype.md)
  A type that represents a string literal.
- [LanguageTag.UnicodeScalarLiteralType](languagetag/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Default Implementations
- [CustomStringConvertible Implementations](languagetag/customstringconvertible-implementations.md)
- [Equatable Implementations](languagetag/equatable-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](languagetag/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](languagetag/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](languagetag/expressiblebyunicodescalarliteral-implementations.md)
- [RawRepresentable Implementations](languagetag/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)

## See Also

- [var defaultLocalization: LanguageTag?](package/defaultlocalization.md)
  The default localization for resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/languagetag)*