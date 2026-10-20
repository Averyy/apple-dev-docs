# moveToArchive

**Framework**: MailKit  
**Kind**: property  
**Role**: Type Property

An object that moves the message to the account’s Archive mailbox.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class var moveToArchive: MEMessageAction { get }
```

```objc
@property (class, readonly) MEMessageAction * moveToArchiveAction;
```

## See Also

### Transferring Messages
- [class var moveToJunk: MEMessageAction](./movetojunk.md)
  An object that moves the message to the account’s Junk mailbox.
- [class var moveToTrash: MEMessageAction](./movetotrash.md)
  An object that moves the message to the account’s Trash mailbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageaction/movetoarchive)*