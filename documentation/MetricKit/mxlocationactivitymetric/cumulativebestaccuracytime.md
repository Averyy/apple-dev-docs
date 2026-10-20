# cumulativeBestAccuracyTime

**Framework**: MetricKit  
**Kind**: property  
**Role**: Instance Property

The total time spent tracking the current location at the best accuracy.

**Availability**:
- iOS 13.0+ - Deprecated in 27.2
- iPadOS 13.0+ - Deprecated in 27.2
- Mac Catalyst 13.1+ - Deprecated in 27.0
- macOS 10.15+ - Deprecated in 27.2
- visionOS 1.0+ - Deprecated in 27.2

> **Deprecated**: Use [`bestAccuracy`](../locationactivitytimemetric/bestaccuracy.md) instead.

## Declaration

```swift
var cumulativeBestAccuracyTime: Measurement<UnitDuration> { get }
```

```objc
@property (strong, readonly, nonnull) NSMeasurement<NSUnitDuration *> * cumulativeBestAccuracyTime;
```

## See Also

### Reading location services use
- [var cumulativeBestAccuracyForNavigationTime: Measurement<UnitDuration>](./cumulativebestaccuracyfornavigationtime.md)
  The total time spent tracking the current location at the best accuracy for navigation.
- [var cumulativeNearestTenMetersAccuracyTime: Measurement<UnitDuration>](./cumulativenearesttenmetersaccuracytime.md)
  The total time spent tracking the current location to an accuracy of 10 meters.
- [var cumulativeHundredMetersAccuracyTime: Measurement<UnitDuration>](./cumulativehundredmetersaccuracytime.md)
  The total time spent tracking the current location to an accuracy of 100 meters.
- [var cumulativeKilometerAccuracyTime: Measurement<UnitDuration>](./cumulativekilometeraccuracytime.md)
  The total time spent tracking the current location to an accuracy of 1 kilometer.
- [var cumulativeThreeKilometersAccuracyTime: Measurement<UnitDuration>](./cumulativethreekilometersaccuracytime.md)
  The total time spent tracking the current location to an accuracy of 3 kilometers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metrickit/mxlocationactivitymetric/cumulativebestaccuracytime)*