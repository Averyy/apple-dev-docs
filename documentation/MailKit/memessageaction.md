# MEMessageAction

**Framework**: MailKit  
**Kind**: class

An action the system performs on a message, such as setting a color or archiving it.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEMessageAction
```

## Topics

### Changing the Read Status
- [class var markAsRead: MEMessageAction](memessageaction/markasread.md)
  An object that marks the message as read.
- [class var markAsUnread: MEMessageAction](memessageaction/markasunread.md)
  An object that marks the message as unread.
### Transferring Messages
- [class var moveToArchive: MEMessageAction](memessageaction/movetoarchive.md)
  An object that moves the message to the account’s Archive mailbox.
- [class var moveToJunk: MEMessageAction](memessageaction/movetojunk.md)
  An object that moves the message to the account’s Junk mailbox.
- [class var moveToTrash: MEMessageAction](memessageaction/movetotrash.md)
  An object that moves the message to the account’s Trash mailbox.
### Type Methods
- [class func flag(MEMessageAction.Flag) -> Self](memessageaction/flag(_:).md)
- [class func setBackgroundColor(MEMessageAction.MessageColor) -> Self](memessageaction/setbackgroundcolor(_:).md)
### Enumerations
- [MEMessageAction.Flag](memessageaction/flag.md)
- [MEMessageAction.MessageColor](memessageaction/messagecolor.md)
  A color that the system uses to display a message in the message list.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [func decideAction(for: MEMessage, completionHandler: (MEMessageActionDecision?) -> Void)](memessageactionhandler/decideaction(for:completionhandler:).md)
  Determines the action that the system takes when it downloads a message.
- [class MEMessageActionDecision](memessageactiondecision.md)
  The action that the system performs on a message, or a request to ask the action handler again later when the message content is available.
- [MEMessageAction.MessageColor](memessageaction/messagecolor.md)
  A color that the system uses to display a message in the message list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageaction)*