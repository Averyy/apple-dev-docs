# ASPasskeyRegistrationCredentialExtensionOutput

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
struct ASPasskeyRegistrationCredentialExtensionOutput
```

## Topics

### Creating an extension output instance
- [init(largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput?, prf: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput?)](aspasskeyregistrationcredentialextensionoutput-swift.struct/init(largeblob:prf:).md)
  Creates an extension output instance.
### Inspecting properties
- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput?](aspasskeyregistrationcredentialextensionoutput-swift.struct/largeblob.md)
  The output for a large binary object operation during passkey registration.
- [struct ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput](asauthorizationpublickeycredentiallargeblobregistrationoutput-swift.struct.md)
  The result of the large binary object support check, resulting from a passkey registration response.
- [var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput?](aspasskeyregistrationcredentialextensionoutput-swift.struct/prf.md)
  The outputs of the WebAuthn PRF extension in passkey registration requests.
- [struct ASAuthorizationPublicKeyCredentialPRFRegistrationOutput](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct.md)
  A type to represent outputs of the web authentication PRF extension, when requesting them during a registration.

## See Also

- [var extensionOutput: ASPasskeyRegistrationCredentialExtensionOutput?](aspasskeyregistrationcredential/extensionoutput-2lf9m.md)
  An output from WebAuthn extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredentialextensionoutput-swift.struct)*