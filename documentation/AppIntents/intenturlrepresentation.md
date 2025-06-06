# IntentURLRepresentation

**Framework**: App Intents  
**Kind**: struct

The URL representation of an app intent.

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
struct IntentURLRepresentation<Intent> where Intent : AppIntent
```

#### Overview

Note that you need to use a universal link for your URL representation, you can’t use a custom URL scheme. For more information about universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

## Topics

### Initializers
- [init(String)](intenturlrepresentation/init(_:).md)
- [init(stringInterpolation: IntentURLRepresentation<Intent>.StringInterpolation)](intenturlrepresentation/init(stringinterpolation:).md)
  Creates an instance from a string interpolation.
- [init(stringLiteral: String)](intenturlrepresentation/init(stringliteral:).md)
  Creates an instance initialized to the given string value.
### Type Aliases
- [IntentURLRepresentation.ExtendedGraphemeClusterLiteralType](intenturlrepresentation/extendedgraphemeclusterliteraltype.md)
  A type that represents an extended grapheme cluster literal.
- [IntentURLRepresentation.StringLiteralType](intenturlrepresentation/stringliteraltype.md)
  A type that represents a string literal.
- [IntentURLRepresentation.UnicodeScalarLiteralType](intenturlrepresentation/unicodescalarliteraltype.md)
  A type that represents a Unicode scalar literal.
### Default Implementations
- [ExpressibleByExtendedGraphemeClusterLiteral Implementations](intenturlrepresentation/expressiblebyextendedgraphemeclusterliteral-implementations.md)
- [ExpressibleByStringInterpolation Implementations](intenturlrepresentation/expressiblebystringinterpolation-implementations.md)
- [ExpressibleByStringLiteral Implementations](intenturlrepresentation/expressiblebystringliteral-implementations.md)

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intenturlrepresentation)*