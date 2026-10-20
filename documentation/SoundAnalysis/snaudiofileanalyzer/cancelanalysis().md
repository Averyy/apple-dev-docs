# cancelAnalysis()

**Framework**: Sound Analysis  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) cancelAnalysis;
```

#### Discussion

The method executes asynchronously, and when it completes, the analyzer calls the completion handler you provide to the [`analyze(completionHandler:)`](./analyze%28completionhandler%29.md) method.

## See Also

### Analyzing Data
- [func analyze()](./analyze%28%29.md)
  Analyzes the audio file synchronously.
- [func analyze(completionHandler: (Bool) -> Void)](./analyze%28completionhandler%29.md)
  Analyzes the audio file asynchronously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snaudiofileanalyzer/cancelanalysis())*