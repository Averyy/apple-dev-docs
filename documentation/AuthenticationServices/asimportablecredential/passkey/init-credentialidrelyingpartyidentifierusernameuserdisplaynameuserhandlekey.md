# init(credentialID:relyingPartyIdentifier:userName:userDisplayName:userHandle:key:)

**Framework**: Authentication Services  
**Kind**: init

Creates a passkey instance.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst 18.2+
- macOS 15.2+
- visionOS 2.2+

## Declaration

```swift
init(credentialID: Data, relyingPartyIdentifier: String, userName: String, userDisplayName: String, userHandle: Data, key: Data)
```

## Parameters

- `credentialID`: The credential ID associated with this passkey.
- `relyingPartyIdentifier`: The relying party identifier associated with the passkey
- `userName`: The username associated with the passkey.
- `userDisplayName`: The human-readable name associated with the passkey.
- `userHandle`: The user handle associated with the passkey.
- `key`: The private key associated with this passkey.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asimportablecredential/passkey/init(credentialid:relyingpartyidentifier:username:userdisplayname:userhandle:key:))*