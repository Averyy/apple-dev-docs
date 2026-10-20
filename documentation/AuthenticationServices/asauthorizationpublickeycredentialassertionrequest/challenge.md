# challenge

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The challenge to sign.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var challenge: Data { get set }
```

```objc
@property (nonatomic, copy) NSData * challenge;
```

## See Also

### Getting the properties
- [var relyingPartyIdentifier: String](./relyingpartyidentifier.md)
  The domain name of the website for the credential.
- [var allowedCredentials: [any ASAuthorizationPublicKeyCredentialDescriptor]](./allowedcredentials.md)
  A list of allowed credential descriptors the user attempts to sign in with.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./userverificationpreference.md)
  A preference that indicates whether the authenticator attempts to verify the user at the time of sign-in.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialassertionrequest/challenge)*