# UIFocusAnimationContext

**Framework**: UIKit  
**Kind**: protocol

Information about focusing animations being performed by the system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
protocol UIFocusAnimationContext : NSObjectProtocol
```

#### Overview

You don’t adopt this protocol in your custom classes. When a focus update occurs and the system provides you with a [`UIFocusAnimationCoordinator`](uifocusanimationcoordinator.md) object, you can use that object to specify custom focus-related animations. When the time comes for the system to execute your animations, it delivers an object that adopts this protocol to your animation block. The context object contains information about the system animations that you can use to configure the behavior of your own animations. For example, you might configure your animations to be exactly half the duration of the system animations.

## Topics

### Getting the animation attributes
- [var duration: TimeInterval](uifocusanimationcontext/duration.md)
  The duration (measured in seconds) of the focus animation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [func addCoordinatedFocusingAnimations(((any UIFocusAnimationContext) -> Void)?, completion: (() -> Void)?)](uifocusanimationcoordinator/addcoordinatedfocusinganimations(_:completion:).md)
  Runs the specified set of animations together with the system animations for adding focus to an item.
- [func addCoordinatedUnfocusingAnimations(((any UIFocusAnimationContext) -> Void)?, completion: (() -> Void)?)](uifocusanimationcoordinator/addcoordinatedunfocusinganimations(_:completion:).md)
  Runs the specified set of animations together with the system animations for removing focus from an item.
- [func addCoordinatedAnimations((() -> Void)?, completion: (() -> Void)?)](uifocusanimationcoordinator/addcoordinatedanimations(_:completion:).md)
  Specifies the animations to coordinate with the active focus animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifocusanimationcontext)*