# mailComposeSessionDidBegin(_:)

**Framework**: MailKit  
**Kind**: method  
**Required**: Yes

Informs the handler when the user opens a compose window.

**Availability**:
- macOS 12.0+

## Declaration

```swift
@MainActor
func mailComposeSessionDidBegin(_ session: MEComposeSession)
```

## Parameters

- `session`: The compose session that corresponds to the message the user is composing.

## See Also

- [class MEComposeSession](mecomposesession.md)
  An object that represents a single mail compose window.
- [func mailComposeSessionDidEnd(MEComposeSession)](mecomposesessionhandler/mailcomposesessiondidend(_:).md)
  Informs the handler when the user closes a compose window.
- [struct MEComposeSessionError](mecomposesessionerror.md)
  An error that indicates the compose session is in an erroneous state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesessionhandler/mailcomposesessiondidbegin(_:))*