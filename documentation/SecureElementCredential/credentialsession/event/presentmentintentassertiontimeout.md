# CredentialSession.Event.presentmentIntentAssertionTimeout

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

The session’s presentment intent assertion timed out.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case presentmentIntentAssertionTimeout
```

## Discussion

A [`CredentialSession.PresentmentIntentAssertion`](../presentmentintentassertion.md) granted by a credential session lasts for 60 seconds. If it expires, your app needs to request a new one with [`acquirePresentmentAssertion()`](../acquirepresentmentassertion%28%29.md).

## See Also

### Timeout events
- [CredentialSession.Event.cardEmulationTimeout](./cardemulationtimeout.md)
  The session’s card emulation timer expired.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/event/presentmentintentassertiontimeout)*