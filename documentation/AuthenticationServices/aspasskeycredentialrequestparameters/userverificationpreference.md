# userVerificationPreference

**Framework**: Authentication Services  
**Kind**: property

The relying party’s preference for user verification.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference { get }
```

## See Also

- [var allowedCredentials: [Data]](aspasskeycredentialrequestparameters/allowedcredentials.md)
  A list of passkey credentials that the relying party accepts for this challenge.
- [var clientDataHash: Data](aspasskeycredentialrequestparameters/clientdatahash.md)
  The client data that you sign as part of the response.
- [var relyingPartyIdentifier: String](aspasskeycredentialrequestparameters/relyingpartyidentifier.md)
  The relying party that issues the challenge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequestparameters/userverificationpreference)*