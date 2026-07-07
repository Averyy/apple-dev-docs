# jsonRepresentation

**Framework**: StoreKit  
**Kind**: property

The JSON representation of the transaction information.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var jsonRepresentation: Data { get }
```

#### Discussion

The [`jsonRepresentation`](transaction/jsonrepresentation.md) is UTF-8 string data that has the same JSON schema as the [`JWSTransactionDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSTransactionDecodedPayload) object. You can use this data to decode the transaction information into your own data type instead of using the [`Transaction`](transaction.md) value and its [`Transaction properties`](transaction-properties.md) directly.

The JSON Web Signature (JWS) Compact Serialization for the transaction is available in the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) property of the [`VerificationResult`](verificationresult.md). The JWS string consists of three Base64URL-encoded components, separated by a period: a header, a payload, and a signature. The [`jsonRepresentation`](transaction/jsonrepresentation.md) is the Base64URL-decoded payload component.

> **Note**:  If you send the transaction to your server or store it, use the [`jwsRepresentation`](verificationresult/jwsrepresentation-21vgo.md) and validate the signature before parsing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/jsonrepresentation)*