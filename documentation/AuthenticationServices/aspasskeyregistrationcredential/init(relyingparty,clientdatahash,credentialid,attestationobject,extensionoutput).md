# init(relyingParty:clientDataHash:credentialID:attestationObject:extensionOutput:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Initializes a passkey registration credential object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
convenience init(relyingParty: String, clientDataHash: Data, credentialID: Data, attestationObject: Data, extensionOutput: ASPasskeyRegistrationCredentialExtensionOutput?)
```

## Parameters

- `relyingParty`: The relying party associated with the passkey.
- `clientDataHash`: A hash of the client data for the credential.
- `credentialID`: The identifier for the credential.
- `attestationObject`: The attestation object for the passkey, which may contain an attestation statement and authenticator data.
- `extensionOutput`: The extension output data.

## See Also

### Creating a passkey registration credential
- [init(relyingParty: String, clientDataHash: Data, credentialID: Data, attestationObject: Data)](./init%28relyingparty,clientdatahash,credentialid,attestationobject%29.md)
  Initializes a passkey registration credential object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredential/init(relyingparty:clientdatahash:credentialid:attestationobject:extensionoutput:))*