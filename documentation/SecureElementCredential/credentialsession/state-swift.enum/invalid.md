# CredentialSession.State.invalid

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

The state of an invalid credential session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case invalid
```

#### Discussion

An invalid session is no longer available for use. To resume Secure Element credential functionality, call [`startSession()`](../startsession%28%29.md) to create a new session.

## See Also

### Credential session states
- [CredentialSession.State.management](./management.md)
  The state for managing the credential session.
- [case wired(credential: CredentialSession.Credential)](./wired%28credential%29.md)
  The state for performing wired operations with a given credential.
- [case cardEmulation(credential: CredentialSession.Credential)](./cardemulation%28credential%29.md)
  The state for performing card emulation with a given credential.
- [CredentialSession.Credential](../credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/state-swift.enum/invalid)*