# clientDataHash

**Framework**: Authentication Services  
**Kind**: property

The hash of the client data for this assertion.

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

#### Discussion

Use the client data hash for both registration and assertion challenges.

## See Also

- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](aspasskeycredentialrequest/userverificationpreference.md)
  The relying party’s user verification preference.
- [var supportedAlgorithms: [ASCOSEAlgorithmIdentifier]](aspasskeycredentialrequest/supportedalgorithms-74mad.md)
  A list of cryptographic signature algorithms that the relying party supports.
- [var extensionInput: ASPasskeyCredentialExtensionInput](aspasskeycredentialrequest/extensioninput.md)
  An input for WebAuthn extensions.
- [enum ASPasskeyCredentialExtensionInput](aspasskeycredentialextensioninput.md)
  A type for WebAuthn extension inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/clientdatahash)*