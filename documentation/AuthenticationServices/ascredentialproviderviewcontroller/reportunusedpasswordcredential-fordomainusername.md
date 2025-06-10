# reportUnusedPasswordCredential(forDomain:userName:)

**Framework**: Authentication Services  
**Kind**: method

Receives a report from the system that a relying party indicatd that a password credential isn’t needed anymore for a given user name.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func reportUnusedPasswordCredential(forDomain domain: String, userName: String)
```

#### Discussion

> **Note**: > **Note**: This method will be called for handling password credential updates when a relying party indicates a password is no longer needed using the `ASCredentialUpdater` API. You may hide or remove the credential. This update should be handled in the background, so no blocking UI or error should ever be shown.

The system calls this method when a relying party reports calls [`reportUnusedPasswordCredential(domain:userName:)`](ascredentialupdater/reportunusedpasswordcredential(domain:username:).md) to indicate a password isn’t needed anymore. It may call this because a person using the app has transitioned to using a passkey, or because they deleted their account. Your manager can hide or remove the credential after it receives this report.

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

- `domain`: The website domain that the credential is saved for.
- `userName`: The account user name.

## See Also

- [func reportAllAcceptedPublicKeyCredentials(forRelyingParty: String, userHandle: Data, acceptedCredentialIDs: [Data])](ascredentialproviderviewcontroller/reportallacceptedpublickeycredentials(forrelyingparty:userhandle:acceptedcredentialids:).md)
  Receives a report from the system that a relying party sent a snapshot of all accepted credentials for an account.
- [func reportPublicKeyCredentialUpdate(forRelyingParty: String, userHandle: Data, newName: String)](ascredentialproviderviewcontroller/reportpublickeycredentialupdate(forrelyingparty:userhandle:newname:).md)
  Receives a report from the system that a relying party indicated that a passkey’s user name updated.
- [func reportUnknownPublicKeyCredential(forRelyingParty: String, credentialID: Data)](ascredentialproviderviewcontroller/reportunknownpublickeycredential(forrelyingparty:credentialid:).md)
  Receives a report from the system that a relying party indicated a passkey credential is invalid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/reportunusedpasswordcredential(fordomain:username:))*