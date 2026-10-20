# UIPointerInteractionAnimating

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

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

```objc
@protocol UIPointerInteractionAnimating <NSObject>
```

## Topics

### Managing animations
- [func addAnimations(() -> Void)](./uipointerinteractionanimating/addanimations%28_%29.md)
  Adds the specified animation block to the animator.
- [func addCompletion((Bool) -> Void)](./uipointerinteractionanimating/addcompletion%28_%29.md)
  Adds the specified completion block to the animator.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerinteractionanimating)*