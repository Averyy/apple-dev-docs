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

## Properties

- `encodedSignature` (string): **(Required)** The Base64-encoded cryptographic signature you generate using the offer parameters.
- `productId` (productId): **(Required)** The subscription’s product identifier.
- `nonce` (uuid): **(Required)** A one-time-use UUID antireplay value you generate. Use lowercase.
- `timestamp` (timestamp): **(Required)** The UNIX time, in milliseconds, when you generate the signature.
- `keyId` (string): **(Required)** A string that identifies the private key you use to generate the signature. You can find this identifier in App Store Connect Users and Access > Keys in the Key ID column for the subscription key you generate.
- `offerIdentifier` (string): **(Required)** The subscription offer identifier that you set up in App Store Connect.
- `appAccountToken` (uuid): A UUID that you provide to associate with the transaction if the customer accepts the promotional offer. The string representation of the `appAccountToken` needs to be lowercase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/retentionmessaging/promotionaloffersignaturev1)*