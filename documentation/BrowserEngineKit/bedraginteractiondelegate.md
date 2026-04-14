# BEDragInteractionDelegate

**Framework**: BrowserEngineKit  
**Kind**: protocol

A protocol for a drag interaction delegate.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
protocol BEDragInteractionDelegate : UIDragInteractionDelegate
```

#### Overview

The [`BEDragInteraction`](bedraginteraction.md) class’s [`delegate`](bedraginteraction/delegate.md) implements this protocol. Use [`BEDragInteraction`](bedraginteraction.md) to prepare drag interactions asynchronously and add items to drag sessions, for example, when drag support requires JavaScript.

## Topics

### Participating in drag gestures
- [func dragInteraction(BEDragInteraction, prepare: any UIDragSession, completion: () -> Bool)](bedraginteractiondelegate/draginteraction(_:prepare:completion:).md)
  Prepares the delegate for a drag session.
- [func dragInteraction(BEDragInteraction, itemsForAddingTo: any UIDragSession, forTouchAt: CGPoint, completion: ([UIDragItem]) -> Bool)](bedraginteractiondelegate/draginteraction(_:itemsforaddingto:fortouchat:completion:).md)
  Requests items to add to a drag session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIDragInteractionDelegate](../UIKit/UIDragInteractionDelegate.md)

## See Also

- [class BEDragInteraction](bedraginteraction.md)
  An interaction that enables your app to asynchronously provide drag items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteractiondelegate)*