# ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput

**Framework**: Authentication Services  
**Kind**: struct

A type that represents input for the binary large object extension in passkey assertion requests.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput
```

#### Overview

Use this type during assertion (sign-in) with an existing passkey. An app can specify exactly one operation to perform during the sign-in: either read the existing saved blob or write a new blob (overwriting the existing one, if applicable). This restriction mirrors the operations available in the WebAuthn specification.

## Topics

### Using assertion inputs
- [static var read: ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput](asauthorizationpublickeycredentiallargeblobassertioninput-swift.struct/read.md)
  An operation to read the existing blob value.
- [static func write(Data) -> ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput](asauthorizationpublickeycredentiallargeblobassertioninput-swift.struct/write(_:).md)
  An operation to write the blob value, overwriting any existing value.
### Inspecting the operation
- [var operation: ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput.Operation](asauthorizationpublickeycredentiallargeblobassertioninput-swift.struct/operation-swift.property.md)
  The reading or writing operation the input performs.
- [ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput.Operation](asauthorizationpublickeycredentiallargeblobassertioninput-swift.struct/operation-swift.enum.md)
  A type to represent the possible operations of a large binary object assertion input.

## See Also

- [init(largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput?, prf: ASAuthorizationPublicKeyCredentialPRFAssertionInput?)](aspasskeyassertioncredentialextensioninput-swift.struct/init(largeblob:prf:).md)
  Creates a passkey assertion input.
- [struct ASAuthorizationPublicKeyCredentialPRFAssertionInput](asauthorizationpublickeycredentialprfassertioninput-swift.struct.md)
  A type that represents input for the web authentication PRF extension in passkey assertion requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentiallargeblobassertioninput-swift.struct)*