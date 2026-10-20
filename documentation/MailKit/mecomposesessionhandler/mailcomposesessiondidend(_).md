# mailComposeSessionDidEnd(_:)

**Framework**: MailKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Informs the handler when the user closes a compose window.

**Availability**:
- macOS 12.0+

## Declaration

```swift
func mailComposeSessionDidEnd(_ session: MEComposeSession)
```

```objc
- (void) mailComposeSessionDidEnd:(MEComposeSession *) session;
```

## Parameters

- `session`: The compose session that corresponds to the message the user is composing.

## See Also

### Handling Compose Sessions
- [class MEComposeSession](../mecomposesession.md)
  An object that represents a single mail compose window.
- [func mailComposeSessionDidBegin(MEComposeSession)](./mailcomposesessiondidbegin%28_%29.md)
  Informs the handler when the user opens a compose window.
- [struct MEComposeSessionError](../mecomposesessionerror.md)
  An error that indicates the compose session is in an erroneous state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mailkit/mecomposesessionhandler/mailcomposesessiondidend(_:))*