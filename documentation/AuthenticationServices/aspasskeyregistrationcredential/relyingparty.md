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
@property (nonatomic, readonly) NSString * relyingParty;
```

## See Also

### Accessing credential information
- [var attestationObject: Data](./attestationobject.md)
  The attestation object for this passkey.
- [var clientDataHash: Data](./clientdatahash.md)
  A hash of the client data for this credential.
- [var credentialID: Data](./credentialid.md)
  The identifier for this credential.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredential/relyingparty)*