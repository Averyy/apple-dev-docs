# init(userHandle:relyingParty:signature:clientDataHash:authenticatorData:credentialID:)

**Framework**: Authentication Services  
**Kind**: init

Initializes a passkey assertion credential object.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(userHandle: Data, relyingParty: String, signature: Data, clientDataHash: Data, authenticatorData: Data, credentialID: Data)
```

## Parameters

- `userHandle`: The user handle of this passkey.
- `relyingParty`: The relying party associated with this passkey.
- `signature`: The cryptographic signature of this credential.
- `clientDataHash`: A hash of the client data for this credential.
- `authenticatorData`: The authenticator data of the application that created this credential.
- `credentialID`: The identifier for this credential.

## See Also

- [convenience init(userHandle: Data, relyingParty: String, signature: Data, clientDataHash: Data, authenticatorData: Data, credentialID: Data, extensionOutput: ASPasskeyAssertionCredentialExtensionOutput?)](aspasskeyassertioncredential/init(userhandle:relyingparty:signature:clientdatahash:authenticatordata:credentialid:extensionoutput:).md)
  Initializes a passkey assertion credential object, optionally specifying an extension output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredential/init(userhandle:relyingparty:signature:clientdatahash:authenticatordata:credentialid:))*