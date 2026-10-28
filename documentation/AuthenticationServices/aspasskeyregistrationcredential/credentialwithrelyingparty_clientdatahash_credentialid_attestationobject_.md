# credentialWithRelyingParty:clientDataHash:credentialID:attestationObject:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Type Method

Creates and initializes a new passkey registration credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) credentialWithRelyingParty:(NSString *) relyingParty clientDataHash:(NSData *) clientDataHash credentialID:(NSData *) credentialID attestationObject:(NSData *) attestationObject;
```

## Return Value

The credential object.

## Parameters

- `relyingParty`: The relying party associated with this passkey.
- `clientDataHash`: A hash of the client data for this credential.
- `credentialID`: The identifier for this credential.
- `attestationObject`: The attestation object for this passkey, which may contain an attestation statement and authenticator data.

## See Also

### Creating a passkey registration credential
- [init(relyingParty: String, clientDataHash: Data, credentialID: Data, attestationObject: Data)](./init%28relyingparty,clientdatahash,credentialid,attestationobject%29.md)
  Initializes a passkey registration credential object.
- [- initWithRelyingParty:clientDataHash:credentialID:attestationObject:extensionOutput:](./initwithrelyingparty_clientdatahash_credentialid_attestationobject_extensionoutput_.md)
  Initializes a passkey registration credential object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredential/credentialwithrelyingparty:clientdatahash:credentialid:attestationobject:)*