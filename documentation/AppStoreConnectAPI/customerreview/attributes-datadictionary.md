# CustomerReview.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

The attributes of the customer’s review including its content.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object CustomerReview.Attributes
```

## Topics

### Types
- [type TerritoryCode](territorycode.md)
  The App Store territory codes.

## Properties

- `body` (string): The review text that the customer wrote.
- `createdDate` (date-time): The date and time the customer created the review.
- `rating` (integer): The rating the customer provided.
- `reviewerNickname` (string): The customer’s nickname used in the review.
- `title` (string): The title that the customer wrote for the review.
- `territory` (TerritoryCode): The App Store territory.

## See Also

- [object CustomerReview.Relationships](customerreview/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/customerreview/attributes-data.dictionary)*