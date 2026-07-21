# CredentialSession.Event.credentialFinishedInstalling(credential:)

**Framework**: SecureElementCredential  
**Kind**: case

The session finished installing a credential.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+

## Declaration

```swift
case credentialFinishedInstalling(credential: CredentialSession.Credential)
```

#### Discussion

The associated value `credential` indicates which credential finished installing.

The [`CredentialSession.Credential`](credentialsession/credential.md) object returned could be in:

- [`CredentialSession.Credential.State.installed(instances:)`](credentialsession/credential/state-swift.enum/installed(instances:).md) if the installation succeeded
- [`CredentialSession.Credential.State.installationFailed`](credentialsession/credential/state-swift.enum/installationfailed.md) if the installation failed

## See Also

- [CredentialSession.Credential](credentialsession/credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/event/credentialfinishedinstalling(credential:))*