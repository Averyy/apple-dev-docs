# prf

**Framework**: Authentication Services  
**Kind**: property

The outputs of the WebAuthn PRF extension in passkey assertion requests.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var prf: ASAuthorizationPublicKeyCredentialPRFAssertionOutput? { get }
```

## See Also

- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput?](aspasskeyassertioncredentialextensionoutput-swift.struct/largeblob.md)
  The output for a large binary object operation during passkey assertion.
- [struct ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput](asauthorizationpublickeycredentiallargeblobassertionoutput-swift.struct.md)
  A type to represent the output of the requested large binary object operation, which returns in a passkey sign-in response.
- [struct ASAuthorizationPublicKeyCredentialPRFAssertionOutput](asauthorizationpublickeycredentialprfassertionoutput-swift.struct.md)
  A type to represent outputs of the web authentication PRF extension, when requesting them during an assertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredentialextensionoutput-swift.struct/prf)*