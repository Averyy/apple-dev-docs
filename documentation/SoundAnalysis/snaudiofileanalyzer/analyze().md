# analyze()

**Framework**: Sound Analysis  
**Kind**: method  
**Role**: Instance Method

Analyzes the audio file synchronously.

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
func analyze()
```

```objc
- (void) analyze;
```

## Mentions

- [Classifying Sounds in an Audio File](../classifying-sounds-in-an-audio-file.md)

## Discussion

This method executes synchronously and may block the calling thread for a long time.

> ❗ **Important**:  Keep your app’s user interface responsive by calling this method from a thread other than the main thread.

The audio file analyzer sends errors to each request’s results observer.

## See Also

### Analyzing Data
- [func analyze(completionHandler: (Bool) -> Void)](./analyze%28completionhandler%29.md)
  Analyzes the audio file asynchronously.
- [func cancelAnalysis()](./cancelanalysis%28%29.md)
  Cancels all the asynchronous sound analysis requests the analyzer is currently processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer/analyze())*