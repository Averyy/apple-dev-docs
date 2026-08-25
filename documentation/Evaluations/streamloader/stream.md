# stream

**Framework**: Evaluations  
**Kind**: property

The async sequence that forwards each sample from the underlying async sequence during an evaluation run.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)
- Xcode 27.0+ (Beta)

## Declaration

```swift
var stream: any AsyncSequence<Sample, any Error> { get }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/streamloader/stream)*