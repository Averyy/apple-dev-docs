# CredentialSession.Event.sessionInvalidated(reason:)

**Framework**: SecureElementCredential  
**Kind**: case

The session became invalidated.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case sessionInvalidated(reason: CredentialSession.ErrorCode)
```

#### Discussion

The associated value `reason` provides a reason for the invalidation.

## See Also

- [CredentialSession.ErrorCode](credentialsession/errorcode.md)
  An error encountered by a credential session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/event/sessioninvalidated(reason:))*