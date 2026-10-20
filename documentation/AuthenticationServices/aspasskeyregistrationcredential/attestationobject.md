# attestationObject

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The attestation object for this passkey.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var attestationObject: Data { get }
```

```objc
@property (nonatomic, readonly) NSData * attestationObject;
```

#### Discussion

The relying party may use information in the attestation object to assess the origin of a passkey during registration.

## See Also

### Accessing credential information
- [var clientDataHash: Data](./clientdatahash.md)
  A hash of the client data for this credential.
- [var credentialID: Data](./credentialid.md)
  The identifier for this credential.
- [var relyingParty: String](./relyingparty.md)
  The relying party associated with this passkey.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredential/attestationobject)*