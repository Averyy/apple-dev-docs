# CredentialSession.Event.presentmentIntentAssertionTimeout

**Framework**: SecureElementCredential  
**Kind**: case

The session’s presentment intent assertion timed out.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case presentmentIntentAssertionTimeout
```

#### Discussion

A [`CredentialSession.PresentmentIntentAssertion`](credentialsession/presentmentintentassertion.md) granted by a credential session lasts for 60 seconds. If it expires, your app needs to request a new one with [`acquirePresentmentAssertion()`](credentialsession/acquirepresentmentassertion().md).

## See Also

- [CredentialSession.Event.cardEmulationTimeout](credentialsession/event/cardemulationtimeout.md)
  The session’s card emulation timer expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/event/presentmentintentassertiontimeout)*