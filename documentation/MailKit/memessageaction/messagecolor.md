# MEMessageAction.MessageColor

**Framework**: MailKit  
**Kind**: enum

A color that the system uses to display a message in the message list.

**Availability**:
- macOS 12.0+

## Declaration

```swift
enum MessageColor
```

## Topics

### Specifying a Message Color
- [MEMessageAction.MessageColor.green](memessageaction/messagecolor/green.md)
  Sets the color of the message to green.
- [MEMessageAction.MessageColor.yellow](memessageaction/messagecolor/yellow.md)
  Sets the color of the message to yellow.
- [MEMessageAction.MessageColor.orange](memessageaction/messagecolor/orange.md)
  Sets the color of the message to orange.
- [MEMessageAction.MessageColor.red](memessageaction/messagecolor/red.md)
  Sets the color of the message to red.
- [MEMessageAction.MessageColor.purple](memessageaction/messagecolor/purple.md)
  Sets the color of the message to purple.
- [MEMessageAction.MessageColor.blue](memessageaction/messagecolor/blue.md)
  Sets the color of the message to blue.
- [MEMessageAction.MessageColor.gray](memessageaction/messagecolor/gray.md)
  Sets the color of the message to gray.
- [MEMessageAction.MessageColor.none](memessageaction/messagecolor/none.md)
  Clears the color of the message.
### Initializers
- [init?(rawValue: Int)](memessageaction/messagecolor/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func decideAction(for: MEMessage, completionHandler: (MEMessageActionDecision?) -> Void)](memessageactionhandler/decideaction(for:completionhandler:).md)
  Determines the action that the system takes when it downloads a message.
- [class MEMessageAction](memessageaction.md)
  An action the system performs on a message, such as setting a color or archiving it.
- [class MEMessageActionDecision](memessageactiondecision.md)
  The action that the system performs on a message, or a request to ask the action handler again later when the message content is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageaction/messagecolor)*