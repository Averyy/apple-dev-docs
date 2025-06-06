# phase

**Framework**: Create ML  
**Kind**: property

Phase publisher.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
final var phase: AnyPublisher<MLPhase, Never> { get }
```

## See Also

- [var checkpoints: AnyPublisher<MLCheckpoint, Never>](mljob/checkpoints.md)
  A publisher that sends a checkpoint for each of the session’s checkpoint intervals.
- [var result: AnyPublisher<Result, any Error>](mljob/result.md)
  A publisher that provides a result when the training session has finished.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mljob/phase)*