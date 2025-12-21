# ASCredentialDataManager

**Framework**: Authentication Services  
**Kind**: class

This class allows submitting credentials and events to any credential manager enabled on the system.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
final class ASCredentialDataManager
```

#### Overview

By informing credential managers of new, updated, removed, or revoked credentials, they can stay synchronized with the credential information of the person using the device.

In order to protect the user’s privacy, `ASCredentialDataManager` does not indicate whether the operation succeeded. A successful call only indicates that the parameters passed were well formed.

## Topics

### Initializers
- [init()](ascredentialdatamanager/init.md)
### Instance Methods
- [func reportAllAcceptedPublicKeyCredentials(relyingPartyIdentifier: String, userHandle: Data, acceptedCredentialIDs: [Data]) async throws](ascredentialdatamanager/reportallacceptedpublickeycredentials(relyingpartyidentifier:userhandle:acceptedcredentialids:).md)
  Report a snapshot of all the credentialIDs that will be accepted for a `userHandle`. Credentials not present in the `acceptedCredentialIDs` may be removed or hidden by a password manager. Relying party may choose to perform this periodically, e.g. on every sign in. This information is shared with all password managers enabled in the system.
- [func reportPublicKeyCredentialUpdate(relyingPartyIdentifier: String, userHandle: Data, newName: String) async throws](ascredentialdatamanager/reportpublickeycredentialupdate(relyingpartyidentifier:userhandle:newname:).md)
  Report an update to a credential’s name, such as when changing the user name on an account. This information is shared with all password managers enabled in the system.
- [func reportUnknownPublicKeyCredential(relyingPartyIdentifier: String, credentialID: Data) async throws](ascredentialdatamanager/reportunknownpublickeycredential(relyingpartyidentifier:credentialid:).md)
  Report that a specific credential is unknown or no longer accepted. The credential may be removed or hidden by a password manager. This information is shared with all password managers enabled in the system.
- [func reportUnusedPasswordCredential(domain: String, userName: String) async throws](ascredentialdatamanager/reportunusedpasswordcredential(domain:username:).md)
  Report an unused password credential for a given domain and username. Password managers may remove or hide the password credential. This information is shared with all password managers enabled in the system.
- [func save(password: ASPasswordCredential, for: ASAutoFillURLScope, title: String?, anchor: ASPresentationAnchor) async throws](ascredentialdatamanager/save(password:for:title:anchor:).md)
  Save or update a password credential to the user’s preferred password manager in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialdatamanager)*