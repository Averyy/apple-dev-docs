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
### Describing a Language Tag
- [var description: String](languagetag/description.md)
  A textual representation of the language tag.
### Default Implementations
- [CustomStringConvertible Implementations](languagetag/customstringconvertible-implementations.md)
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