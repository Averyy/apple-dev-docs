# init(checkpoint:)

**Framework**: Create ML  
**Kind**: init

Creates a random forest regressor  from a checkpoint.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(checkpoint: MLCheckpoint) throws
```

#### Discussion

> **Note**: `MLCreateError` if the checkpoint can’t be loaded.

## Parameters

- `checkpoint`: Training checkpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor/init(checkpoint:))*