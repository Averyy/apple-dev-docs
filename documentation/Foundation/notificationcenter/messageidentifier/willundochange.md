# willUndoChange

**Framework**: Foundation  
**Kind**: property

An identifier for a message about an undo manager preparing to perform an undo.

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
static var willUndoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillUndoChangeMessage> { get }
```

#### Discussion

Use this identifier with [`NotificationCenter`](notificationcenter.md)’s `addObserver(of:for:using:)` or `messages(of:for:bufferSize:)` methods to observe messages of type [`UndoManager.WillUndoChangeMessage`](undomanager/willundochangemessage.md).

## See Also

- [static var didUndoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidUndoChangeMessage>](notificationcenter/messageidentifier/didundochange.md)
  An identifier for a message about an undo manager having performed an undo.
- [static var willRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillRedoChangeMessage>](notificationcenter/messageidentifier/willredochange.md)
  An identifier for a message about an undo manager preparing to perform a redo.
- [static var didRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidRedoChangeMessage>](notificationcenter/messageidentifier/didredochange.md)
  An identifier for a message about an undo manager having performed a redo.
- [static var checkpoint: NotificationCenter.BaseMessageIdentifier<UndoManager.CheckpointMessage>](notificationcenter/messageidentifier/checkpoint.md)
  An identifier for a message about an undo manager reaching a checkpoint.
- [static var didOpenUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidOpenUndoGroupMessage>](notificationcenter/messageidentifier/didopenundogroup.md)
  An identifier for a message about an undo manager having opened an undo group.
- [static var willCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.WillCloseUndoGroupMessage>](notificationcenter/messageidentifier/willcloseundogroup.md)
  An identifier for a message about an undo manager preparing to close an undo group.
- [static var didCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidCloseUndoGroupMessage>](notificationcenter/messageidentifier/didcloseundogroup.md)
  An identifier for a message about an undo manager having closed an undo group.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/willundochange)*