# country

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The name of the country or region associated with the placemark.

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
var country: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * country;
```

## Discussion

If the placemark location is Apple’s headquarters, for example, the value for this property would be the string “United States”.

## See Also

### Getting the placemark’s country
- [var isoCountryCode: String?](./isocountrycode.md)
  The abbreviated country or region name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/country)*