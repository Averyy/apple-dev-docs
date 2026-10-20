# relyingParty

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The relying party associated with this passkey.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var relyingParty: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * relyingParty;
```

## See Also

### Accessing credential information
- [var authenticatorData: Data](./authenticatordata.md)
  The authenticator data of the application that created this passkey assertion credential.
- [var clientDataHash: Data](./clientdatahash.md)
  A hash of the client data for this credential.
- [var credentialID: Data](./credentialid.md)
  The identifier for this credential.
- [var signature: Data](./signature.md)
  The cryptographic signature of this credential.
- [var userHandle: Data](./userhandle.md)
  The user handle of this passkey.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredential/relyingparty)*