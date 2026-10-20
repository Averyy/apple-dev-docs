# countryCode

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The abbreviated country or region name.

**Availability**:
- iOS 3.0+ - Deprecated in 26.0
- iPadOS 3.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.9+ - Deprecated in 26.0
- tvOS 9.2+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 2.0+ - Deprecated in 26.0

> **Deprecated**: Use MKMapItem's location, address and addressRepresentations properties instead. Use MKAddressRepresentations for formatted address strings for MapKit provided MKMapItems

## Declaration

```swift
var countryCode: String? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSString * countryCode;
```

#### Discussion

This string is the standard abbreviation used to refer to the country or region. For example, if the placemark location was Apple’s headquarters, the value for this property would be the string “US”.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkplacemark/countrycode)*