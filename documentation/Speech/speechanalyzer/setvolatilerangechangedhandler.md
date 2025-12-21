# setVolatileRangeChangedHandler(_:)

**Framework**: Speech  
**Kind**: method

A closure that the analyzer calls when the volatile range changes.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final func setVolatileRangeChangedHandler(_ handler: sending ((CMTimeRange, Bool, Bool) -> Void)?)
```

#### Discussion

You can use this handler to manage audio input resources and monitor progress.

You can also use this handler to respond to result finalization, but the better tool for that job is the [`resultsFinalizationTime`](speechmoduleresult/resultsfinalizationtime.md) property of a module’s results. When the analyzer calls this handler, the application may not have consumed the result from the stream yet; this handler may be called with a new volatile range while there are still results prior to the new volatile range waiting to be consumed.

This closure replaces any handler you specified when creating the analyzer.

## Parameters

- `handler`: A closure called to report the analysis’ progress. The closure takes the following parameters:

## See Also

- [var volatileRange: CMTimeRange?](speechanalyzer/volatilerange.md)
  The range of results that can change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/setvolatilerangechangedhandler(_:))*