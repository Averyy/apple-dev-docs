# Results

**Framework**: Speech  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
associatedtype Results : Sendable, AsyncSequence where Self.Results.Failure == any Error
```

## See Also

### Getting results
- [var results: Self.Results](./results-swift.property.md)
  An asynchronous sequence containing this module’s analysis results. Results are added to the sequence as they are created.
- [associatedtype Result : SpeechModuleResult, Sendable](./result.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmodule/results-swift.associatedtype)*