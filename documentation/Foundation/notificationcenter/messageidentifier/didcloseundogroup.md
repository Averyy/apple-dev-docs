# didCloseUndoGroup

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An identifier for a message about an undo manager having closed an undo group.

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
static var didCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidCloseUndoGroupMessage> { get }
```

Available when `Self` is `NotificationCenter.BaseMessageIdentifier<UndoManager.DidCloseUndoGroupMessage>`.

## Discussion

Use this identifier with [`NotificationCenter`](../../notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`UndoManager.DidCloseUndoGroupMessage`](../../undomanager/didcloseundogroupmessage.md).

## See Also

### Identifying undo manager messages
- [static var willUndoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillUndoChangeMessage>](./willundochange.md)
  An identifier for a message about an undo manager preparing to perform an undo.
- [static var didUndoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidUndoChangeMessage>](./didundochange.md)
  An identifier for a message about an undo manager having performed an undo.
- [static var willRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillRedoChangeMessage>](./willredochange.md)
  An identifier for a message about an undo manager preparing to perform a redo.
- [static var didRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidRedoChangeMessage>](./didredochange.md)
  An identifier for a message about an undo manager having performed a redo.
- [static var checkpoint: NotificationCenter.BaseMessageIdentifier<UndoManager.CheckpointMessage>](./checkpoint.md)
  An identifier for a message about an undo manager reaching a checkpoint.
- [static var didOpenUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidOpenUndoGroupMessage>](./didopenundogroup.md)
  An identifier for a message about an undo manager having opened an undo group.
- [static var willCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.WillCloseUndoGroupMessage>](./willcloseundogroup.md)
  An identifier for a message about an undo manager preparing to close an undo group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/didcloseundogroup)*