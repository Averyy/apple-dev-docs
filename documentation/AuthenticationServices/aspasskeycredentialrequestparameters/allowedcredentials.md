# allowedCredentials

**Framework**: Authentication Services  
**Kind**: property

A list of passkey credentials that the relying party accepts for this challenge.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var allowedCredentials: [Data] { get }
```

#### Discussion

If the array is empty, then the relying party accepts any passkey credential.

## See Also

- [var clientDataHash: Data](aspasskeycredentialrequestparameters/clientdatahash.md)
  The client data that you sign as part of the response.
- [var relyingPartyIdentifier: String](aspasskeycredentialrequestparameters/relyingpartyidentifier.md)
  The relying party that issues the challenge.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](aspasskeycredentialrequestparameters/userverificationpreference.md)
  The relying party’s preference for user verification.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequestparameters/allowedcredentials)*