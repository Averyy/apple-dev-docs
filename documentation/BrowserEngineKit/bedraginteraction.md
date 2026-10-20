# BEDragInteraction

**Framework**: BrowserEngineKit  
**Kind**: class  
**Role**: Class

An interaction that enables your app to asynchronously provide drag items.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
class BEDragInteraction
```

```objc
@interface BEDragInteraction : UIDragInteraction
```

#### Overview

This class is a subclass of [`UIDragInteraction`](../UIKit/uidraginteraction.md) that adds asynchronous support for drag interaction. If you don’t need to interact with drag operations asynchronously, use [`UIDragInteraction`](../UIKit/uidraginteraction.md) instead.

To support UI element drag interaction in your browser app asynchronously, create an instance of this class and attach it to the source view.

Set the isntance’s [`delegate`](./bedraginteraction/delegate.md) to an object that conforms to [`BEDragInteractionDelegate`](./bedraginteractiondelegate.md), and implement prepartions in the delegate for the [`UIDragSession`](../UIKit/uidragsession.md). The system requests drag items from your delegate by calling the delegate’s [`dragInteraction(_:itemsForBeginning:)`](../UIKit/uidraginteractiondelegate/draginteraction%28_,itemsforbeginning%29.md) method.

## Topics

### Creating a drag interaction
- [init(delegate: any BEDragInteractionDelegate)](./bedraginteraction/init%28delegate%29.md)
  Creates a drag interaction and assigns its delegate.
### Handling drag gestures
- [var delegate: (any BEDragInteractionDelegate)?](./bedraginteraction/delegate.md)
  A delegate for a drag interaction.
- [protocol BEDragInteractionDelegate](./bedraginteractiondelegate.md)
  A protocol for a drag interaction delegate.

## Relationships

### Inherits From
- [UIDragInteraction](../UIKit/uidraginteraction.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIInteraction](../UIKit/uiinteraction.md)

## See Also

### Drag interaction
- [protocol BEDragInteractionDelegate](./bedraginteractiondelegate.md)
  A protocol for a drag interaction delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteraction)*