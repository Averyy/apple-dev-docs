# MEMessageActionDecision

**Framework**: MailKit  
**Kind**: class

The action that the system performs on a message, or a request to ask the action handler again later when the message content is available.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEMessageActionDecision
```

## Topics

### Determining Actions to Perform on Messages
- [class var invokeAgainWithBody: MEMessageActionDecision](memessageactiondecision/invokeagainwithbody.md)
  An object that indicates the handler needs the message content before it can decide what action to take on a message.
### Type Methods
- [class func action(MEMessageAction) -> Self](memessageactiondecision/action(_:).md)
- [class func actions([MEMessageAction]) -> Self](memessageactiondecision/actions(_:).md)
### Initializers
- [init?(coder: NSCoder)](memessageactiondecision/init(coder:).md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [func decideAction(for: MEMessage, completionHandler: (MEMessageActionDecision?) -> Void)](memessageactionhandler/decideaction(for:completionhandler:).md)
  Determines the action that the system takes when it downloads a message.
- [class MEMessageAction](memessageaction.md)
  An action the system performs on a message, such as setting a color or archiving it.
- [MEMessageAction.MessageColor](memessageaction/messagecolor.md)
  A color that the system uses to display a message in the message list.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/memessageactiondecision)*