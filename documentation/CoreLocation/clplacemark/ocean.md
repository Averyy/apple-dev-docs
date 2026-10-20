# ocean

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The name of the ocean associated with the placemark.

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
var ocean: String? { get }
```

```objc
@property (nonatomic, copy, readonly, nullable) NSString * ocean;
```

#### Discussion

For coordinates that lie over an ocean, this property contains the name of the ocean.

## See Also

### Getting landscape information
- [var inlandWater: String?](./inlandwater.md)
  The name of the inland water body associated with the placemark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark/ocean)*