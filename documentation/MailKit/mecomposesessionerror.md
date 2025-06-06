# MEComposeSessionError

**Framework**: MailKit  
**Kind**: struct

An error that indicates the compose session is in an erroneous state.

**Availability**:
- macOS 12.0+

## Declaration

```swift
struct MEComposeSessionError
```

## Topics

### Indicating Erroneous States
- [static var invalidBody: MEComposeSessionError.Code](mecomposesessionerror/invalidbody.md)
  An error that indicates the message’s body is invalid.
- [static var invalidHeaders: MEComposeSessionError.Code](mecomposesessionerror/invalidheaders.md)
  An error that indicates one or more of the message’s headers are invalid.
- [static var invalidRecipients: MEComposeSessionError.Code](mecomposesessionerror/invalidrecipients.md)
  An error that indicates one or more of the message’s recipients are invalid.
- [let MEComposeSessionErrorDomain: String](mecomposesessionerrordomain.md)
  A constant for the compose session error domain.
### Type Properties
- [static var errorDomain: String](mecomposesessionerror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class MEComposeSession](mecomposesession.md)
  An object that represents a single mail compose window.
- [func mailComposeSessionDidBegin(MEComposeSession)](mecomposesessionhandler/mailcomposesessiondidbegin(_:).md)
  Informs the handler when the user opens a compose window.
- [func mailComposeSessionDidEnd(MEComposeSession)](mecomposesessionhandler/mailcomposesessiondidend(_:).md)
  Informs the handler when the user closes a compose window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesessionerror)*