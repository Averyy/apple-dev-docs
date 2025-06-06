# UIPointerInteractionAnimating

**Framework**: UIKit  
**Kind**: protocol

An interface for modifying an interaction animation in coordination with the pointer effect animations.

**Availability**:
- iOS 13.4+
- iPadOS 13.4+
- Mac Catalyst 13.4+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIPointerInteractionAnimating : NSObjectProtocol
```

## Topics

### Managing animations
- [func addAnimations(() -> Void)](uipointerinteractionanimating/addanimations(_:).md)
  Adds the specified animation block to the animator.
- [func addCompletion((Bool) -> Void)](uipointerinteractionanimating/addcompletion(_:).md)
  Adds the specified completion block to the animator.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteractionanimating)*