# CredentialSession.State.wired(credential:)

**Framework**: SecureElementCredential  
**Kind**: case  
**Role**: Case

The state for performing wired operations with a given credential.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case wired(credential: CredentialSession.Credential)
```

## Mentions

- [Accessing and using secure element credentials](../../accessing-and-using-secure-element-credentials.md)

#### Discussion

In the wired state, the session can call [`transceive(_:)`](../transceive%28_%29.md) to exchange data with the selected credential.

## Parameters

- `credential`: The credential currently in use by the session.

## See Also

### Credential session states
- [CredentialSession.State.management](./management.md)
  The state for managing the credential session.
- [case cardEmulation(credential: CredentialSession.Credential)](./cardemulation%28credential%29.md)
  The state for performing card emulation with a given credential.
- [CredentialSession.Credential](../credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.
- [CredentialSession.State.invalid](./invalid.md)
  The state of an invalid credential session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/state-swift.enum/wired(credential:))*