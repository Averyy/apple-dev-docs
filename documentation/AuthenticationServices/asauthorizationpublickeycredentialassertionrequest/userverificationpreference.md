# userVerificationPreference

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

A preference that indicates whether the authenticator attempts to verify the user at the time of sign-in.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference { get set }
```

```objc
@property (nonatomic) ASAuthorizationPublicKeyCredentialUserVerificationPreference userVerificationPreference;
```

## See Also

### Getting the properties
- [var challenge: Data](./challenge.md)
  The challenge to sign.
- [var relyingPartyIdentifier: String](./relyingpartyidentifier.md)
  The domain name of the website for the credential.
- [var allowedCredentials: [any ASAuthorizationPublicKeyCredentialDescriptor]](./allowedcredentials.md)
  A list of allowed credential descriptors the user attempts to sign in with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialassertionrequest/userverificationpreference)*