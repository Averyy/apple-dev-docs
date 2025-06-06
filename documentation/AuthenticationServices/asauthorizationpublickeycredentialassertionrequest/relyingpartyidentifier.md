# relyingPartyIdentifier

**Framework**: Authentication Services  
**Kind**: property  
**Required**: Yes

The domain name of the website for the credential.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var relyingPartyIdentifier: String { get set }
```

## See Also

- [var challenge: Data](asauthorizationpublickeycredentialassertionrequest/challenge.md)
  The challenge to sign.
- [var allowedCredentials: [any ASAuthorizationPublicKeyCredentialDescriptor]](asauthorizationpublickeycredentialassertionrequest/allowedcredentials.md)
  A list of allowed credential descriptors the user attempts to sign in with.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](asauthorizationpublickeycredentialassertionrequest/userverificationpreference.md)
  A preference that indicates whether the authenticator attempts to verify the user at the time of sign-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialassertionrequest/relyingpartyidentifier)*