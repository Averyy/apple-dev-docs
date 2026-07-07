# CredentialSession.State.management

**Framework**: SecureElementCredential  
**Kind**: case

The state for managing the credential session.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case management
```

## Mentions

- [Accessing and using secure element credentials](accessing-and-using-secure-element-credentials.md)

#### Discussion

In this state, the session can list all credentials and can add and delete individual credentials.

## See Also

- [case wired(credential: CredentialSession.Credential)](credentialsession/state-swift.enum/wired(credential:).md)
  The state for performing wired operations with a given credential.
- [case cardEmulation(credential: CredentialSession.Credential)](credentialsession/state-swift.enum/cardemulation(credential:).md)
  The state for performing card emulation with a given credential.
- [CredentialSession.Credential](credentialsession/credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.
- [CredentialSession.State.invalid](credentialsession/state-swift.enum/invalid.md)
  The state of an invalid credential session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/state-swift.enum/management)*