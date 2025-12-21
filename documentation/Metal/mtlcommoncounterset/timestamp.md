# timestamp

**Framework**: Metal  
**Kind**: property

The common name for the counter set that contains the timestamp counter.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
static let timestamp: MTLCommonCounterSet
```

## Mentions

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Discussion

The [`timestamp`](mtlcommoncounterset/timestamp.md) counter set contains the [`timestamp`](mtlcommoncounter/timestamp.md) counter. Use this name to check whether a GPU device supports the corresponding counter set (see [`Confirming which counters and counter sets a GPU supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md)).

## See Also

- [static let stageUtilization: MTLCommonCounterSet](mtlcommoncounterset/stageutilization.md)
  The common name for the counter set that contains hardware utilization measurements from various render stages.
- [static let statistic: MTLCommonCounterSet](mtlcommoncounterset/statistic.md)
  The common name for the counter set that contains GPU workload statistics.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcommoncounterset/timestamp)*