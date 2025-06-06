# name

**Framework**: Authentication Services  
**Kind**: property  
**Required**: Yes

A user-visible name that identifies a credential.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var name: String { get set }
```

## See Also

- [var attestationPreference: ASAuthorizationPublicKeyCredentialAttestationKind](asauthorizationpublickeycredentialregistrationrequest/attestationpreference.md)
  The type of attestation you’re requesting.
- [var challenge: Data](asauthorizationpublickeycredentialregistrationrequest/challenge.md)
  Arbitrary data that the client signs as proof of a valid registration or attestation.
- [var displayName: String?](asauthorizationpublickeycredentialregistrationrequest/displayname.md)
  A user-visible name for the credential, such as the account’s user name.
- [var relyingPartyIdentifier: String](asauthorizationpublickeycredentialregistrationrequest/relyingpartyidentifier.md)
  The domain name of the website for the credential.
- [var userID: Data](asauthorizationpublickeycredentialregistrationrequest/userid.md)
  Data that the relying party associates with the credential.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](asauthorizationpublickeycredentialregistrationrequest/userverificationpreference.md)
  A preference for whether the authenticator attempts to verify the user at the time of sign-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialregistrationrequest/name)*