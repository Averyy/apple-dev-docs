# volatileRange

**Framework**: Speech  
**Kind**: property

The range of results that can change.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final var volatileRange: CMTimeRange? { get }
```

#### Discussion

This property conveys the “finalized” idea. Results within the volatile range may be replaced by updated results, but results that lie outside the volatile range will not be replaced. The application can safely consolidate results that lay outside the range.

The volatile range includes pending analyses—audio that has been sent out but where no results have come back yet. If there aren’t any pending results and the modules aren’t supplying volatile results—if all the previously-sent results are final—the volatile range is empty.

- `volatileRange.start` is the start of the non-final results and the start of the input that is subject to ongoing analysis
- `volatileRange.end` is the extent of the input that is subject to ongoing analysis after being dequeued from the input sequence

A module is not required to provide new, final results for audio ranges that were previously volatile but otherwise unchanged by finalization. However, you can create two modules—one that provides both volatile and final results, and a second that only provides final results—and process results from the latter differently.

The volatile range is `nil` if no input has been received.

## See Also

- [func setVolatileRangeChangedHandler(sending ((CMTimeRange, Bool, Bool) -> Void)?)](speechanalyzer/setvolatilerangechangedhandler(_:).md)
  A closure that the analyzer calls when the volatile range changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/volatilerange)*