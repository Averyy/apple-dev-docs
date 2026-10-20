# altitude

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The absolute altitude of the device relative to sea level, measured in meters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var altitude: Double { get }
```

```objc
@property (nonatomic, readonly) double altitude;
```

#### Discussion

This value can be positive or negative.

## See Also

### Accessing Altitude Data
- [var accuracy: Double](./accuracy.md)
  The estimated uncertainty of the altimeter in meters, based on one standard deviation.
- [var precision: Double](./precision.md)
  The recommended resolution for the altitude, in meters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmabsolutealtitudedata/altitude)*