# ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput

**Framework**: Authentication Services  
**Kind**: struct

A type to represent the output of the requested large binary object operation, which returns in a passkey sign-in response.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput
```

#### Overview

For a read operation, this type contains the saved blob, if one is present and the read succeeds. For a write operation, this type indicates whether the write succeeds.

## Topics

### Inspecting the result
- [var result: ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput.OperationResult](asauthorizationpublickeycredentiallargeblobassertionoutput-swift.struct/result.md)
  The result of the requested large binary object operation.
- [ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput.OperationResult](asauthorizationpublickeycredentiallargeblobassertionoutput-swift.struct/operationresult.md)
  A type that represents the result of the requested binary large object operation.
### Type Methods
- [static func read(data: Data?) -> ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput](asauthorizationpublickeycredentiallargeblobassertionoutput-swift.struct/read(data:).md)
- [static func write(success: Bool) -> ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput](asauthorizationpublickeycredentiallargeblobassertionoutput-swift.struct/write(success:).md)

## See Also

- [var largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionOutput?](aspasskeyassertioncredentialextensionoutput-swift.struct/largeblob.md)
  The output for a large binary object operation during passkey assertion.
- [var prf: ASAuthorizationPublicKeyCredentialPRFAssertionOutput?](aspasskeyassertioncredentialextensionoutput-swift.struct/prf.md)
  The outputs of the WebAuthn PRF extension in passkey assertion requests.
- [struct ASAuthorizationPublicKeyCredentialPRFAssertionOutput](asauthorizationpublickeycredentialprfassertionoutput-swift.struct.md)
  A type to represent outputs of the web authentication PRF extension, when requesting them during an assertion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentiallargeblobassertionoutput-swift.struct)*