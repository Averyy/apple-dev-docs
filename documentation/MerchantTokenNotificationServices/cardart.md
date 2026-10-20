# CardArt

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary  
**Role**: Object

Data for displaying art to represent a card.

**Availability**:
- App Store Connect API 1.0.10+
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```
object CardArt
```

## Properties

- `name` (string) *(required)*: A name representing the bank and the card used for the transaction.

  **Minimum Length**: `1`; **Maximum Length**: `64`
- `type` (string) *(required)*: The card type.

  **Minimum Length**: `1`; **Maximum Length**: `64`
- `url` (string) *(required)*: The URL for downloading the card art, as provided by the issuing bank.

  **Minimum Length**: `1`; **Maximum Length**: `128`

## See Also

### Merchant token event retrieval
- [Get Details of a Merchant Token Event](./merchant-token-event-retrieval.md)
  Get the details of a merchant token event after receiving a notification.
- [object MerchantTokenEventResponse](./merchanttokeneventresponse.md)
  A response body that contains information about a life-cycle event for a merchant token.
- [object MerchantTokenMetadata](./merchanttokenmetadata.md)
  The card information related to a merchant token, including its card art and metadata.
- [object CardMetadata](./cardmetadata.md)
  Data about the card, including its expiration date and suffix.
- [object EncryptedTokenMetadata](./encryptedtokenmetadata.md)
  Encrypted data about the merchant token, including its Merchant Payment Account Number (MPAN) and expiration date.
- [object TokenMetadata](./tokenmetadata.md)
  Unencrypted metadata about a merchant token, including its Merchant Payment Account Number (MPAN) and expiration date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/cardart)*