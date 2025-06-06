# MSCriticalMessagingError.sendFailed

**Framework**: Messages  
**Kind**: case

The message failed to send.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+

## Declaration

```swift
case sendFailed
```

## Mentions

- [Sending SMS messages from an app](critical-messaging-api.md)

#### Discussion

The framework isn’t able to send the message for one of the following reasons:

- An unreachable or incorrectly formatted phone number
- An unavailable cellular network
- The device’s SIM is in a disabled state

> **Note**: The phone number needs to conform to the [`ITU E.164 telephone numbering plan`](https://developer.apple.comhttps://www.itu.int/rec/T-REC-E.164-201011-I/en) standard, without any additional non-numeric characters such as dashes, periods, parentheses, or a plus character (+) that introduces a country code.

The phone number needs to conform to the [`ITU E.164 telephone numbering plan`](https://developer.apple.comhttps://www.itu.int/rec/T-REC-E.164-201011-I/en) standard, without any additional non-numeric characters such as dashes, periods, parentheses, or a plus character (+) that introduces a country code.

## See Also

- [MSCriticalMessagingError.unknown](mscriticalmessagingerror/unknown.md)
  The error code the framework returns after an unknown error occurs.
- [MSCriticalMessagingError.invalidAuthenticationRequest](mscriticalmessagingerror/invalidauthenticationrequest.md)
  The authentication request isn’t valid.
- [MSCriticalMessagingError.notSupported](mscriticalmessagingerror/notsupported.md)
  The framework doesn’t support the current device.
- [MSCriticalMessagingError.notAuthorized](mscriticalmessagingerror/notauthorized.md)
  The operation isn’t authorized.


---

*[View on Apple Developer](https://developer.apple.com/documentation/messages/mscriticalmessagingerror/sendfailed)*