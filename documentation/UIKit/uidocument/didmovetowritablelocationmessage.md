# UIDocument.DidMoveToWritableLocationMessage

**Framework**: UIKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
struct DidMoveToWritableLocationMessage
```

## Topics

### Initializers
- [init(document: UIDocument, oldURL: URL)](./didmovetowritablelocationmessage/init%28document,oldurl%29.md)
### Instance Properties
- [var document: UIDocument](./didmovetowritablelocationmessage/document.md)
- [var oldURL: URL](./didmovetowritablelocationmessage/oldurl.md)

## Relationships

### Conforms To
- [NotificationCenter.AsyncMessage](../../Foundation/notificationcenter/asyncmessage.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Notifications
- [class let stateChangedNotification: NSNotification.Name](./statechangednotification.md)
  A notification the document object posts when there’s a change in the state of the document.
- [UIDocument.StateChangedMessage](./statechangedmessage.md)
- [class let didMoveToWritableLocationNotification: NSNotification.Name](./didmovetowritablelocationnotification.md)
  A notification that the document posts when copying the file from a readonly location in order to write changes. This notification will be posted on the file presenter queue.
- [class let didMoveToWritableLocationOldURLKey: String](./didmovetowritablelocationoldurlkey.md)
  The key in a `UIDocumentDidMoveToWritableLocationNotification`’s `userInfo` dictionary that contains the previous readonly file URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/didmovetowritablelocationmessage)*