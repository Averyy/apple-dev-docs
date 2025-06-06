# cancelAnalysis()

**Framework**: Sound Analysis  
**Kind**: method

Cancels all the asynchronous sound analysis requests the analyzer is currently processing.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func cancelAnalysis()
```

#### Discussion

The method executes asynchronously, and when it completes, the analyzer calls the completion handler you provide to the [`analyze(completionHandler:)`](snaudiofileanalyzer/analyze(completionhandler:).md) method.

## See Also

- [func analyze()](snaudiofileanalyzer/analyze.md)
  Analyzes the audio file synchronously.
- [func analyze(completionHandler: (Bool) -> Void)](snaudiofileanalyzer/analyze(completionhandler:).md)
  Analyzes the audio file asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer/cancelanalysis())*