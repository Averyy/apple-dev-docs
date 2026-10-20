# HKWorkoutActivityType.other

**Framework**: HealthKit  
**Kind**: case  
**Role**: Case

The constant for a workout that does not match any of the other workout activity types.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case other
```

```c
HKWorkoutActivityTypeOther
```

#### Discussion

If your app uses the [`HKWorkoutActivityType.swimming`](./swimming.md) or [`HKWorkoutActivityType.other`](./other.md) activity type, you must explain how your app calculates workout data when sensor information is not available. For more information, see the [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/watchos/interaction/workout/).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkworkoutactivitytype/other)*