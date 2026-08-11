# EnumURLRepresentation

**Framework**: App Intents  
**Kind**: struct

The type that provides the URL for an app enum.

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
struct EnumURLRepresentation<Enum> where Enum : AppEnum
```

#### Overview

If you adopt the [`URLRepresentableEnum`](urlrepresentableenum.md) protocol in an app enum, use this type to build the URL for your type. Construct the type as a Swift string that contains characters suitable for use in a URL. To adjust the URL dynamically for your content, include a reference to your app enum value as part of the content. The following example shows an app enum type that includes the enum’s current value in the final URL:

```swift
enum Destination: String, AppEnum, URLRepresentableEnum {
   case root
   case locationServices

   static var urlRepresentation = URLRepresentation("https://example.com/root=\(.rawValue)")
}
```

If you need to differentiate URLs by more than the enum’s current value, provide an array of values for your representation instead. The following example shows the same enum from the previous example, but with distinct strings for each case.

```swift
enum Destination: String, AppEnum, URLRepresentableEnum {
   case root
   case locationServices

   static var urlRepresentation = URLRepresentation([
      .root: "https://example.com/link1=\(.root)",
      .locationServices: "https://example.com/link2=\(.locationServices)"
   ])
}
```

Make sure you define your app enum type using a URL-friendly value. The system automatically converts values of type [`String`](https://developer.apple.com/documentation/Swift/String), [`Int`](https://developer.apple.com/documentation/Swift/Int), and [`URL`](https://developer.apple.com/documentation/Foundation/URL) to values suitable for inclusion in a URL.

## Topics

### Structures
- [EnumURLRepresentation.EnumSingleURLRepresentation](enumurlrepresentation/enumsingleurlrepresentation.md)
### Initializers
- [init([Enum : EnumURLRepresentation<Enum>.EnumSingleURLRepresentation])](enumurlrepresentation/init(_:)-1odm.md)
  Creates a URL representation for an app enum using the provided dictionary.
- [init(String)](enumurlrepresentation/init(_:)-6p999.md)
  Creates a URL representation for an app enum using the provided Swift string.

## Relationships

### Conforms To
- [ExpressibleByExtendedGraphemeClusterLiteral](../Swift/ExpressibleByExtendedGraphemeClusterLiteral.md)
- [ExpressibleByStringInterpolation](../Swift/ExpressibleByStringInterpolation.md)
- [ExpressibleByStringLiteral](../Swift/ExpressibleByStringLiteral.md)
- [ExpressibleByUnicodeScalarLiteral](../Swift/ExpressibleByUnicodeScalarLiteral.md)

## See Also

- [protocol URLRepresentableEnum](urlrepresentableenum.md)
  An interface you apply to an app enum type so the system can handle it like a universal link.
- [protocol CustomURLRepresentationParameterConvertible](customurlrepresentationparameterconvertible.md)
  An interface that allows a type to express its contents in a URL representation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/enumurlrepresentation)*