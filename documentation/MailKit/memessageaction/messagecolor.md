# MEMessageAction.MessageColor

**Framework**: MailKit  
**Kind**: enum  
**Role**: Enumeration

A color that the system uses to display a message in the message list.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum MessageColor
```

```c
enum MEMessageActionMessageColor : NSInteger;
```

## Topics

### Specifying a Message Color
- [MEMessageAction.MessageColor.green](./messagecolor/green.md)
  Sets the color of the message to green.
- [MEMessageAction.MessageColor.yellow](./messagecolor/yellow.md)
  Sets the color of the message to yellow.
- [MEMessageAction.MessageColor.orange](./messagecolor/orange.md)
  Sets the color of the message to orange.
- [MEMessageAction.MessageColor.red](./messagecolor/red.md)
  Sets the color of the message to red.
- [MEMessageAction.MessageColor.purple](./messagecolor/purple.md)
  Sets the color of the message to purple.
- [MEMessageAction.MessageColor.blue](./messagecolor/blue.md)
  Sets the color of the message to blue.
- [MEMessageAction.MessageColor.gray](./messagecolor/gray.md)
  Sets the color of the message to gray.
- [MEMessageAction.MessageColor.none](./messagecolor/none.md)
  Clears the color of the message.
### Initializers
- [init?(rawValue: Int)](./messagecolor/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Performing Actions on Messages
- [func decideAction(for: MEMessage, completionHandler: (MEMessageActionDecision?) -> Void)](../memessageactionhandler/decideaction%28for,completionhandler%29.md)
  Determines the action that the system takes when it downloads a message.
- [class MEMessageAction](../memessageaction.md)
  An action the system performs on a message, such as setting a color or archiving it.
- [class MEMessageActionDecision](../memessageactiondecision.md)
  The action that the system performs on a message, or a request to ask the action handler again later when the message content is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageaction/messagecolor)*