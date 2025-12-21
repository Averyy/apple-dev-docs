# promotionalOfferSignatureV1

**Framework**: Retention Messaging API  
**Kind**: dictionary

The promotional offer signature you generate using an earlier signature version.

**Availability**:
- Retention Messaging API 1.0+

## Declaration

```swift
object promotionalOfferSignatureV1
```

#### Discussion

To provide a promotional-offer retention message, you need to cryptographically sign the offer and include it in the [`promotionalOffer`](promotionaloffer.md) parameter of your [`RealtimeResponseBody`](realtimeresponsebody.md) response.

> 💡 **Tip**: For a simpler implementation, use [`promotionalOfferSignatureV2`](promotionaloffersignaturev2.md) instead.

For instructions on generating the `encodedSignature` for the `promotionalOfferSignatureV1`, see [`Generating a signature for promotional offers`](https://developer.apple.com/documentation/StoreKit/generating-a-signature-for-promotional-offers).


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/promotionaloffersignaturev1)*