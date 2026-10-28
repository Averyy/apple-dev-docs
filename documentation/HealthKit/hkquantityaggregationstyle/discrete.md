# discrete

**Framework**: HealthKit  
**Kind**: property  
**Role**: Type Property

Discrete samples may be averaged over time.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0 (renamed: HKQuantityAggregationStyle.discreteArithmetic)
- iPadOS 8.0+ - Deprecated in 13.0 (renamed: HKQuantityAggregationStyle.discreteArithmetic)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: HKQuantityAggregationStyle.discreteArithmetic)
- macOS 13.0+
- visionOS 1.0+ - Deprecated in 1.0 (renamed: HKQuantityAggregationStyle.discreteArithmetic)
- watchOS 2.0+ - Deprecated in 6.0 (renamed: HKQuantityAggregationStyle.discreteArithmetic)

> **Deprecated**: Use [`HKQuantityAggregationStyle.discreteArithmetic`](./discretearithmetic.md) instead.

## Declaration

```swift
static var discrete: HKQuantityAggregationStyle { get }
```

```c
HKQuantityAggregationStyleDiscrete
```

## Discussion

You typically use discrete types to monitor the change in the value over time. For example, body mass, heart rate, temperature, and respiratory rate are all discrete quantity types. You can also query for the minimum or maximum value in a given time period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle/discrete)*