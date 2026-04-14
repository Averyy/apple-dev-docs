# BEDragInteraction

**Framework**: BrowserEngineKit  
**Kind**: class

An interaction that enables your app to asynchronously provide drag items.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
class BEDragInteraction
```

#### Overview

This class is a subclass of [`UIDragInteraction`](https://developer.apple.com/documentation/UIKit/UIDragInteraction) that adds asynchronous support for drag interaction. If you don’t need to interact with drag operations asynchronously, use [`UIDragInteraction`](https://developer.apple.com/documentation/UIKit/UIDragInteraction) instead.

To support UI element drag interaction in your browser app asynchronously, create an instance of this class and attach it to the source view.

Set the isntance’s [`delegate`](bedraginteraction/delegate.md) to an object that conforms to [`BEDragInteractionDelegate`](bedraginteractiondelegate.md), and implement prepartions in the delegate for the [`UIDragSession`](https://developer.apple.com/documentation/UIKit/UIDragSession). The system requests drag items from your delegate by calling the delegate’s [`dragInteraction(_:itemsForBeginning:)`](https://developer.apple.com/documentation/UIKit/UIDragInteractionDelegate/dragInteraction(_:itemsForBeginning:)) method.

## Topics

### Creating a drag interaction
- [init(delegate: any BEDragInteractionDelegate)](bedraginteraction/init(delegate:).md)
  Creates a drag interaction and assigns its delegate.
### Handling drag gestures
- [var delegate: (any BEDragInteractionDelegate)?](bedraginteraction/delegate.md)
  A delegate for a drag interaction.
- [protocol BEDragInteractionDelegate](bedraginteractiondelegate.md)
  A protocol for a drag interaction delegate.

## Relationships

### Inherits From
- [UIDragInteraction](../UIKit/UIDragInteraction.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIInteraction](../UIKit/UIInteraction.md)

## See Also

- [protocol BEDragInteractionDelegate](bedraginteractiondelegate.md)
  A protocol for a drag interaction delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteraction)*