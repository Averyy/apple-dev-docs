# MSCriticalMessagingError.notAuthorized

**Framework**: Messages  
**Kind**: case

The operation isn’t authorized.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
case notAuthorized
```

#### Discussion

The requested operation isn’t authorized; use [`requestAuthorization(for:)`](mscriticalsmsmessenger/requestauthorization(for:).md) to request someone’s authorization to be able to send background messages from this app.

## See Also

- [MSCriticalMessagingError.unknown](mscriticalmessagingerror/unknown.md)
  The error code the framework returns after an unknown error occurs.
- [MSCriticalMessagingError.invalidAuthenticationRequest](mscriticalmessagingerror/invalidauthenticationrequest.md)
  The authentication request isn’t valid.
- [MSCriticalMessagingError.notSupported](mscriticalmessagingerror/notsupported.md)
  The framework doesn’t support the current device.
- [MSCriticalMessagingError.sendFailed](mscriticalmessagingerror/sendfailed.md)
  The message failed to send.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mscriticalmessagingerror/notauthorized)*