# HKCategoryValueSleepAnalysis.asleepCore

**Framework**: HealthKit  
**Kind**: case

The user is in light or intermediate sleep.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
case asleepCore
```

#### Discussion

This value corresponds to stage N2 of the American Academy of Sleep Medicine’s scoring model. Stage N2 is also referred to as light or intermediate sleep. It accounts for a major part of the time spent asleep. The [`HKCategoryValueSleepAnalysis.asleepCore`](hkcategoryvaluesleepanalysis/asleepcore.md) value also includes stage N1, which makes up only a small portion of the night.

## See Also

- [HKCategoryValueSleepAnalysis.awake](hkcategoryvaluesleepanalysis/awake.md)
  The user is awake.
- [HKCategoryValueSleepAnalysis.asleepDeep](hkcategoryvaluesleepanalysis/asleepdeep.md)
  The user is in deep sleep.
- [HKCategoryValueSleepAnalysis.asleepREM](hkcategoryvaluesleepanalysis/asleeprem.md)
  The user is in REM sleep.
- [HKCategoryValueSleepAnalysis.asleepUnspecified](hkcategoryvaluesleepanalysis/asleepunspecified.md)
  The user is asleep, but the specific stage isn’t known.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis/asleepcore)*