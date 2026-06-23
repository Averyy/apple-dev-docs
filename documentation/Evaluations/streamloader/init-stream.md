# init(stream:)

**Framework**: Evaluations  
**Kind**: init

Creates a loader backed by the given async sequence.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(stream: some Sendable & AsyncSequence<Sample, any Error>)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/evaluations/streamloader/init(stream:))*