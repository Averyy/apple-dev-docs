# extensionInput

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

An input for WebAuthn extensions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var extensionInput: ASPasskeyCredentialExtensionInput { get }
```

## See Also

### Viewing passkey challenge information
- [var clientDataHash: Data](./clientdatahash.md)
  The hash of the client data for this assertion.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./userverificationpreference.md)
  The relying party’s user verification preference.
- [var supportedAlgorithms: [ASCOSEAlgorithmIdentifier]](./supportedalgorithms-74mad.md)
  A list of cryptographic signature algorithms that the relying party supports.
- [enum ASPasskeyCredentialExtensionInput](../aspasskeycredentialextensioninput.md)
  A type for WebAuthn extension inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/extensioninput)*