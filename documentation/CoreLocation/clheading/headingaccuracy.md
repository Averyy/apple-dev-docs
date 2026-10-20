# headingAccuracy

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The maximum deviation (measured in degrees) between the reported heading and the true geomagnetic heading.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- watchOS 2.0+

## Declaration

```swift
var headingAccuracy: CLLocationDirection { get }
```

```objc
@property (nonatomic, readonly) CLLocationDirection headingAccuracy;
```

#### Discussion

A positive value in this property represents the potential error between the value reported by the [`magneticHeading`](./magneticheading.md) property and the actual direction of magnetic north. Thus, the lower the value of this property, the more accurate the heading. A negative value means that the reported heading is invalid, which can occur when the device is uncalibrated or there is strong interference from local magnetic fields.

## See Also

### Getting the heading values
- [var magneticHeading: CLLocationDirection](./magneticheading.md)
  The heading (measured in degrees) relative to magnetic north.
- [var trueHeading: CLLocationDirection](./trueheading.md)
  The heading (measured in degrees) relative to true north.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clheading/headingaccuracy)*