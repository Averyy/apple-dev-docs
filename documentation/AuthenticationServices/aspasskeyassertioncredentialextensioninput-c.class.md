# ASPasskeyAssertionCredentialExtensionInput

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

A type that encapsulates input for various WebAuthn extensions during passkey assertion.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```objc
@interface ASPasskeyAssertionCredentialExtensionInput : NSObject
```

## Topics

### Inputs
- [largeBlob](./aspasskeyassertioncredentialextensioninput-c.class/largeblob.md)
  Input for the WebAuthn large binary object extension in passkey assertion requests.
- [ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput](./asauthorizationpublickeycredentiallargeblobassertioninput-c.class.md)
  A type that represents input for the binary large object extension in passkey assertion requests.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSCopying](../Foundation/nscopying.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Viewing passkey challenge information
- [var clientDataHash: Data](./aspasskeycredentialrequest/clientdatahash.md)
  The hash of the client data for this assertion.
- [var userVerificationPreference: ASAuthorizationPublicKeyCredentialUserVerificationPreference](./aspasskeycredentialrequest/userverificationpreference.md)
  The relying party’s user verification preference.
- [supportedAlgorithms](./aspasskeycredentialrequest/supportedalgorithms-27z68.md)
  A list of cryptographic signature algorithms that the relying party supports.
- [assertionExtensionInput](./aspasskeycredentialrequest/assertionextensioninput.md)
  An input for WebAuthn extensions.
- [registrationExtensionInput](./aspasskeycredentialrequest/registrationextensioninput.md)
  An input for WebAuthn extensions.
- [ASPasskeyRegistrationCredentialExtensionInput](./aspasskeyregistrationcredentialextensioninput-c.class.md)
  A type that encapsulates input for various WebAuthn extensions during passkey registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredentialextensioninput-c.class)*