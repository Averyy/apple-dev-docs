# Album.Prices.Price

**Framework**: Apple Music Feed  
**Kind**: dictionary

Information about a pricing offer.

**Availability**:
- AppleMusicFeed 1.0+

## Declaration

```swift
object Album.Prices.Price
```

#### Discussion

See the [`Album.Prices`](album/prices-data.dictionary.md) data example.

## Properties

- `currencyCode` (string): The currency for the offer in ISO 4217 format.
- `price` (number): The price for the offer.
- `priceType` (string): The type of content availability for the offer. The possible values are `buy`, `streaming`, and `preorder`.
- `quality` (string): The audio quality for the offer. The possible values are `standard-definition` and `high-definition`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applemusicfeed/album/prices-data.dictionary/price)*