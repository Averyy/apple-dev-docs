# ASAuthorizationPublicKeyCredentialPRFAssertionInput

**Framework**: Authentication Services  
**Kind**: struct

A type that represents input for the web authentication PRF extension in passkey assertion requests.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct ASAuthorizationPublicKeyCredentialPRFAssertionInput
```

#### Overview

The PRF extension lets you create general purpose `SymmetricKey` keys from passkeys, which can be useful for tasks like encryption of user data. Using the same input values with the same passkey produces the same `SymmetricKey`.

## Topics

### Accessing input values
- [let inputValues: ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues?](asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.property.md)
  The input values to use when generating the PRF extension output, if specified.
- [static func inputValues(ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues, perCredentialInputValues: [Data : ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues]?) -> ASAuthorizationPublicKeyCredentialPRFAssertionInput](asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues(_:percredentialinputvalues:).md)
  The inputs for the PRF extension.
### Accessing per-credential input values
- [let perCredentialInputValues: [Data : ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues]?](asauthorizationpublickeycredentialprfassertioninput-swift.struct/percredentialinputvalues.md)
  A map of credential identifiers to input values for the PRF extension.
- [static func perCredentialInputValues([Data : ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues]) -> ASAuthorizationPublicKeyCredentialPRFAssertionInput](asauthorizationpublickeycredentialprfassertioninput-swift.struct/percredentialinputvalues(_:).md)
  The inputs for the PRF extension, when not specifying general input values.
### Supporting types
- [ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues](asauthorizationpublickeycredentialprfassertioninput-swift.struct/inputvalues-swift.struct.md)
  The values to use as inputs to the salts for deriving the symmetric key.

## See Also

- [init(largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput?, prf: ASAuthorizationPublicKeyCredentialPRFAssertionInput?)](aspasskeyassertioncredentialextensioninput-swift.struct/init(largeblob:prf:).md)
  Creates a passkey assertion input.
- [struct ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput](asauthorizationpublickeycredentiallargeblobassertioninput-swift.struct.md)
  A type that represents input for the binary large object extension in passkey assertion requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct)*