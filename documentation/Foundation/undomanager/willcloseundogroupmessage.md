# UndoManager.WillCloseUndoGroupMessage

**Framework**: Foundation  
**Kind**: struct  
**Role**: Structure

A message that an undo manager sends before closing an undo group.

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
struct WillCloseUndoGroupMessage
```

## Overview

The undo manager posts this message after you call [`endUndoGrouping()`](./endundogrouping%28%29.md). Because this is a “will”-style message, the undo manager sends the message before it closes the undo group.

Observe this message with the identifier [`willCloseUndoGroup`](../notificationcenter/messageidentifier/willcloseundogroup.md), or specify its type directly to the `addObserver(of:for:using:)` method. The [`Subject`](../notificationcenter/mainactormessage/subject.md) of this message type is [`UndoManager`](../undomanager.md).

This message interoperates with the notification [`NSUndoManagerWillCloseUndoGroup`](../nsnotification/name-swift.struct/nsundomanagerwillcloseundogroup.md). The system notifies observers of the message when the [`NotificationCenter`](../notificationcenter.md) posts the notification. Similarly, the system notifies observers of the notification when it posts the message.

## Topics

### Initializers
- [init()](./willcloseundogroupmessage/init%28%29.md)
  Creates a will close undo group message.

## Relationships

### Conforms To
- [NotificationCenter.MainActorMessage](../notificationcenter/mainactormessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Working with notification messages
- [UndoManager.WillUndoChangeMessage](./willundochangemessage.md)
  A message that an undo manager sends before undoing a change.
- [UndoManager.DidUndoChangeMessage](./didundochangemessage.md)
  A message that an undo manager sends after undoing a change.
- [UndoManager.WillRedoChangeMessage](./willredochangemessage.md)
  A message that an undo manager sends before redoing a change.
- [UndoManager.DidRedoChangeMessage](./didredochangemessage.md)
  A message that an undo manager sends after redoing a change.
- [UndoManager.CheckpointMessage](./checkpointmessage.md)
  A message that an undo manager sends at certain checkpoints.
- [UndoManager.DidOpenUndoGroupMessage](./didopenundogroupmessage.md)
  A message that an undo manager sends after opening an undo group.
- [UndoManager.DidCloseUndoGroupMessage](./didcloseundogroupmessage.md)
  A message that an undo manager sends after closing an undo group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/undomanager/willcloseundogroupmessage)*