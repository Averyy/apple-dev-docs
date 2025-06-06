# BEDragInteractionDelegate

**Framework**: BrowserEngineKit  
**Kind**: protocol

A protocol to which the drag interaction delegates conform.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
protocol BEDragInteractionDelegate : UIDragInteractionDelegate
```

#### Overview

Use [`BEDragInteraction`](bedraginteraction.md) and its delegate to asynchronously prepare drag interactions and add items to drag sessions, for example when supporting drag interaction requires Javascript execution. If you don’t need to asynchronously interact with drag interactions, use [`UIDragInteraction`](https://developer.apple.com/documentation/UIKit/UIDragInteraction) instead.

## Topics

### Participating in drag gestures
- [func dragInteraction(BEDragInteraction, prepare: any UIDragSession, completion: () -> Bool)](bedraginteractiondelegate/draginteraction(_:prepare:completion:).md)
  Called when the drag interaction has begun, to allow the delegate to prepare for the drag session before the system requests drag items through `-dragInteraction:itemsForBeginningSession:`.
- [func dragInteraction(BEDragInteraction, itemsForAddingTo: any UIDragSession, forTouchAt: CGPoint, completion: ([UIDragItem]) -> Bool)](bedraginteractiondelegate/draginteraction(_:itemsforaddingto:fortouchat:completion:).md)
  The asynchronous counterpart to `-dragInteraction:itemsForAddingToSession:withTouchAtPoint:` to allow touches on this view to add items to an existing drag session. Please refer to the aforementioned delegate method for its full documentation.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIDragInteractionDelegate](../UIKit/UIDragInteractionDelegate.md)

## See Also

- [class BEDragInteraction](bedraginteraction.md)
  A `UIDragInteraction` subclass with features specific to browsers to enable asynchronous preparations and behaviours.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteractiondelegate)*