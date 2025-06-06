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

> **Note**: The session doesn’t send this event if a credential fails to install. Instead, the credential remains in the [`CredentialSession.Credential.State.installationPending`](credentialsession/credential/state-swift.enum/installationpending.md) state until the app calls [`listCredentials()`](credentialsession/listcredentials().md). This call allows the framework to confirm that the installation failed and transitions the credential state to [`CredentialSession.Credential.State.installationFailed`](credentialsession/credential/state-swift.enum/installationfailed.md).

The session doesn’t send this event if a credential fails to install. Instead, the credential remains in the [`CredentialSession.Credential.State.installationPending`](credentialsession/credential/state-swift.enum/installationpending.md) state until the app calls [`listCredentials()`](credentialsession/listcredentials().md). This call allows the framework to confirm that the installation failed and transitions the credential state to [`CredentialSession.Credential.State.installationFailed`](credentialsession/credential/state-swift.enum/installationfailed.md).

## See Also

- [CredentialSession.Credential](credentialsession/credential.md)
  Information about a credential that a credential session retrieves from the Secure Element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/secureelementcredential/credentialsession/event/credentialfinishedinstalling(credential:))*