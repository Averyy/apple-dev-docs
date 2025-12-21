# ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput

**Framework**: Authentication Services  
**Kind**: struct

The result of the large binary object support check, resulting from a passkey registration response.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput
```

#### Overview

This type indicates whether the passkey provider that manages the passkey supports the `largeBlob` extension. The design of this type mirrors the response in the WebAuthn specification.

## Topics

### Accessing output properties
- [var isSupported: Bool](asauthorizationpublickeycredentiallargeblobregistrationoutput-swift.struct/issupported.md)
  A Boolean value that indicates support for the large binary object extension.
### Using defined support values
- [static var supported: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput](asauthorizationpublickeycredentiallargeblobregistrationoutput-swift.struct/supported.md)
- [static var unsupported: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput](asauthorizationpublickeycredentiallargeblobregistrationoutput-swift.struct/unsupported.md)

## See Also

- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput?](aspasskeyregistrationcredentialextensionoutput-swift.struct/largeblob.md)
  The output for a large binary object operation during passkey registration.
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput?](aspasskeyregistrationcredentialextensionoutput-swift.struct/prf.md)
  The outputs of the WebAuthn PRF extension in passkey registration requests.
- [struct ASAuthorizationPublicKeyCredentialPRFRegistrationOutput](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct.md)
  A type to represent outputs of the web authentication PRF extension, when requesting them during a registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentiallargeblobregistrationoutput-swift.struct)*