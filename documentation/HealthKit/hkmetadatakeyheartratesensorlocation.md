# HKMetadataKeyHeartRateSensorLocation

**Framework**: HealthKit  
**Kind**: var

The location where a specific heart rate reading was taken.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HKMetadataKeyHeartRateSensorLocation: String
```

#### Discussion

This key takes an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) containing an [`HKHeartRateSensorLocation`](hkheartratesensorlocation.md) as its value.

## Topics

### Valid Locations
- [enum HKHeartRateSensorLocation](hkheartratesensorlocation.md)
  Constants that indicate where on the body the heart rate sensor is located.

## See Also

- [let HKMetadataKeyHeartRateMotionContext: String](hkmetadatakeyheartratemotioncontext.md)
  The user’s activity level when the heart rate sample was measured.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkmetadatakeyheartratesensorlocation)*