# CardMetadata

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary  
**Role**: Object

Data about the card, including its expiration date and suffix.

**Availability**:
- App Store Connect API 1.0.10+
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```
object CardMetadata
```

## Properties

- `cardCountry` (string): The 2-letter ISO country code.

  **Maximum Length**: `2`
- `expirationDate` (string): The card’s expiration date.

  **Maximum Length**: `8`
- `fpanSuffix` (string): The last four digits of a card’s number.

  **Maximum Length**: `4`
- `longDescription` (string): The long card description.

  **Maximum Length**: `128`
- `shortDescription` (string): The short card description.

  **Maximum Length**: `64`

## See Also

### Merchant token event retrieval
- [Get Details of a Merchant Token Event](./merchant-token-event-retrieval.md)
  Get the details of a merchant token event after receiving a notification.
- [object MerchantTokenEventResponse](./merchanttokeneventresponse.md)
  A response body that contains information about a life-cycle event for a merchant token.
- [object MerchantTokenMetadata](./merchanttokenmetadata.md)
  The card information related to a merchant token, including its card art and metadata.
- [object CardArt](./cardart.md)
  Data for displaying art to represent a card.
- [object EncryptedTokenMetadata](./encryptedtokenmetadata.md)
  Encrypted data about the merchant token, including its Merchant Payment Account Number (MPAN) and expiration date.
- [object TokenMetadata](./tokenmetadata.md)
  Unencrypted metadata about a merchant token, including its Merchant Payment Account Number (MPAN) and expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/cardmetadata)*