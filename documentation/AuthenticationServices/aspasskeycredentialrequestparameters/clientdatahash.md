# clientDataHash

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

The client data that you sign as part of the response.

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

### Viewing credential request parameters
- [var allowedCredentials: [Data]](./allowedcredentials.md)
  A list of passkey credentials that the relying party accepts for this challenge.
- [var relyingPartyIdentifier: String](./relyingpartyidentifier.md)
  The relying party that issues the challenge.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./userverificationpreference.md)
  The relying party’s preference for user verification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequestparameters/clientdatahash)*