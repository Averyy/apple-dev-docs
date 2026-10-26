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

```objc
@property (nonatomic, readonly) NSArray<NSNumber *> * supportedAlgorithms;
```

#### Discussion

For credential assertion requests, this property is empty. For credential registration requests, it contains one or more numbers from the Internet Assigned Numbers Authority (IANA) [Concise Binary Object Representation Object Signing and Encryption (COSE) algorithms registry](https://www.iana.org/assignments/cose/cose.xhtml#algorithms), as [`NSNumber`](../../Foundation/nsnumber.md) objects.

## See Also

### Viewing passkey challenge information
- [var clientDataHash: Data](./clientdatahash.md)
  The hash of the client data for this assertion.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./userverificationpreference.md)
  The relying party’s user verification preference.
- [assertionExtensionInput](./assertionextensioninput.md)
  An input for WebAuthn extensions.
- [ASPasskeyAssertionCredentialExtensionInput](../aspasskeyassertioncredentialextensioninput-c.class.md)
  A type that encapsulates input for various WebAuthn extensions during passkey assertion.
- [registrationExtensionInput](./registrationextensioninput.md)
  An input for WebAuthn extensions.
- [ASPasskeyRegistrationCredentialExtensionInput](../aspasskeyregistrationcredentialextensioninput-c.class.md)
  A type that encapsulates input for various WebAuthn extensions during passkey registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeycredentialrequest/supportedalgorithms-27z68)*