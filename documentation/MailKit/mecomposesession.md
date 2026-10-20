# MEComposeSession

**Framework**: MailKit  
**Kind**: class  
**Role**: Class

An object that represents a single mail compose window.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEComposeSession
```

```objc
@interface MEComposeSession : NSObject
```

## Topics

### Managing Compose Sessions
- [var sessionID: UUID](./mecomposesession/sessionid.md)
  A unique identifier for the session.
- [func reload()](./mecomposesession/reload%28%29.md)
  Refreshes the compose session with the extension’s new information.
### Accessing Message Properties
- [var mailMessage: MEMessage](./mecomposesession/mailmessage.md)
  The properties of the mail message, such as the subject and recipients.
### Instance Properties
- [var composeContext: MEComposeContext](./mecomposesession/composecontext.md)
### Initializers
- [init?(coder: NSCoder)](./mecomposesession/init%28coder%29.md)

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

### Handling Compose Sessions
- [func mailComposeSessionDidBegin(MEComposeSession)](./mecomposesessionhandler/mailcomposesessiondidbegin%28_%29.md)
  Informs the handler when the user opens a compose window.
- [func mailComposeSessionDidEnd(MEComposeSession)](./mecomposesessionhandler/mailcomposesessiondidend%28_%29.md)
  Informs the handler when the user closes a compose window.
- [struct MEComposeSessionError](./mecomposesessionerror.md)
  An error that indicates the compose session is in an erroneous state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesession)*