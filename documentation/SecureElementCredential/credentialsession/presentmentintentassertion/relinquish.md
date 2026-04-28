# relinquish()

**Framework**: SecureElementCredential  
**Kind**: method

Ends the presentment intent assertion.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+

## Declaration

```swift
final func relinquish() async throws
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Discussion

Call this function after your presentment task finishes.

A [`CredentialSession.PresentmentIntentAssertion`](credentialsession/presentmentintentassertion.md) times out after 60 seconds. If you don’t explicitly relinquish the object by then, the session produces a [`CredentialSession.Event.presentmentIntentAssertionTimeout`](credentialsession/event/presentmentintentassertiontimeout.md) event, and invalidates this object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/presentmentintentassertion/relinquish())*