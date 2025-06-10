# HKQuantityAggregationStyle

**Framework**: HealthKit  
**Kind**: enum

Constant values that describe how quantities can be aggregated over time.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum HKQuantityAggregationStyle
```

#### Overview

A quantity type’s aggregation style determines the type of statistics queries that you can perform. Discrete types support average, minimum, and maximum queries. Cumulative types support only sum queries. For more information, see [`HKStatisticsQuery`](hkstatisticsquery.md).

## Topics

### Aggregation Styles
- [HKQuantityAggregationStyle.cumulative](hkquantityaggregationstyle/cumulative.md)
  Cumulative samples that can be summed over time.
- [HKQuantityAggregationStyle.discreteArithmetic](hkquantityaggregationstyle/discretearithmetic.md)
  Discrete samples that can be averaged over time using an arithmetic mean.
- [HKQuantityAggregationStyle.discreteTemporallyWeighted](hkquantityaggregationstyle/discretetemporallyweighted.md)
  Discrete samples that can be averaged over a time interval using a temporally weighted integration function.
- [HKQuantityAggregationStyle.discreteEquivalentContinuousLevel](hkquantityaggregationstyle/discreteequivalentcontinuouslevel.md)
  Discrete samples that can be combined over a time interval by computing the equivalent continuous sound level.
### Deprecated Styles
- [static var discrete: HKQuantityAggregationStyle](hkquantityaggregationstyle/discrete.md)
  Discrete samples may be averaged over time.
### Initializers
- [init?(rawValue: Int)](hkquantityaggregationstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var aggregationStyle: HKQuantityAggregationStyle](hkquantitytype/aggregationstyle.md)
  The aggregation style for the given quantity type.
- [func `is`(compatibleWith: HKUnit) -> Bool](hkquantitytype/is(compatiblewith:).md)
  Returns a Boolean value that indicates whether the quantity type is compatible with the given unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle)*