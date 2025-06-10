# jsonRepresentation

**Framework**: StoreKit  
**Kind**: property

The JSON representation of the subscription renewal information.

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

The [`jsonRepresentation`](product/subscriptioninfo/renewalinfo/jsonrepresentation.md) is UTF-8 string data that has the same JSON schema as the [`JWSRenewalInfoDecodedPayload`](https://developer.apple.com/documentation/AppStoreServerAPI/JWSRenewalInfoDecodedPayload) object. You can use the JSON data to decode the subscription renewal information into your own data type, or use the [`Product.SubscriptionInfo.RenewalInfo`](product/subscriptioninfo/renewalinfo.md) value and its properties directly.

The JSON Web Signature (JWS) Compact Serialization for the subscription renewal information is available in the [`jwsRepresentation`](verificationresult/jwsrepresentation-178oj.md) property of the [`VerificationResult`](verificationresult.md). The JWS string consists of three Base64URL-encoded components, separated by a period: a header, a payload, and a signature. The [`jsonRepresentation`](transaction/jsonrepresentation.md) is the Base64URL-decoded payload component.

> **Note**:  If you send the subscription renewal information to your server or store it, use the [`jwsRepresentation`](verificationresult/jwsrepresentation-178oj.md) and validate the signature before parsing it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/jsonrepresentation)*