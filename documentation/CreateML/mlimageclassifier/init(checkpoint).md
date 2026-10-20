# init(checkpoint:)

**Framework**: Create ML  
**Kind**: init

Creates an image classifier from a training session checkpoint.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(checkpoint: MLCheckpoint) throws
```

#### Discussion

You can only use a checkpoint from an image classifier’s training session if its [`phase`](mlcheckpoint/phase.md) property is [`MLPhase.training`](mlphase/training.md).

## Parameters

- `checkpoint`: A checkpoint from an image classifier training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/init(checkpoint:))*