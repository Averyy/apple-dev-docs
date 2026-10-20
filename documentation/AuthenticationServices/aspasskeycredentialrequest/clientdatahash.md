# clientDataHash

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) NSData * clientDataHash;
```

#### Discussion

Use the client data hash for both registration and assertion challenges.

## See Also

### Viewing passkey challenge information
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./userverificationpreference.md)
  The relying party’s user verification preference.
- [var supportedAlgorithms: [ASCOSEAlgorithmIdentifier]](./supportedalgorithms-74mad.md)
  A list of cryptographic signature algorithms that the relying party supports.
- [var extensionInput: ASPasskeyCredentialExtensionInput](./extensioninput.md)
  An input for WebAuthn extensions.
- [enum ASPasskeyCredentialExtensionInput](../aspasskeycredentialextensioninput.md)
  A type for WebAuthn extension inputs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/clientdatahash)*