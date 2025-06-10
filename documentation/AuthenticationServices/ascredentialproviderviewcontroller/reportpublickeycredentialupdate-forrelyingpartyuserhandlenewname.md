# reportPublicKeyCredentialUpdate(forRelyingParty:userHandle:newName:)

**Framework**: Authentication Services  
**Kind**: method

Receives a report from the system that a relying party indicated that a passkey’s user name updated.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reportPublicKeyCredentialUpdate(forRelyingParty relyingParty: String, userHandle: Data, newName: String)
```

#### Discussion

The system calls this method when a relying party sends an updated user name by calling [`reportPublicKeyCredentialUpdate(relyingPartyIdentifier:userHandle:newName:)`](ascredentialupdater/reportpublickeycredentialupdate(relyingpartyidentifier:userhandle:newname:).md).

> ❗ **Important**: Perform any updates in the background and don’t show a blocking UI or any error.

To indicate support for this feature, add the key `SupportsCredentialUpdate` with a value of `YES` under the `ASCredentialProviderExtensionCapabilities` dictionary in your app’s information property list:

```not specified
Info.plist
├─ NSExtension
    ├─ NSExtensionAttributes
        ├─ ASCredentialProviderExtensionCapabilities
            ├─ SupportsCredentialUpdate => YES
```

## Parameters

- `relyingParty`: The relying party, typically a website, for which to save the credential.
- `userHandle`: The user identifier.
- `newName`: The new user name for the credential.

## See Also

- [func reportAllAcceptedPublicKeyCredentials(forRelyingParty: String, userHandle: Data, acceptedCredentialIDs: [Data])](ascredentialproviderviewcontroller/reportallacceptedpublickeycredentials(forrelyingparty:userhandle:acceptedcredentialids:).md)
  Receives a report from the system that a relying party sent a snapshot of all accepted credentials for an account.
- [func reportUnknownPublicKeyCredential(forRelyingParty: String, credentialID: Data)](ascredentialproviderviewcontroller/reportunknownpublickeycredential(forrelyingparty:credentialid:).md)
  Receives a report from the system that a relying party indicated a passkey credential is invalid.
- [func reportUnusedPasswordCredential(forDomain: String, userName: String)](ascredentialproviderviewcontroller/reportunusedpasswordcredential(fordomain:username:).md)
  Receives a report from the system that a relying party indicatd that a password credential isn’t needed anymore for a given user name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/reportpublickeycredentialupdate(forrelyingparty:userhandle:newname:))*