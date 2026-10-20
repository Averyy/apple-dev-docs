# userID

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Data that the relying party associates with the credential.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var userID: Data { get set }
```

```objc
@property (nonatomic, copy) NSData * userID;
```

## See Also

### Getting the properties
- [var attestationPreference: ASAuthorizationPublicKeyCredentialAttestationKind](./attestationpreference.md)
  The type of attestation you’re requesting.
- [var challenge: Data](./challenge.md)
  Arbitrary data that the client signs as proof of a valid registration or attestation.
- [var displayName: String?](./displayname.md)
  A user-visible name for the credential, such as the account’s user name.
- [var name: String](./name.md)
  A user-visible name that identifies a credential.
- [var relyingPartyIdentifier: String](./relyingpartyidentifier.md)
  The domain name of the website for the credential.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./userverificationpreference.md)
  A preference for whether the authenticator attempts to verify the user at the time of sign-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialregistrationrequest/userid)*