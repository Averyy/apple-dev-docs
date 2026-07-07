# CredentialSession.State.invalid

**Framework**: SecureElementCredential  
**Kind**: case

The state of an invalid credential session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case invalid
```

#### Discussion

An invalid session is no longer available for use. To resume Secure Element credential functionality, call [`startSession()`](credentialsession/startsession().md) to create a new session.

## See Also

- [CredentialSession.State.management](credentialsession/state-swift.enum/management.md)
  The state for managing the credential session.
- [case wired(credential: CredentialSession.Credential)](credentialsession/state-swift.enum/wired(credential:).md)
  The state for performing wired operations with a given credential.
- [case cardEmulation(credential: CredentialSession.Credential)](credentialsession/state-swift.enum/cardemulation(credential:).md)
  The state for performing card emulation with a given credential.
- [CredentialSession.Credential](credentialsession/credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/state-swift.enum/invalid)*