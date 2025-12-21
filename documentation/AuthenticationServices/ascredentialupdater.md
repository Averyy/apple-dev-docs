# ASCredentialUpdater

**Framework**: Authentication Services  
**Kind**: class

A class to pass credential update events to credential managers enabled on the system.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
final class ASCredentialUpdater
```

#### Overview

The `ASCredentialUpdater` implements the functionality of the WebAuthn Signal API, allowing apps to update credential managers with information about existing credentials. By informing credential managers of updated, removed, or revoked credentials, the credential managers can stay synchronized with the credential information of the person using the device.

Use `ASCredendialUpdater` in the following scenarios:

The following example shows how an app might use this class when processing various sign-in and account-management events:

```swift
import AuthenticationServices

let credentialUpdater = ASCredentialUpdater()

func handleSuccessfulPasskeySignIn() {
    ...
    // Update passkey if the username changed on the account.
    try credentialUpdater.reportPublicKeyCredentialUpdate(relyingPartyIdentifier:"example.com", userHandle:userData, newName: "name")
    
    // Report accepted credentials.
    try credentialUpdater.reportAllAcceptedPublicKeyCredentials(relyingPartyIdentifier:"example.com", userHandle:userData, allowedCredentialIDs:[credentialID1, credentailID2])
    
    // Remove or hide stale password.
    try credentialUpdater.reportUnusedPasswordCredential(domain: "example.com", username:"user")
}

func handleFailedPasskeySignIn() {
    ...
    // Remove or hide invalid passkey.
    try credentialUpdater.reportUnknownPublicKeyCredential(relyingPartyIdentifier:"example.com", credentialID:credentialIDData)
}

func handleAccountAccountDeletion() {
    ...
    try credentialUpdater.reportAllAcceptedPublicKeyCredentials(relyingPartyIdentifier:"example.com", userHandle:userData, allowedCredentialIDs:[])
    try credentialUpdater.reportUnusedPasswordCredential(domain: "example.com", username:"user")
}
```

> **Note**: To protect the privacy of the person using the app, this class’s methods don’t indicate whether their operations succeeded. A successful call only indicates that the parameters were well formed.

## Topics

### Creating a credential updater
- [init()](ascredentialupdater/init.md)
  Creates an instance of the credential updater class.
### Reporting accepted credentials
- [func reportAllAcceptedPublicKeyCredentials(relyingPartyIdentifier: String, userHandle: Data, acceptedCredentialIDs: [Data]) async throws](ascredentialupdater/reportallacceptedpublickeycredentials(relyingpartyidentifier:userhandle:acceptedcredentialids:).md)
  Provides credential managers with a snapshot of all credential identifiers accepted for a given user handle.
### Reporting updated credentials
- [func reportPublicKeyCredentialUpdate(relyingPartyIdentifier: String, userHandle: Data, newName: String) async throws](ascredentialupdater/reportpublickeycredentialupdate(relyingpartyidentifier:userhandle:newname:).md)
  Provides credential managers with an update to a credential’s name, such as when changing the user name or email address on an account.
### Reporting unused and unknown credentials
- [func reportUnusedPasswordCredential(domain: String, userName: String) async throws](ascredentialupdater/reportunusedpasswordcredential(domain:username:).md)
  Informs credential managers that a password is no longer in use.
- [func reportUnknownPublicKeyCredential(relyingPartyIdentifier: String, credentialID: Data) async throws](ascredentialupdater/reportunknownpublickeycredential(relyingpartyidentifier:credentialid:).md)
  Informs credential managers that a specific credential is unknown or no longer accepted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialupdater)*