# MTLCommonCounterSet

**Framework**: Metal  
**Kind**: struct

The name of a specific counter set that a GPU device can support.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLCommonCounterSet
```

## Mentions

- [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)

#### Overview

This type defines the constants that let a GPU device declare which counter sets it supports.

> ❗ **Important**:  Some GPUs may only support some of the counters within a counter set.

For more information, see [`Confirming which counters and counter sets a GPU supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md).

## Topics

### Common counter set names
- [static let timestamp: MTLCommonCounterSet](mtlcommoncounterset/timestamp.md)
  The common name for the counter set that contains the timestamp counter.
- [static let stageUtilization: MTLCommonCounterSet](mtlcommoncounterset/stageutilization.md)
  The common name for the counter set that contains hardware utilization measurements from various render stages.
- [static let statistic: MTLCommonCounterSet](mtlcommoncounterset/statistic.md)
  The common name for the counter set that contains GPU workload statistics.
### Swift support
- [init(rawValue: String)](mtlcommoncounterset/init(rawvalue:).md)
  Creates a common counter set name from a raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Confirming which counters and counter sets a GPU supports](confirming-which-counters-and-counter-sets-a-gpu-supports.md)
  Check whether a GPU produces the runtime performance data you want to sample.
- [protocol MTLCounterSet](mtlcounterset.md)
  A collection of individual counters a GPU device supports for a counter set.
- [protocol MTLCounter](mtlcounter.md)
  An individual counter a GPU device lists within one of its counter sets.
- [struct MTLCommonCounter](mtlcommoncounter.md)
  The name of a specific counter that can appear in a GPU device’s counter sets.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommoncounterset)*