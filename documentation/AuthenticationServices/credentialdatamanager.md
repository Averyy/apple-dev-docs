# CredentialDataManager

**Framework**: Authentication Services  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 26.2+
- iPadOS 26.2+
- Mac Catalyst 26.2+
- macOS 26.2+
- visionOS 26.2+

## Declaration

```swift
@MainActor
struct CredentialDataManager
```

## Topics

### Instance Methods
- [func reportAllAcceptedPublicKeyCredentials(relyingPartyIdentifier: String, userHandle: Data, acceptedCredentialIDs: [Data]) async throws](./credentialdatamanager/reportallacceptedpublickeycredentials%28relyingpartyidentifier,userhandle,acceptedcredentialids%29.md)
  Report a snapshot of all the credentialIDs that will be accepted for a `userHandle`. Credentials not present in the `acceptedCredentialIDs` may be removed or hidden by a password manager. Relying party may choose to perform this periodically, e.g. on every sign in. This information is shared with all password managers enabled in the system.
- [func reportPublicKeyCredentialUpdate(relyingPartyIdentifier: String, userHandle: Data, newName: String) async throws](./credentialdatamanager/reportpublickeycredentialupdate%28relyingpartyidentifier,userhandle,newname%29.md)
  Report an update to a credential’s name, such as when changing the user name on an account. This information is shared with all password managers enabled in the system.
- [func reportUnknownPublicKeyCredential(relyingPartyIdentifier: String, credentialID: Data) async throws](./credentialdatamanager/reportunknownpublickeycredential%28relyingpartyidentifier,credentialid%29.md)
  Report that a specific credential is unknown or no longer accepted. The credential may be removed or hidden by a password manager. This information is shared with all password managers enabled in the system.
- [func reportUnusedPasswordCredential(domain: String, userName: String) async throws](./credentialdatamanager/reportunusedpasswordcredential%28domain,username%29.md)
  Report an unused password credential for a given domain and username. Password managers may remove or hide the password credential. This information is shared with all password managers enabled in the system.
- [func save(password: ASPasswordCredential, for: ASAutoFillURLScope, title: String?) async throws](./credentialdatamanager/save%28password,for,title%29.md)
  Save or update a password credential to the user’s preferred password manager in the system.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/credentialdatamanager)*