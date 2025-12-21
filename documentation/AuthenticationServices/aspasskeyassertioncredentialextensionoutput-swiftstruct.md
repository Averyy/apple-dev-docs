# ASPasskeyAssertionCredentialExtensionOutput

**Framework**: Authentication Services  
**Kind**: struct

A type that encapsulates output for various WebAuthn extensions during passkey assertion.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ASPasskeyAssertionCredentialExtensionOutput
```

## Topics

### Creating an extension output instance
- [init(largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput?, prf: ASAuthorizationPublicKeyCredentialPRFAssertionOutput?)](aspasskeyassertioncredentialextensionoutput-swift.struct/init(largeblob:prf:).md)
  Creates an extension output instance.
### Inspecting properties
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput?](aspasskeyassertioncredentialextensionoutput-swift.struct/largeblob.md)
  The output for a large binary object operation during passkey assertion.
- [struct ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput](asauthorizationpublickeycredentiallargeblobassertionoutput-swift.struct.md)
  A type to represent the output of the requested large binary object operation, which returns in a passkey sign-in response.
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionOutput?](aspasskeyassertioncredentialextensionoutput-swift.struct/prf.md)
  The outputs of the WebAuthn PRF extension in passkey assertion requests.
- [struct ASAuthorizationPublicKeyCredentialPRFAssertionOutput](asauthorizationpublickeycredentialprfassertionoutput-swift.struct.md)
  A type to represent outputs of the web authentication PRF extension, when requesting them during an assertion.

## See Also

- [var extensionOutput: ASPasskeyAssertionCredentialExtensionOutput?](aspasskeyassertioncredential/extensionoutput-7t6rn.md)
  An output from WebAuthn extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredentialextensionoutput-swift.struct)*