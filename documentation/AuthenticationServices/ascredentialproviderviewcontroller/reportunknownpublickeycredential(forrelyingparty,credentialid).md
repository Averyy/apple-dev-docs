# reportUnknownPublicKeyCredential(forRelyingParty:credentialID:)

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Receives a report from the system that a relying party indicated a passkey credential is invalid.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func reportUnknownPublicKeyCredential(forRelyingParty relyingParty: String, credentialID: Data)
```

```objc
- (void) reportUnknownPublicKeyCredentialForRelyingParty:(NSString *) relyingParty credentialID:(NSData *) credentialID;
```

#### Discussion

The system calls this method when a relying party reports an invalid passkey by calling [`reportUnknownPublicKeyCredential(relyingPartyIdentifier:credentialID:)`](../ascredentialupdater/reportunknownpublickeycredential%28relyingpartyidentifier,credentialid%29.md). Your manager can hide or remove the credential after it receives this report.

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

- `relyingParty`: The relying party, typically a website, for which to update the credential.
- `credentialID`: An identifier that uniquely identifies the passkey.

## See Also

### Receiving credential updates
- [func reportAllAcceptedPublicKeyCredentials(forRelyingParty: String, userHandle: Data, acceptedCredentialIDs: [Data])](./reportallacceptedpublickeycredentials%28forrelyingparty,userhandle,acceptedcredentialids%29.md)
  Receives a report from the system that a relying party sent a snapshot of all accepted credentials for an account.
- [func reportPublicKeyCredentialUpdate(forRelyingParty: String, userHandle: Data, newName: String)](./reportpublickeycredentialupdate%28forrelyingparty,userhandle,newname%29.md)
  Receives a report from the system that a relying party indicated that a passkey’s user name updated.
- [func reportUnusedPasswordCredential(forDomain: String, userName: String)](./reportunusedpasswordcredential%28fordomain,username%29.md)
  Receives a report from the system that a relying party indicatd that a password credential isn’t needed anymore for a given user name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/ascredentialproviderviewcontroller/reportunknownpublickeycredential(forrelyingparty:credentialid:))*