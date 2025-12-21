# ASAuthorizationPublicKeyCredentialPRFRegistrationOutput

**Framework**: Authentication Services  
**Kind**: struct

A type to represent outputs of the web authentication PRF extension, when requesting them during a registration.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ASAuthorizationPublicKeyCredentialPRFRegistrationOutput
```

#### Overview

This object represents one or two `SymmetricKey` keys that are available anywhere the passkey is available for use. These are general purpose keys that you can use for application-specific needs, such as encryption of user data.

Don’t store or export these keys. Derive these keys only as the result of an assertion operation, and then discard them when the operation finishes.

## Topics

### Creating an outputs instance
- [init(first: SymmetricKey, second: SymmetricKey?)](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/init(first:second:).md)
  Initializes an object representing the outputs of the web authentication PRF extension.
### Determining PRF support
- [let isSupported: Bool](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/issupported.md)
  A Boolean value that indicates whether the newly created passkey supports the PRF extension.
### Using defined support values
- [static var supported: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/supported.md)
  A Boolean value that indicates the newly created passkey supports the PRF extension.
- [static var unsupported: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/unsupported.md)
  A Boolean value that indicates the newly created passkey doesn’t support the PRF extension.
### Accessing symmetric keys
- [let first: SymmetricKey?](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/first.md)
  A symmetric key that’s unique to the passkey and derives from the first input, if specified.
- [let second: SymmetricKey?](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct/second.md)
  A second symmetric key that’s unique to the passkey, and derives from the second input, if specified.

## See Also

- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput?](aspasskeyregistrationcredentialextensionoutput-swift.struct/largeblob.md)
  The output for a large binary object operation during passkey registration.
- [struct ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput](asauthorizationpublickeycredentiallargeblobregistrationoutput-swift.struct.md)
  The result of the large binary object support check, resulting from a passkey registration response.
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput?](aspasskeyregistrationcredentialextensionoutput-swift.struct/prf.md)
  The outputs of the WebAuthn PRF extension in passkey registration requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfregistrationoutput-swift.struct)*