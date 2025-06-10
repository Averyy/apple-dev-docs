# MSCriticalMessagingError

**Framework**: Messages  
**Kind**: enum

Values that describe errors the Critical Messaging API returns.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
enum MSCriticalMessagingError
```

## Topics

### Error codes
- [MSCriticalMessagingError.unknown](mscriticalmessagingerror/unknown.md)
  The error code the framework returns after an unknown error occurs.
- [MSCriticalMessagingError.invalidAuthenticationRequest](mscriticalmessagingerror/invalidauthenticationrequest.md)
  The authentication request isn’t valid.
- [MSCriticalMessagingError.notSupported](mscriticalmessagingerror/notsupported.md)
  The framework doesn’t support the current device.
- [MSCriticalMessagingError.notAuthorized](mscriticalmessagingerror/notauthorized.md)
  The operation isn’t authorized.
- [MSCriticalMessagingError.sendFailed](mscriticalmessagingerror/sendfailed.md)
  The message failed to send.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let MSStickersErrorDomain: String](msstickerserrordomain.md)
  The error domain for stickers.
- [let MSMessagesErrorDomain: String](msmessageserrordomain.md)
  The error domain for iMessage apps.
- [enum MSMessageErrorCode](msmessageerrorcode.md)
  The error codes that the Messages framework generates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mscriticalmessagingerror)*