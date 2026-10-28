# BEDragInteractionDelegate

**Framework**: BrowserEngineKit  
**Kind**: protocol  
**Role**: Protocol

A protocol for a drag interaction delegate.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
protocol BEDragInteractionDelegate : UIDragInteractionDelegate
```

```objc
@protocol BEDragInteractionDelegate <UIDragInteractionDelegate>
```

## Overview

The [`BEDragInteraction`](./bedraginteraction.md) class’s [`delegate`](./bedraginteraction/delegate.md) implements this protocol. Use [`BEDragInteraction`](./bedraginteraction.md) to prepare drag interactions asynchronously and add items to drag sessions, for example, when drag support requires JavaScript.

## Topics

### Participating in drag gestures
- [func dragInteraction(BEDragInteraction, prepare: any UIDragSession, completion: () -> Bool)](./bedraginteractiondelegate/draginteraction%28_,prepare,completion%29.md)
  Prepares the delegate for a drag session.
- [func dragInteraction(BEDragInteraction, itemsForAddingTo: any UIDragSession, forTouchAt: CGPoint, completion: ([UIDragItem]) -> Bool)](./bedraginteractiondelegate/draginteraction%28_,itemsforaddingto,fortouchat,completion%29.md)
  Requests items to add to a drag session.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIDragInteractionDelegate](../UIKit/uidraginteractiondelegate.md)

## See Also

### Drag interaction
- [class BEDragInteraction](./bedraginteraction.md)
  An interaction that enables your app to asynchronously provide drag items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteractiondelegate)*