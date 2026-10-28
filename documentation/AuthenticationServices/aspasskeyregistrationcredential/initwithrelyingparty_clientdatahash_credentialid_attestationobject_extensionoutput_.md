# initWithRelyingParty:clientDataHash:credentialID:attestationObject:extensionOutput:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Instance Method

Initializes a passkey registration credential object.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
- (instancetype) initWithRelyingParty:(NSString *) relyingParty clientDataHash:(NSData *) clientDataHash credentialID:(NSData *) credentialID attestationObject:(NSData *) attestationObject extensionOutput:(ASPasskeyRegistrationCredentialExtensionOutput *) extensionOutput;
```

## Return Value

The credential object.

## Parameters

- `relyingParty`: The relying party associated with the passkey.
- `clientDataHash`: A hash of the client data for the credential.
- `credentialID`: The identifier for the credential.
- `attestationObject`: The attestation object for the passkey, which may contain an attestation statement and authenticator data.
- `extensionOutput`: The extension output data, if any.

## See Also

### Creating a passkey registration credential
- [+ credentialWithRelyingParty:clientDataHash:credentialID:attestationObject:](./credentialwithrelyingparty_clientdatahash_credentialid_attestationobject_.md)
  Creates and initializes a new passkey registration credential.
- [init(relyingParty: String, clientDataHash: Data, credentialID: Data, attestationObject: Data)](./init%28relyingparty,clientdatahash,credentialid,attestationobject%29.md)
  Initializes a passkey registration credential object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredential/initwithrelyingparty:clientdatahash:credentialid:attestationobject:extensionoutput:)*