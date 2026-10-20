# CredentialSession.State.cardEmulation(credential:)

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

The state for performing card emulation with a given credential.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case cardEmulation(credential: CredentialSession.Credential)
```

## Mentions

- [Accessing and using secure element credentials](../../accessing-and-using-secure-element-credentials.md)

#### Discussion

In the card emulation state, the session makes the selected credential available to NFC contactless readers.

## Parameters

- `credential`: The credential currently in use by the session.

## See Also

### Credential session states
- [CredentialSession.State.management](./management.md)
  The state for managing the credential session.
- [case wired(credential: CredentialSession.Credential)](./wired%28credential%29.md)
  The state for performing wired operations with a given credential.
- [CredentialSession.Credential](../credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.
- [CredentialSession.State.invalid](./invalid.md)
  The state of an invalid credential session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/state-swift.enum/cardemulation(credential:))*