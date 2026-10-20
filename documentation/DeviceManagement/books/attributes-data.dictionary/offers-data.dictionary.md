# Books.Attributes.Offers

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- VPP License Management 2.1+

## Declaration

```
object Books.Attributes.Offers
```

## Topics

### Related Objects
- [object Books.Attributes.Offers.Assets](./offers-data.dictionary/assets-data.dictionary.md)
- [object Books.Attributes.Offers.Discounts](./offers-data.dictionary/discounts-data.dictionary.md)
- [object Books.Attributes.Offers.Download](./offers-data.dictionary/download-data.dictionary.md)

## Properties

- `assets` ([Books.Attributes.Offers.Assets])
- `buyParams` (string)
- `currencyCode` (string)
- `discounts` ([Books.Attributes.Offers.Discounts])
- `download` (Books.Attributes.Offers.Download)
- `expectedReleaseDate` (string)
- `offerSummary` (string)
- `price` (number)
- `priceFormatted` (string)
- `pricePerUnit` (number)
- `pricePerUnitFormatted` (string)
- `quantity` (integer)
- `recurringSubscriptionPeriod` (string)
- `type` (string) *(required)*: **Allowed Values**: `anonymousDownload`, `buy`, `complete`, `get`, `preorder`, `preordered`, `purchased`, `radio`, `redownload`, `rent`, `subscribe`, `subscription`, `update`

## See Also

### Related Objects
- [object Books.Attributes.SeriesInfo](./seriesinfo-data.dictionary.md)
- [object Books.Attributes.TaxExclusivePrices](./taxexclusiveprices-data.dictionary.md)
- [object Books.Attributes.UserRating](./userrating-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/books/attributes-data.dictionary/offers-data.dictionary)*