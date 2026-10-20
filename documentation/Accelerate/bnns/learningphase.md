# BNNS.LearningPhase

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the learning phase of a normalization operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
@frozen
enum LearningPhase
```

## Topics

### Learning Phases
- [BNNS.LearningPhase.inference](./learningphase/inference.md)
  The layer apply context is inference.
- [BNNS.LearningPhase.training](./learningphase/training.md)
  The layer apply context is training.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/learningphase)*