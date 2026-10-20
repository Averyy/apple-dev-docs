# CredentialSession.Event.connectivityEvent(_:)

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

A credential received a connectivity event during card emulation.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case connectivityEvent(CredentialSession.ConnectivityEvent)
```

#### Discussion

You might not receive this event if your app hasn’t acquired the [`CredentialSession.PresentmentIntentAssertion`](../presentmentintentassertion.md). If your app doesn’t have the presentment intent assertion, Wallet or another default app might respond to certain field events, depending on the device configuration.

## See Also

### Card emulation events
- [CredentialSession.ConnectivityEvent](../connectivityevent.md)
  An event that a credential receives during card emulation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/event/connectivityevent(_:))*