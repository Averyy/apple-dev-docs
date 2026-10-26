# init(relyingParty:clientDataHash:credentialID:attestationObject:)

**Framework**: Authentication Services  
**Kind**: init  
**Role**: Initializer

Initializes a passkey registration credential object.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
init(relyingParty: String, clientDataHash: Data, credentialID: Data, attestationObject: Data)
```

```objc
- (instancetype) initWithRelyingParty:(NSString *) relyingParty clientDataHash:(NSData *) clientDataHash credentialID:(NSData *) credentialID attestationObject:(NSData *) attestationObject;
```

## Parameters

- `relyingParty`: The relying party associated with this passkey.
- `clientDataHash`: A hash of the client data for this credential.
- `credentialID`: The identifier for this credential.
- `attestationObject`: The attestation object for this passkey, which may contain an attestation statement and authenticator data.

## See Also

### Creating a passkey registration credential
- [convenience init(relyingParty: String, clientDataHash: Data, credentialID: Data, attestationObject: Data, extensionOutput: ASPasskeyRegistrationCredentialExtensionOutput?)](./init%28relyingparty,clientdatahash,credentialid,attestationobject,extensionoutput%29.md)
  Initializes a passkey registration credential object.
- [+ credentialWithRelyingParty:clientDataHash:credentialID:attestationObject:](./credentialwithrelyingparty_clientdatahash_credentialid_attestationobject_.md)
  Creates and initializes a new passkey registration credential.
- [- initWithRelyingParty:clientDataHash:credentialID:attestationObject:extensionOutput:](./initwithrelyingparty_clientdatahash_credentialid_attestationobject_extensionoutput_.md)
  Initializes a passkey registration credential object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredential/init(relyingparty:clientdatahash:credentialid:attestationobject:))*