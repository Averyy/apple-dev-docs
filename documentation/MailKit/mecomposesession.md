# MEComposeSession

**Framework**: MailKit  
**Kind**: class

An object that represents a single mail compose window.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class MEComposeSession
```

## Topics

### Managing Compose Sessions
- [var sessionID: UUID](mecomposesession/sessionid.md)
  A unique identifier for the session.
- [func reload()](mecomposesession/reload.md)
  Refreshes the compose session with the extension’s new information.
### Accessing Message Properties
- [var mailMessage: MEMessage](mecomposesession/mailmessage.md)
  The properties of the mail message, such as the subject and recipients.
### Instance Properties
- [var composeContext: MEComposeContext](mecomposesession/composecontext.md)

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

- [func mailComposeSessionDidBegin(MEComposeSession)](mecomposesessionhandler/mailcomposesessiondidbegin(_:).md)
  Informs the handler when the user opens a compose window.
- [func mailComposeSessionDidEnd(MEComposeSession)](mecomposesessionhandler/mailcomposesessiondidend(_:).md)
  Informs the handler when the user closes a compose window.
- [struct MEComposeSessionError](mecomposesessionerror.md)
  An error that indicates the compose session is in an erroneous state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesession)*