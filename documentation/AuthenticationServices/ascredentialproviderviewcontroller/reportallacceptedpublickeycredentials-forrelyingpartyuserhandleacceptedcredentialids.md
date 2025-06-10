# reportAllAcceptedPublicKeyCredentials(forRelyingParty:userHandle:acceptedCredentialIDs:)

**Framework**: Authentication Services  
**Kind**: method

Receives a report from the system that a relying party sent a snapshot of all accepted credentials for an account.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reportAllAcceptedPublicKeyCredentials(forRelyingParty relyingParty: String, userHandle: Data, acceptedCredentialIDs: [Data])
```

#### Discussion

The system calls this method when a relying party sends a list of accepted credentials by calling [`reportAllAcceptedPublicKeyCredentials(relyingPartyIdentifier:userHandle:acceptedCredentialIDs:)`](ascredentialupdater/reportallacceptedpublickeycredentials(relyingpartyidentifier:userhandle:acceptedcredentialids:).md). Your manager can hide or remove any credential that’s absent from the `acceptedCredentialIDs` array.

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

- `relyingParty`: The relying party, typically a website, for which to save the credentials.
- `userHandle`: The user identifier.
- `acceptedCredentialIDs`: An array of identifiers that uniquely identifies the accepted credentials.

## See Also

- [func reportPublicKeyCredentialUpdate(forRelyingParty: String, userHandle: Data, newName: String)](ascredentialproviderviewcontroller/reportpublickeycredentialupdate(forrelyingparty:userhandle:newname:).md)
  Receives a report from the system that a relying party indicated that a passkey’s user name updated.
- [func reportUnknownPublicKeyCredential(forRelyingParty: String, credentialID: Data)](ascredentialproviderviewcontroller/reportunknownpublickeycredential(forrelyingparty:credentialid:).md)
  Receives a report from the system that a relying party indicated a passkey credential is invalid.
- [func reportUnusedPasswordCredential(forDomain: String, userName: String)](ascredentialproviderviewcontroller/reportunusedpasswordcredential(fordomain:username:).md)
  Receives a report from the system that a relying party indicatd that a password credential isn’t needed anymore for a given user name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/reportallacceptedpublickeycredentials(forrelyingparty:userhandle:acceptedcredentialids:))*