# isoCountryCode

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The abbreviated country or region name.

**Availability**:
- iOS 5.0+ - Deprecated in 27.2
- iPadOS 5.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.8+ - Deprecated in 27.2
- tvOS 9.0+ - Deprecated in 27.0
- visionOS 1.0+ - Deprecated in 27.2
- watchOS 2.0+ - Deprecated in 27.2

> **Deprecated**: Use either GeoToolbox.PlaceDescriptor or MapKit

## Declaration

```swift
var isoCountryCode: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * ISOcountryCode;
```

#### Discussion

This string is the standard abbreviation used to refer to the country or region. For example, if the placemark location is Apple’s headquarters, the value for this property would be the string “US”.

## See Also

### Getting the placemark’s country
- [var country: String?](./country.md)
  The name of the country or region associated with the placemark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/isocountrycode)*