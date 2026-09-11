# stream

**Framework**: Evaluations  
**Kind**: property

The async sequence that forwards each sample from the underlying async sequence during an evaluation run.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+
- Xcode 27.0+

## Declaration

```swift
var stream: any AsyncSequence<Sample, any Error> { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/streamloader/stream)*