# results

**Framework**: Speech  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

An asynchronous sequence containing this module’s analysis results. Results are added to the sequence as they are created.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var results: Self.Results { get }
```

#### Discussion

Each module has its own result sequence and data structure.

If there is an error in the overall analysis, all modules will throw the error from their individual result sequence.

## See Also

### Getting results
- [associatedtype Result : SpeechModuleResult, Sendable](./result.md)
- [associatedtype Results : Sendable, AsyncSequence](./results-swift.associatedtype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechmodule/results-swift.property)*