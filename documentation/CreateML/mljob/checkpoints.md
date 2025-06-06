# checkpoints

**Framework**: Create ML  
**Kind**: property

A publisher that sends a checkpoint for each of the session’s checkpoint intervals.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
final var checkpoints: AnyPublisher<MLCheckpoint, Never> { get }
```

## See Also

- [var result: AnyPublisher<Result, any Error>](mljob/result.md)
  A publisher that provides a result when the training session has finished.
- [var phase: AnyPublisher<MLPhase, Never>](mljob/phase.md)
  Phase publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mljob/checkpoints)*