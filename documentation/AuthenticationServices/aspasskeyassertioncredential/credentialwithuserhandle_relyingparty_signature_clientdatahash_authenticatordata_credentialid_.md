# credentialWithUserHandle:relyingParty:signature:clientDataHash:authenticatorData:credentialID:

**Framework**: Authentication Services  
**Kind**: method  
**Role**: Type Method

Creates and initializes a new passkey assertion credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```objc
+ (instancetype) credentialWithUserHandle:(NSData *) userHandle relyingParty:(NSString *) relyingParty signature:(NSData *) signature clientDataHash:(NSData *) clientDataHash authenticatorData:(NSData *) authenticatorData credentialID:(NSData *) credentialID;
```

#### Return Value

The credential object.

## Parameters

- `userHandle`: The user handle of this passkey.
- `relyingParty`: The relying party associated with this passkey.
- `signature`: The cryptographic signature of this credential.
- `clientDataHash`: A hash of the client data for this credential.
- `authenticatorData`: The authenticator data of the application that created this credential.
- `credentialID`: The identifier for this credential.

## See Also

### Creating a passkey assertion credential
- [init(userHandle: Data, relyingParty: String, signature: Data, clientDataHash: Data, authenticatorData: Data, credentialID: Data)](./init%28userhandle,relyingparty,signature,clientdatahash,authenticatordata,credentialid%29.md)
  Initializes a passkey assertion credential object.
- [- initWithUserHandle:relyingParty:signature:clientDataHash:authenticatorData:credentialID:extensionOutput:](./initwithuserhandle_relyingparty_signature_clientdatahash_authenticatordata_credentialid_extensionoutput_.md)
  Initializes a passkey assertion credential object, optionally specifying an extension output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredential/credentialwithuserhandle:relyingparty:signature:clientdatahash:authenticatordata:credentialid:)*