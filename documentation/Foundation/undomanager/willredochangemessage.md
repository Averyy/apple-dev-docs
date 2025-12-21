# UndoManager.WillRedoChangeMessage

**Framework**: Foundation  
**Kind**: struct

A message that an undo manager sends before redoing a change.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct WillRedoChangeMessage
```

#### Overview

The undo manager posts this message after you call [`redo()`](undomanager/redo().md). Because this is a “will”-style message, the undo manager sends the message before it performs the redo.

Observe this message with the identifier [`willRedoChange`](notificationcenter/messageidentifier/willredochange.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`UndoManager`](undomanager.md).

This message interoperates with the notification [`NSUndoManagerWillRedoChange`](nsnotification/name-swift.struct/nsundomanagerwillredochange.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification and vice versa.

## Topics

### Initializers
- [init()](undomanager/willredochangemessage/init.md)
  Creates a will redo change message.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](notificationcenter/mainactormessage.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UndoManager.WillUndoChangeMessage](undomanager/willundochangemessage.md)
  A message that an undo manager sends before undoing a change.
- [UndoManager.DidUndoChangeMessage](undomanager/didundochangemessage.md)
  A message that an undo manager sends after undoing a change.
- [UndoManager.DidRedoChangeMessage](undomanager/didredochangemessage.md)
  A message that an undo manager sends after redoing a change.
- [UndoManager.CheckpointMessage](undomanager/checkpointmessage.md)
  A message that an undo manager sends at certain checkpoints.
- [UndoManager.DidOpenUndoGroupMessage](undomanager/didopenundogroupmessage.md)
  A message that an undo manager sends after opening an undo group.
- [UndoManager.WillCloseUndoGroupMessage](undomanager/willcloseundogroupmessage.md)
  A message that an undo manager sends before closing an undo group.
- [UndoManager.DidCloseUndoGroupMessage](undomanager/didcloseundogroupmessage.md)
  A message that an undo manager sends after closing an undo group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/willredochangemessage)*