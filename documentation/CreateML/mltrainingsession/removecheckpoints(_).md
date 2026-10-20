# removeCheckpoints(_:)

**Framework**: Create ML  
**Kind**: method

Removes the checkpoints that satisfy your closure from the training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
final func removeCheckpoints(_ predicate: (MLCheckpoint) -> Bool) throws
```

## Parameters

- `predicate`: A closure that returns a Boolean indicating whether to remove a checkpoint.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mltrainingsession/removecheckpoints(_:))*