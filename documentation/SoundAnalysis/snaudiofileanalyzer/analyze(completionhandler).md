# analyze(completionHandler:)

**Framework**: Sound Analysis  
**Kind**: method  
**Role**: Instance Method

Analyzes the audio file asynchronously.

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
func analyze(completionHandler: @escaping @Sendable (Bool) -> Void)
```

```swift
func analyze() async -> Bool
```

```objc
- (void) analyzeWithCompletionHandler:(void (^)(BOOL didReachEndOfFile)) completionHandler;
```

## Mentions

- [Classifying Sounds in an Audio File](../classifying-sounds-in-an-audio-file.md)

## Discussion

The method executes asynchronously and calls the completion handler after the analyzer finishes analyzing the entire file. The audio file analyzer sends errors to each request’s results observer.

If you call the [`cancelAnalysis()`](./cancelanalysis%28%29.md) method, the analyzer calls your completion handler and passes `false` because it can’t reach the end of the file.

## Parameters

- `completionHandler`: A completion closure (Swift) or block (Objective-C) the analyzer calls when it finishes analyzing a file.

## See Also

### Analyzing Data
- [func analyze()](./analyze%28%29.md)
  Analyzes the audio file synchronously.
- [func cancelAnalysis()](./cancelanalysis%28%29.md)
  Cancels all the asynchronous sound analysis requests the analyzer is currently processing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer/analyze(completionhandler:))*