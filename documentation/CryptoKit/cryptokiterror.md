# CryptoKitError

**Framework**: Apple CryptoKit  
**Kind**: enum

General cryptography errors used by CryptoKit.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum CryptoKitError
```

## Topics

### Reporting errors
- [CryptoKitError.incorrectKeySize](cryptokiterror/incorrectkeysize.md)
  The key size is incorrect.
- [CryptoKitError.invalidParameter](cryptokiterror/invalidparameter.md)
  The parameter is invalid.
- [CryptoKitError.incorrectParameterSize](cryptokiterror/incorrectparametersize.md)
  The parameter size is incorrect.
- [CryptoKitError.underlyingCoreCryptoError(error:)](cryptokiterror/underlyingcorecryptoerror(error:).md)
  The underlying corecrypto library is unable to complete the requested action.
- [CryptoKitError.authenticationFailure](cryptokiterror/authenticationfailure.md)
  The authentication tag or signature is incorrect.
- [CryptoKitError.wrapFailure](cryptokiterror/wrapfailure.md)
  The framework can’t wrap the specified key.
- [CryptoKitError.unwrapFailure](cryptokiterror/unwrapfailure.md)
  The framework can’t unwrap the specified key.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [enum CryptoKitASN1Error](cryptokitasn1error.md)
  Errors from decoding ASN.1 content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cryptokit/cryptokiterror)*