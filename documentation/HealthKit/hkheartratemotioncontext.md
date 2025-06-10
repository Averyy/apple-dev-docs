# HKHeartRateMotionContext

**Framework**: HealthKit  
**Kind**: enum

Values that indicate the user’s level of activity when the heart rate sample was measured.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
enum HKHeartRateMotionContext
```

## Topics

### Motion Contextes
- [HKHeartRateMotionContext.active](hkheartratemotioncontext/active.md)
  A value indicating that the user was in motion during the heart rate sample.
- [HKHeartRateMotionContext.notSet](hkheartratemotioncontext/notset.md)
  A value indicating that the user’s activity level could not be determined.
- [HKHeartRateMotionContext.sedentary](hkheartratemotioncontext/sedentary.md)
  A value indicating that the user has been still for at least 5 minutes prior to the heart rate sample.
### Initializers
- [init?(rawValue: Int)](hkheartratemotioncontext/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [static let heartRate: HKQuantityTypeIdentifier](hkquantitytypeidentifier/heartrate.md)
  A quantity sample type that measures the user’s heart rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkheartratemotioncontext)*