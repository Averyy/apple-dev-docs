# didMoveToWritableLocationOldURLKey

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

The key in a `UIDocumentDidMoveToWritableLocationNotification`’s `userInfo` dictionary that contains the previous readonly file URL.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
class let didMoveToWritableLocationOldURLKey: String
```

```c
extern NSString * const UIDocumentDidMoveToWritableLocationOldURLKey;
```

## See Also

### Notifications
- [class let stateChangedNotification: NSNotification.Name](./statechangednotification.md)
  A notification the document object posts when there’s a change in the state of the document.
- [UIDocument.StateChangedMessage](./statechangedmessage.md)
- [class let didMoveToWritableLocationNotification: NSNotification.Name](./didmovetowritablelocationnotification.md)
  A notification that the document posts when copying the file from a readonly location in order to write changes. This notification will be posted on the file presenter queue.
- [UIDocument.DidMoveToWritableLocationMessage](./didmovetowritablelocationmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/didmovetowritablelocationoldurlkey)*