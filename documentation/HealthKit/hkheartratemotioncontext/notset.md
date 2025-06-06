# HKHeartRateMotionContext.notSet

**Framework**: HealthKit  
**Kind**: case

A value indicating that the user’s activity level could not be determined.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
case notSet
```

#### Discussion

This value is identical to the sample’s metadata not containing a [`HKMetadataKeyHeartRateMotionContext`](hkmetadatakeyheartratemotioncontext.md) key.

## See Also

- [HKHeartRateMotionContext.active](hkheartratemotioncontext/active.md)
  A value indicating that the user was in motion during the heart rate sample.
- [HKHeartRateMotionContext.sedentary](hkheartratemotioncontext/sedentary.md)
  A value indicating that the user has been still for at least 5 minutes prior to the heart rate sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartratemotioncontext/notset)*