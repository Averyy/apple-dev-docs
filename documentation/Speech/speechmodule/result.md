# Result

**Framework**: Speech  
**Kind**: associatedtype  
**Required**: Yes

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
associatedtype Result : SpeechModuleResult, Sendable where Self.Result == Self.Results.Element
```

## See Also

- [var results: Self.Results](speechmodule/results-swift.property.md)
  An asynchronous sequence containing this module’s analysis results. Results are added to the sequence as they are created.
- [associatedtype Results : Sendable, AsyncSequence](speechmodule/results-swift.associatedtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmodule/result)*