# prf

**Framework**: Authentication Services  
**Kind**: property

The outputs of the WebAuthn PRF extension in passkey registration requests.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var prf: ASAuthorizationPublicKeyCredentialPRFRegistrationOutput? { get }
```

## See Also

- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput?](aspasskeyregistrationcredentialextensionoutput-swift.struct/largeblob.md)
  The output for a large binary object operation during passkey registration.
- [struct ASAuthorizationPublicKeyCredentialLargeBlobRegistrationOutput](asauthorizationpublickeycredentiallargeblobregistrationoutput-swift.struct.md)
  The result of the large binary object support check, resulting from a passkey registration response.
- [struct ASAuthorizationPublicKeyCredentialPRFRegistrationOutput](asauthorizationpublickeycredentialprfregistrationoutput-swift.struct.md)
  A type to represent outputs of the web authentication PRF extension, when requesting them during a registration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyregistrationcredentialextensionoutput-swift.struct/prf)*