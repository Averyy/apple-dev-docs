# HKQuantityAggregationStyle

**Framework**: HealthKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum HKQuantityAggregationStyle : NSInteger;
```

## Overview

A quantity type’s aggregation style determines the type of statistics queries that you can perform. Discrete types support average, minimum, and maximum queries. Cumulative types support only sum queries. For more information, see [`HKStatisticsQuery`](./hkstatisticsquery.md).

## Topics

### Aggregation Styles
- [HKQuantityAggregationStyle.cumulative](./hkquantityaggregationstyle/cumulative.md)
  Cumulative samples that can be summed over time.
- [HKQuantityAggregationStyle.discreteArithmetic](./hkquantityaggregationstyle/discretearithmetic.md)
  Discrete samples that can be averaged over time using an arithmetic mean.
- [HKQuantityAggregationStyle.discreteTemporallyWeighted](./hkquantityaggregationstyle/discretetemporallyweighted.md)
  Discrete samples that can be averaged over a time interval using a temporally weighted integration function.
- [HKQuantityAggregationStyle.discreteEquivalentContinuousLevel](./hkquantityaggregationstyle/discreteequivalentcontinuouslevel.md)
  Discrete samples that can be combined over a time interval by computing the equivalent continuous sound level.
### Deprecated Styles
- [static var discrete: HKQuantityAggregationStyle](./hkquantityaggregationstyle/discrete.md)
  Discrete samples may be averaged over time.
### Initializers
- [init?(rawValue: Int)](./hkquantityaggregationstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing Quantity Type Data
- [var aggregationStyle: HKQuantityAggregationStyle](./hkquantitytype/aggregationstyle.md)
  The aggregation style for the given quantity type.
- [func `is`(compatibleWith: HKUnit) -> Bool](./hkquantitytype/is%28compatiblewith%29.md)
  Returns a Boolean value that indicates whether the quantity type is compatible with the given unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquantityaggregationstyle)*