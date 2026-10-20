# LanguageTag

**Framework**: PackageDescription  
**Kind**: struct  
**Role**: Structure

A wrapper around an IETF language tag.

## Declaration

```swift
struct LanguageTag
```

#### Overview

To learn more about the IETF worldwide standard for language tags, see [RFC5646](https://tools.ietf.org/html/rfc5646).

## Topics

### Creating a Language Tag
- [init(extendedGraphemeClusterLiteral: String)](./languagetag/init%28extendedgraphemeclusterliteral%29.md)
  Creates an instance initialized to the given value.
- [init(stringLiteral: String)](./languagetag/init%28stringliteral%29.md)
  Creates an instance initialized to the given value.
- [init(unicodeScalarLiteral: String)](./languagetag/init%28unicodescalarliteral%29.md)
  Creates an instance initialized to the given value.
- [init?(rawValue: String)](./languagetag/init%28rawvalue%29.md)
  Creates a new instance with the specified raw value.
### Describing a Language Tag
- [var description: String](./languagetag/description.md)
  A textual representation of the language tag.
### Default Implementations
- [CustomStringConvertible Implementations](./languagetag/customstringconvertible-implementations.md)
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](./languagetag/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringLiteral Implementations](./languagetag/expressiblebystringliteral-implementations.md)
- [ExpressibleByUnicodeScalarLiteral Implementations](./languagetag/expressiblebyunicodescalarliteral-implementations.md)
- [RawRepresentable Implementations](./languagetag/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/expressiblebyextendedgraphemeclusterliteral.md)
- [ExpressibleByStringLiteral](../Swift/expressiblebystringliteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/expressiblebyunicodescalarliteral.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)

## See Also

### Localizing Package Resources
- [var defaultLocalization: LanguageTag?](./package/defaultlocalization.md)
  The default localization for resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/packagedescription/languagetag)*