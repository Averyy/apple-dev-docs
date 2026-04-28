# MerchantTokenMetadata

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary

The card information related to a merchant token, including its card art and metadata.

**Availability**:
- App Store Connect API 1.0.10+
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```swift
object MerchantTokenMetadata
```

## Properties

- `cardArt` ([CardArt]): An array that contains data you use to display art that represents the card related to the merchant token.
- `cardMetadata` (CardMetadata): Card data, including its expiration date and suffix, for the card related to the merchant token.

## See Also

- [Get Details of a Merchant Token Event](merchant-token-event-retrieval.md)
  Get the details of a merchant token event after receiving a notification.
- [object MerchantTokenEventResponse](merchanttokeneventresponse.md)
  A response body that contains information about a life-cycle event for a merchant token.
- [object CardArt](cardart.md)
  Data for displaying art to represent a card.
- [object CardMetadata](cardmetadata.md)
  Data about the card, including its expiration date and suffix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenmetadata)*