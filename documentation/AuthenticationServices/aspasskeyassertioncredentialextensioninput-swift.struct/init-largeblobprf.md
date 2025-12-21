# init(largeBlob:prf:)

**Framework**: Authentication Services  
**Kind**: init

Creates a passkey assertion input.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
init(largeBlob: ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput? = nil, prf: ASAuthorizationPublicKeyCredentialPRFAssertionInput? = nil)
```

## Parameters

- `largeBlob`: Input for the WebAuthn   extension.
- `prf`: Input for the WebAuthn PRF extension.

## See Also

- [struct ASAuthorizationPublicKeyCredentialLargeBlobAssertionInput](asauthorizationpublickeycredentiallargeblobassertioninput-swift.struct.md)
  A type that represents input for the binary large object extension in passkey assertion requests.
- [struct ASAuthorizationPublicKeyCredentialPRFAssertionInput](asauthorizationpublickeycredentialprfassertioninput-swift.struct.md)
  A type that represents input for the web authentication PRF extension in passkey assertion requests.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/aspasskeyassertioncredentialextensioninput-swift.struct/init(largeblob:prf:))*