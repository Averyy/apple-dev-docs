# perCredentialInputValues

**Framework**: Authentication Services  
**Kind**: property  
**Role**: Instance Property

A map of credential identifiers to input values for the PRF extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
let perCredentialInputValues: [Data : ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues]?
```

## Discussion

If the user selects a passkey that matches a `credentialID` key in this dictionary, the extension uses the corresponding input values. If the selected passkey doesn’t match, it uses `inputValues` if it’s non-`nil`. Otherwise, no PRF output returns. When this value is nonempty, the request needs to specify `allowedCredentials`.

## See Also

### Accessing per-credential input values
- [static func perCredentialInputValues([Data : ASAuthorizationPublicKeyCredentialPRFAssertionInput.InputValues]) -> ASAuthorizationPublicKeyCredentialPRFAssertionInput](./percredentialinputvalues%28_%29.md)
  The inputs for the PRF extension, when not specifying general input values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationpublickeycredentialprfassertioninput-swift.struct/percredentialinputvalues)*