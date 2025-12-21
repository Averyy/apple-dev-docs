# init(userHandle:relyingParty:signature:clientDataHash:authenticatorData:credentialID:extensionOutput:)

**Framework**: Authentication Services  
**Kind**: init

Initializes a passkey assertion credential object, optionally specifying an extension output.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
convenience init(userHandle: Data, relyingParty: String, signature: Data, clientDataHash: Data, authenticatorData: Data, credentialID: Data, extensionOutput: ASPasskeyAssertionCredentialExtensionOutput?)
```

## Parameters

- `userHandle`: The user handle of the passkey.
- `relyingParty`: The relying party associated with the passkey.
- `signature`: The cryptographic signature of the credential.
- `clientDataHash`: A hash of the client data for the credential.
- `authenticatorData`: The authenticator data of the app that creates the credential.
- `credentialID`: The identifier for the credential.
- `extensionOutput`: An output from WebAuthn extensions.

## See Also

- [init(userHandle: Data, relyingParty: String, signature: Data, clientDataHash: Data, authenticatorData: Data, credentialID: Data)](aspasskeyassertioncredential/init(userhandle:relyingparty:signature:clientdatahash:authenticatordata:credentialid:).md)
  Initializes a passkey assertion credential object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredential/init(userhandle:relyingparty:signature:clientdatahash:authenticatordata:credentialid:extensionoutput:))*