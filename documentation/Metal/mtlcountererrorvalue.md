# MTLCounterErrorValue

**Framework**: Metal  
**Kind**: var

A sentinel value for an entry in a counter sample buffer that indicates the entry’s data is invalid.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var MTLCounterErrorValue: UInt64 { get }
```

## Mentions

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)

#### Discussion

A GPU driver typically sets entries to this value when it encounters an error resolving a counter’s data. The driver also uses this value for counters it doesn’t support within a counter set (see [`Confirming which counters and counter sets a GPU supports`](confirming-which-counters-and-counter-sets-a-gpu-supports.md)).

## See Also

- [Converting a GPU’s counter data into a readable format](converting-a-gpus-counter-data-into-a-readable-format.md)
  Inspect and use the data within a GPU’s counter sample buffer by resolving it into a standard format.
- [struct MTLCounterResultTimestamp](mtlcounterresulttimestamp.md)
  The data structure for storing the data you resolve from a timestamp counter set.
- [struct MTLCounterResultStatistic](mtlcounterresultstatistic.md)
  The data structure for storing the data you resolve from a statistic counter set.
- [struct MTLCounterResultStageUtilization](mtlcounterresultstageutilization.md)
  The data structure for storing the data you resolve from a stage-utilization counter set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcountererrorvalue)*