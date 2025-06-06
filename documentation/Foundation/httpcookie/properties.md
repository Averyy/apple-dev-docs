# properties

**Framework**: Foundation  
**Kind**: property

The cookie’s properties.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var properties: [HTTPCookiePropertyKey : Any]? { get }
```

#### Discussion

This dictionary can be used with [`init(properties:)`](httpcookie/init(properties:).md) (or [`cookieWithProperties:`](nshttpcookie/cookiewithproperties:.md) in Objective-C) to create an equivalent [`HTTPCookie`](httpcookie.md) object.

See [`init(properties:)`](httpcookie/init(properties:).md) for more information on the constraints imposed on the `properties` dictionary.

## See Also

- [struct HTTPCookiePropertyKey](httpcookiepropertykey.md)
  Constants that define the supported keys in a cookie attributes dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/httpcookie/properties)*