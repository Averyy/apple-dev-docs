# HKMetadataKeyHeartRateMotionContext

**Framework**: HealthKit  
**Kind**: var

The user’s activity level when the heart rate sample was measured.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let HKMetadataKeyHeartRateMotionContext: String
```

#### Discussion

This key takes an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) containing an [`HKHeartRateMotionContext`](hkheartratemotioncontext.md) as its value.

## Topics

### Valid Motion Contexts
- [enum HKHeartRateMotionContext](hkheartratemotioncontext.md)
  Values that indicate the user’s level of activity when the heart rate sample was measured.

## See Also

- [static let heartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartrate.md)
  A quantity sample type that measures the user’s heart rate.
- [let HKMetadataKeyHeartRateSensorLocation: String](hkmetadatakeyheartratesensorlocation.md)
  The location where a specific heart rate reading was taken.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyheartratemotioncontext)*