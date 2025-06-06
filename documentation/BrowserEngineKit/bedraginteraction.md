# BEDragInteraction

**Framework**: BrowserEngineKit  
**Kind**: class

A `UIDragInteraction` subclass with features specific to browsers to enable asynchronous preparations and behaviours.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
@MainActor
class BEDragInteraction
```

#### Overview

An interaction that enables your app to asynchronously provide drag items.

#### Overview

`BEDragInteraction` is a subclass of [`UIDragInteraction`](https://developer.apple.com/documentation/UIKit/UIDragInteraction) that additionally supports asynchronous interaction.

When a person drags a UI element in your browser app, create a `BEDragInteraction` and attach it to the source view. When you create the object, set its [`delegate`](bedraginteraction/delegate.md) to an object that conforms to [`BEDragInteractionDelegate`](bedraginteractiondelegate.md). Use the delegate to prepare the [`UIDragSession`](https://developer.apple.com/documentation/UIKit/UIDragSession) before the system requests drag items, which it does by calling the delegate’s [`dragInteraction(_:itemsForBeginning:)`](https://developer.apple.com/documentation/UIKit/UIDragInteractionDelegate/dragInteraction(_:itemsForBeginning:)) method.

## Topics

### Creating a drag interaction
- [init(delegate: any BEDragInteractionDelegate)](bedraginteraction/init(delegate:).md)
  Creates an drag interaction with the specified delegate.
### Handling drag gestures
- [var delegate: (any BEDragInteractionDelegate)?](bedraginteraction/delegate.md)
  The object that manages the drag interaction lifecycle.
- [protocol BEDragInteractionDelegate](bedraginteractiondelegate.md)
  A protocol to which the drag interaction delegates conform.

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
  A protocol to which the drag interaction delegates conform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/browserenginekit/bedraginteraction)*