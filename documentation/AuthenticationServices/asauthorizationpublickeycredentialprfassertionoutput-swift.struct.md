# ASAuthorizationPublicKeyCredentialPRFAssertionOutput

**Framework**: Authentication Services  
**Kind**: struct

A type to represent outputs of the web authentication PRF extension, when requesting them during an assertion.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ASAuthorizationPublicKeyCredentialPRFAssertionOutput
```

#### Overview

This object represents one or two `SymmetricKey` keys that are available anywhere the passkey is available for use. These are general purpose keys that you can use for application-specific needs, such as encryption of user data.

Don’t store or export these keys. Derive these keys only as the result of an assertion operation, and then discard them when the operation finishes.

## Topics

### Creating a PRF assertion output
- [init(first: SymmetricKey, second: SymmetricKey?)](asauthorizationpublickeycredentialprfassertionoutput-swift.struct/init(first:second:).md)
  Initializes an assertion output structure with one or two keys.
### Accessing symmetric keys
- [let first: SymmetricKey](asauthorizationpublickeycredentialprfassertionoutput-swift.struct/first.md)
  A symmetric key that’s unique to the passkey and derives from the first input.
- [let second: SymmetricKey?](asauthorizationpublickeycredentialprfassertionoutput-swift.struct/second.md)
  A second symmetric key that’s unique to the passkey, and derives from the second input, if specified.

## See Also

- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput?](aspasskeyassertioncredentialextensionoutput-swift.struct/largeblob.md)
  The output for a large binary object operation during passkey assertion.
- [struct ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput](asauthorizationpublickeycredentiallargeblobassertionoutput-swift.struct.md)
  A type to represent the output of the requested large binary object operation, which returns in a passkey sign-in response.
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionOutput?](aspasskeyassertioncredentialextensionoutput-swift.struct/prf.md)
  The outputs of the WebAuthn PRF extension in passkey assertion requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertionoutput-swift.struct)*