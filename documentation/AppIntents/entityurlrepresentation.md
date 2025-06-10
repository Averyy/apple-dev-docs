# EntityURLRepresentation

**Framework**: App Intents  
**Kind**: struct

The URL representation of an app entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst ?+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
struct EntityURLRepresentation<Entity> where Entity : AppEntity
```

#### Overview

Note that you need to use a universal link for your URL representation, you can’t use a custom URL scheme. For more information about universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

## Topics

### Initializers
- [init(String)](entityurlrepresentation/init(_:).md)
- [init(stringInterpolation: EntityURLRepresentation<Entity>.StringInterpolation)](entityurlrepresentation/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.
- [init(stringLiteral: String)](entityurlrepresentation/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
### Type Aliases
- [EntityURLRepresentation.ExtendedGraphemeClusterLiteralType](entityurlrepresentation/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [EntityURLRepresentation.StringLiteralType](entityurlrepresentation/stringliteraltype.md)
  A type that represents a string literal.
- [EntityURLRepresentation.UnicodeScalarLiteralType](entityurlrepresentation/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](entityurlrepresentation/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](entityurlrepresentation/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](entityurlrepresentation/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/entityurlrepresentation)*