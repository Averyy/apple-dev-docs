# MEMessageActionDecision

**Framework**: MailKit  
**Kind**: class  
**Role**: Class

The action that the system performs on a message, or a request to ask the action handler again later when the message content is available.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEMessageActionDecision
```

```objc
@interface MEMessageActionDecision : NSObject
```

## Topics

### Determining Actions to Perform on Messages
- [class var invokeAgainWithBody: MEMessageActionDecision](./memessageactiondecision/invokeagainwithbody.md)
  An object that indicates the handler needs the message content before it can decide what action to take on a message.
### Type Methods
- [class func action(MEMessageAction) -> Self](./memessageactiondecision/action%28_%29.md)
- [class func actions([MEMessageAction]) -> Self](./memessageactiondecision/actions%28_%29.md)
### Initializers
- [init?(coder: NSCoder)](./memessageactiondecision/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Performing Actions on Messages
- [func decideAction(for: MEMessage, completionHandler: (MEMessageActionDecision?) -> Void)](./memessageactionhandler/decideaction%28for,completionhandler%29.md)
  Determines the action that the system takes when it downloads a message.
- [class MEMessageAction](./memessageaction.md)
  An action the system performs on a message, such as setting a color or archiving it.
- [MEMessageAction.MessageColor](./memessageaction/messagecolor.md)
  A color that the system uses to display a message in the message list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageactiondecision)*