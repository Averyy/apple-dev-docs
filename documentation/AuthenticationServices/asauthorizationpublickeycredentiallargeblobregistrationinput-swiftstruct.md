# ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput

**Framework**: Authentication Services  
**Kind**: struct

A type that encapsulates input for large binary object extensions during registration.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput
```

#### Overview

Use this type during registration of a new passkey to indicate whether the app requires `largeBlob` support or just needs to know if it’s available. This can be different per passkey, depending on which passkey provider someone chooses to use, but can’t change after you create the passkey. This behavior mirrors the options available in the WebAuthn spec.

## Topics

### Determining binary large object support
- [var supportRequirement: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput.SupportRequirement](asauthorizationpublickeycredentiallargeblobregistrationinput-swift.struct/supportrequirement-swift.property.md)
  A type that represents the level of support required for the large binary object passkey extension.
- [ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput.SupportRequirement](asauthorizationpublickeycredentiallargeblobregistrationinput-swift.struct/supportrequirement-swift.enum.md)
  Values that express the level of support required for the binary large object passkey extension.
### Using defined support values
- [static var supportPreferred: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput](asauthorizationpublickeycredentiallargeblobregistrationinput-swift.struct/supportpreferred.md)
  A value that indicates the app needs binary large object support.
- [static var supportRequired: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput](asauthorizationpublickeycredentiallargeblobregistrationinput-swift.struct/supportrequired.md)
  A value that indicates the app requires large binary object support.

## See Also

- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationInput?](aspasskeyregistrationcredentialextensioninput-swift.struct/largeblob.md)
  Input for the WebAuthn large binary object extension in passkey registration requests.
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationInput?](aspasskeyregistrationcredentialextensioninput-swift.struct/prf.md)
  Input for the WebAuthn PRF extension in passkey registration requests.
- [struct ASAuthorizationPublicKeyCredentialPRFRegistrationInput](asauthorizationpublickeycredentialprfregistrationinput-swift.struct.md)
  A type that encapsulates input for PRF extensions during registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentiallargeblobregistrationinput-swift.struct)*