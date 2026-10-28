# supportedAlgorithms

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

For credential assertion requests, this property is empty.

## See Also

### Viewing passkey challenge information
- [var clientDataHash: Data](./clientdatahash.md)
  The hash of the client data for this assertion.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./userverificationpreference.md)
  The relying party’s user verification preference.
- [var extensionInput: ASPasskeyCredentialExtensionInput](./extensioninput.md)
  An input for WebAuthn extensions.
- [enum ASPasskeyCredentialExtensionInput](../aspasskeycredentialextensioninput.md)
  A type for WebAuthn extension inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/supportedalgorithms-74mad)*