# userHandle

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The user handle of this passkey.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var userHandle: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * userHandle;
```

## See Also

### Accessing credential information
- [var authenticatorData: Data](./authenticatordata.md)
  The authenticator data of the application that created this passkey assertion credential.
- [var clientDataHash: Data](./clientdatahash.md)
  A hash of the client data for this credential.
- [var credentialID: Data](./credentialid.md)
  The identifier for this credential.
- [var relyingParty: String](./relyingparty.md)
  The relying party associated with this passkey.
- [var signature: Data](./signature.md)
  The cryptographic signature of this credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredential/userhandle)*