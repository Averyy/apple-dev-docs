# ASPasskeyAssertionCredentialExtensionInput

**Framework**: Authentication Services  
**Kind**: struct

A type that encapsulates input for various WebAuthn extensions during passkey assertion.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ASPasskeyAssertionCredentialExtensionInput
```

## Topics

### Creating an assertion input
- [init(largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput?, prf: ASAuthorizationPublicKeyCredentialPRFAssertionInput?)](aspasskeyassertioncredentialextensioninput-swift.struct/init(largeblob:prf:).md)
  Creates a passkey assertion input.
- [struct ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput](asauthorizationpublickeycredentiallargeblobassertioninput-swift.struct.md)
  A type that represents input for the binary large object extension in passkey assertion requests.
- [struct ASAuthorizationPublicKeyCredentialPRFAssertionInput](asauthorizationpublickeycredentialprfassertioninput-swift.struct.md)
  A type that represents input for the web authentication PRF extension in passkey assertion requests.
### Using inputs
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput?](aspasskeyassertioncredentialextensioninput-swift.struct/largeblob.md)
  Input for the WebAuthn large binary object extension in passkey assertion requests.
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionInput?](aspasskeyassertioncredentialextensioninput-swift.struct/prf.md)
  Input for the WebAuthn PRF extension in passkey assertion requests.

## See Also

- [var extensionInput: ASPasskeyAssertionCredentialExtensionInput?](aspasskeycredentialrequestparameters/extensioninput-2edlv.md)
  An input for WebAuthn extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredentialextensioninput-swift.struct)*