# MerchantTokenEventResponse

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary  
**Role**: Object

A response body that contains information about a life-cycle event for a merchant token.

**Availability**:
- App Store Connect API 1.0.10+
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```
object MerchantTokenEventResponse
```

## Properties

- `eventType` (string) *(required)*: A field that indicates the type of event for this notification.

  **Maximum Length**: `64`; **Allowed Values**: `UNLINK`, `UPDATED_METADATA`, `UPDATED_CARD_ART`, `UPDATED_MERCHANT_TOKEN_PUBLIC_KEY`, `UPDATED_MERCHANT_TOKEN`
- `merchantTokenIdentifier` (string) *(required)*: The unique identifier of the merchant token.

  **Maximum Length**: `64`
- `merchantTokenMetadata` (MerchantTokenMetadata): Data about the card, including its expiration date and suffix.
- `reason` (string) *(required)*: A string that indicates who originated the token event,  either the user or the card issuer.

  **Maximum Length**: `256`

## See Also

### Merchant token event retrieval
- [Get Details of a Merchant Token Event](./merchant-token-event-retrieval.md)
  Get the details of a merchant token event after receiving a notification.
- [object MerchantTokenMetadata](./merchanttokenmetadata.md)
  The card information related to a merchant token, including its card art and metadata.
- [object CardArt](./cardart.md)
  Data for displaying art to represent a card.
- [object CardMetadata](./cardmetadata.md)
  Data about the card, including its expiration date and suffix.
- [object EncryptedTokenMetadata](./encryptedtokenmetadata.md)
  Encrypted data about the merchant token, including its Merchant Payment Account Number (MPAN) and expiration date.
- [object TokenMetadata](./tokenmetadata.md)
  Unencrypted metadata about a merchant token, including its Merchant Payment Account Number (MPAN) and expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokeneventresponse)*