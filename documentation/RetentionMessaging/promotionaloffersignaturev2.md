# promotionalOfferSignatureV2

**Framework**: Retention Messaging API  
**Kind**: typealias

The promotional-offer signature you generate in a JSON Web Signature (JWS) format.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
string promotionalOfferSignatureV2
```

#### Discussion

To provide a promotional-offer retention message, you need to cryptographically sign the offer and include it in the [`promotionalOffer`](promotionaloffer.md) parameter of your [`RealtimeResponseBody`](realtimeresponsebody.md) response.

To generate the promotional-offer signature in a JWS format, see [`Generating JWS to sign App Store requests`](https://developer.apple.com/documentation/StoreKit/generating-jws-to-sign-app-store-requests), and follow the instructions for promotional-offer signatures, including the custom claims.

> ❗ **Important**: The `transactionId` parameter of the signature is required. Use the [`originalTransactionId`](originaltransactionid.md) you receive in [`DecodedRealtimeRequestBody`](decodedrealtimerequestbody.md).

The App Store Server Library provides functions that simplify generating this signature. For more information, see [`Simplifying your implementation by using the App Store Server Library`](https://developer.apple.com/documentation/AppStoreServerAPI/simplifying-your-implementation-by-using-the-app-store-server-library).


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/promotionaloffersignaturev2)*