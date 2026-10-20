# clientDataHash

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A hash of the client data for this credential.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var clientDataHash: Data { get }
```

```objc
@property (nonatomic, copy, readonly) NSData * clientDataHash;
```

## See Also

### Accessing credential information
- [var authenticatorData: Data](./authenticatordata.md)
  The authenticator data of the application that created this passkey assertion credential.
- [var credentialID: Data](./credentialid.md)
  The identifier for this credential.
- [var relyingParty: String](./relyingparty.md)
  The relying party associated with this passkey.
- [var signature: Data](./signature.md)
  The cryptographic signature of this credential.
- [var userHandle: Data](./userhandle.md)
  The user handle of this passkey.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredential/clientdatahash)*