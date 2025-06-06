# MTLCounterResultTimestamp

**Framework**: Metal  
**Kind**: struct

The data structure for storing the data you resolve from a timestamp counter set.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct MTLCounterResultTimestamp
```

## Mentions

- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Overview

For steps that explain how to resolve data from a counter set, such as [`timestamp`](mtlcounterresulttimestamp/timestamp.md), see [`Converting a GPU’s Counter Data into a Readable Format`](converting-a-gpus-counter-data-into-a-readable-format.md).

## Topics

### Timestamp Values
- [var timestamp: UInt64](mtlcounterresulttimestamp/timestamp.md)
  A timestamp value from a GPU at a particular point in time during an operation, typically at the beginning or ending of a render stage.
### Swift Support
- [init()](mtlcounterresulttimestamp/init.md)
  Creates a default timestamp result.
- [init(timestamp: UInt64)](mtlcounterresulttimestamp/init(timestamp:).md)
  Creates a timestamp result from a value.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [Converting a GPU’s Counter Data into a Readable Format](converting-a-gpus-counter-data-into-a-readable-format.md)
  Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.
- [struct MTLCounterResultStatistic](mtlcounterresultstatistic.md)
  The data structure for storing the data you resolve from a statistic counter set.
- [struct MTLCounterResultStageUtilization](mtlcounterresultstageutilization.md)
  The data structure for storing the data you resolve from a stage-utilization counter set.
- [var MTLCounterErrorValue: UInt64](mtlcountererrorvalue.md)
  A sentinel value for an entry in a counter sample buffer that indicates the entry’s data is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcounterresulttimestamp)*