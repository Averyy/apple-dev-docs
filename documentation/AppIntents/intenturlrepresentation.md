# IntentURLRepresentation

**Framework**: App Intents  
**Kind**: struct

The URL representation of an app intent.

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
struct IntentURLRepresentation<Intent> where Intent : AppIntent
```

#### Overview

Note that you need to use a universal link for your URL representation, you can’t use a custom URL scheme. For more information about universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

## Topics

### Initializers
- [init(String)](intenturlrepresentation/init(_:).md)

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)

## See Also

- [protocol URLRepresentableIntent](urlrepresentableintent.md)
  An app intent with a URL representation.
- [protocol CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intenturlrepresentation)*