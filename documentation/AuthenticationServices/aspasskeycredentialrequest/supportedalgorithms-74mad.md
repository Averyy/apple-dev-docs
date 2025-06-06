# supportedAlgorithms

**Framework**: Authentication Services  
**Kind**: property

A list of cryptographic signature algorithms that the relying party supports.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var supportedAlgorithms: [ASCOSEAlgorithmIdentifier] { get }
```

#### Discussion

For credential assertion requests, this property is empty.

## See Also

- [var clientDataHash: Data](aspasskeycredentialrequest/clientdatahash.md)
  The hash of the client data for this assertion.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](aspasskeycredentialrequest/userverificationpreference.md)
  The relying party’s user verification preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/supportedalgorithms-74mad)*