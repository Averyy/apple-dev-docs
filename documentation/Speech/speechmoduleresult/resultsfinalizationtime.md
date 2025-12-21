# resultsFinalizationTime

**Framework**: Speech  
**Kind**: property  
**Required**: Yes

The audio input time up to which results from this module have been finalized (after this result). The module’s results are final up to but not including this time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var resultsFinalizationTime: CMTime { get }
```

#### Discussion

This value is mostly equivalent to the start of [`volatileRange`](speechanalyzer/volatilerange.md) after the time at which this result was published. The module publishing this result will publish no futher results with a [`range`](speechmoduleresult/range.md) that encompasses a time predating this time. The module may publish results for a range that includes this time.

The client can draw the following conclusions from this value and `range` (or refer to the [`isFinal`](speechmoduleresult/isfinal.md) property):

- If `resultsFinalizationTime >= range.end` then this result is final. Additionally, all previously-provided results with a `range` predating `resultsFinalizationTime` are also final.
- If `resultsFinalizationTime < range.end` (or `resultsFinalizationTime <= range.start`) then this result is volatile and may or may not be replaced by a result provided later.

A module is not required to provide new, final results for audio ranges that it finalizes through if the previously-volatile result was unchanged by finalization. If needed, however, a client can create two modules—one that provides both volatile and final results, and a second that only provides final results—and process results from the latter differently.

This value is not  equivalent to the start of the volatile range. The [`volatileRange`](speechanalyzer/volatilerange.md) property combines all modules’ volatile ranges together; this property only refers to the finalization status of results from the module delivering this result.

## See Also

- [var isFinal: Bool](speechmoduleresult/isfinal.md)
  Whether this result is final at the time it is produced.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmoduleresult/resultsfinalizationtime)*