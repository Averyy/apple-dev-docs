# allAsleepValues

**Framework**: HealthKit  
**Kind**: property

A set of values that represents the possible stages of sleep.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
static var allAsleepValues: Set<HKCategoryValueSleepAnalysis> { get }
```

#### Discussion

This value includes [`asleep`](hkcategoryvaluesleepanalysis/asleep.md), [`HKCategoryValueSleepAnalysis.asleepCore`](hkcategoryvaluesleepanalysis/asleepcore.md), [`HKCategoryValueSleepAnalysis.asleepDeep`](hkcategoryvaluesleepanalysis/asleepdeep.md), [`HKCategoryValueSleepAnalysis.asleepREM`](hkcategoryvaluesleepanalysis/asleeprem.md), and [`HKCategoryValueSleepAnalysis.asleepUnspecified`](hkcategoryvaluesleepanalysis/asleepunspecified.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcategoryvaluesleepanalysis/allasleepvalues)*