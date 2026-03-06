# CardArt

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary

Data for displaying art to represent a card.

**Availability**:
- App Store Connect API 1.0.10+

## Declaration

```swift
object CardArt
```

## Properties

- `name` (string) *(required)*: A name representing the bank and the card used for the transaction.
- `type` (string) *(required)*: The card type.
- `url` (string) *(required)*: The URL for downloading the card art, as provided by the issuing bank.

## See Also

- [Get Details of a Merchant Token Event](merchant-token-event-retrieval.md)
  Get the details of a merchant token event after receiving a notification.
- [object MerchantTokenEventResponse](merchanttokeneventresponse.md)
  A response body that contains information about a life-cycle event for a merchant token.
- [object MerchantTokenMetadata](merchanttokenmetadata.md)
  The card information related to a merchant token, including its card art and metadata.
- [object CardMetadata](cardmetadata.md)
  Data about the card, including its expiration date and suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/cardart)*