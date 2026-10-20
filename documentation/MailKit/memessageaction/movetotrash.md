# moveToTrash

**Framework**: MailKit  
**Kind**: property  
**Role**: Type Property

An object that moves the message to the account’s Trash mailbox.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class var moveToTrash: MEMessageAction { get }
```

```objc
@property (class, readonly) MEMessageAction * moveToTrashAction;
```

## See Also

### Transferring Messages
- [class var moveToArchive: MEMessageAction](./movetoarchive.md)
  An object that moves the message to the account’s Archive mailbox.
- [class var moveToJunk: MEMessageAction](./movetojunk.md)
  An object that moves the message to the account’s Junk mailbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageaction/movetotrash)*