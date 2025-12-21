# EnumURLRepresentation

**Framework**: App Intents  
**Kind**: struct

The URL representation of an app enum.

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
struct EnumURLRepresentation<Enum> where Enum : AppEnum
```

#### Overview

Note that you need to use a universal link for your URL representation, you can’t use a custom URL scheme. For more information about universal links, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/Xcode/allowing-apps-and-websites-to-link-to-your-content).

## Topics

### Structures
- [EnumURLRepresentation.EnumSingleURLRepresentation](enumurlrepresentation/enumsingleurlrepresentation.md)
### Initializers
- [init([Enum : EnumURLRepresentation<Enum>.EnumSingleURLRepresentation])](enumurlrepresentation/init(_:)-1odm.md)
- [init(String)](enumurlrepresentation/init(_:)-6p999.md)

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/enumurlrepresentation)*