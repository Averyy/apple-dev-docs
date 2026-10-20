# phase

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The training session’s current state.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
final var phase: MLPhase { get }
```

## See Also

### Checking a training session’s progress
- [enum MLPhase](../mlphase.md)
  The possible states of a training session.
- [var iteration: Int](./iteration.md)
  The iteration number of a training session’s phase.
- [var checkpoints: [MLCheckpoint]](./checkpoints.md)
  An array of checkpoints the training session has created so far.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltrainingsession/phase)*