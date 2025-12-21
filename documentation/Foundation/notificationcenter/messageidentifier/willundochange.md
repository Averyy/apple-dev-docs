# willUndoChange

**Framework**: Foundation  
**Kind**: property

An identifier for the undo manager will undo change message.

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
  An identifier for the undo manager did undo change message.
- [static var willRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.WillRedoChangeMessage>](notificationcenter/messageidentifier/willredochange.md)
  An identifier for the undo manager will redo change message.
- [static var didRedoChange: NotificationCenter.BaseMessageIdentifier<UndoManager.DidRedoChangeMessage>](notificationcenter/messageidentifier/didredochange.md)
  An identifier for the undo manager did redo change message.
- [static var checkpoint: NotificationCenter.BaseMessageIdentifier<UndoManager.CheckpointMessage>](notificationcenter/messageidentifier/checkpoint.md)
  An identifier for the undo manager checkpoint message.
- [static var didOpenUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidOpenUndoGroupMessage>](notificationcenter/messageidentifier/didopenundogroup.md)
  An identifier for the undo manager did open undo group message.
- [static var willCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.WillCloseUndoGroupMessage>](notificationcenter/messageidentifier/willcloseundogroup.md)
  An identifier for the undo manager will close undo group message.
- [static var didCloseUndoGroup: NotificationCenter.BaseMessageIdentifier<UndoManager.DidCloseUndoGroupMessage>](notificationcenter/messageidentifier/didcloseundogroup.md)
  An identifier for the undo manager did close undo group message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/notificationcenter/messageidentifier/willundochange)*