# UndoManager.CheckpointMessage

**Framework**: Foundation  
**Kind**: struct

A message that an undo manager sends at certain checkpoints.

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
struct CheckpointMessage
```

#### Overview

The undo manager posts this message when it opens or closes an undo group (except when it opens a top-level group) and when it checks the redo stack.

Observe this message type with the identifier [`checkpoint`](notificationcenter/messageidentifier/checkpoint.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](notificationcenter/mainactormessage/subject.md) of this message type is [`UndoManager`](undomanager.md).

This message interoperates with the notification [`NSUndoManagerCheckpoint`](nsnotification/name-swift.struct/nsundomanagercheckpoint.md). The system notifies observers of the message when the [`NotificationCenter`](notificationcenter.md) posts the notification and vice versa.

## Topics

### Initializers
- [init()](undomanager/checkpointmessage/init.md)
  Creates a undo manager checkpoint message.

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
- [UndoManager.WillRedoChangeMessage](undomanager/willredochangemessage.md)
  A message that an undo manager sends before redoing a change.
- [UndoManager.DidRedoChangeMessage](undomanager/didredochangemessage.md)
  A message that an undo manager sends after redoing a change.
- [UndoManager.DidOpenUndoGroupMessage](undomanager/didopenundogroupmessage.md)
  A message that an undo manager sends after opening an undo group.
- [UndoManager.WillCloseUndoGroupMessage](undomanager/willcloseundogroupmessage.md)
  A message that an undo manager sends before closing an undo group.
- [UndoManager.DidCloseUndoGroupMessage](undomanager/didcloseundogroupmessage.md)
  A message that an undo manager sends after closing an undo group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/checkpointmessage)*