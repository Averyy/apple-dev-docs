# moveToJunk

**Framework**: MailKit  
**Kind**: property  
**Role**: Type Property

An object that moves the message to the account’s Junk mailbox.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class var moveToJunk: MEMessageAction { get }
```

```objc
@property (class, readonly) MEMessageAction * moveToJunkAction;
```

## See Also

### Transferring Messages
- [class var moveToArchive: MEMessageAction](./movetoarchive.md)
  An object that moves the message to the account’s Archive mailbox.
- [class var moveToTrash: MEMessageAction](./movetotrash.md)
  An object that moves the message to the account’s Trash mailbox.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageaction/movetojunk)*