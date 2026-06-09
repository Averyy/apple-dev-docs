# Books.Attributes

**Framework**: Device Management  
**Kind**: dictionary

The attributes for a books resource.

**Availability**:
- VPP License Management 2.1+

## Declaration

```swift
object Books.Attributes
```

## Topics

### Related Objects
- [object Books.Attributes.Offers](books/attributes-data.dictionary/offers-data.dictionary.md)
- [object Books.Attributes.SeriesInfo](books/attributes-data.dictionary/seriesinfo-data.dictionary.md)
- [object Books.Attributes.TaxExclusivePrices](books/attributes-data.dictionary/taxexclusiveprices-data.dictionary.md)
- [object Books.Attributes.UserRating](books/attributes-data.dictionary/userrating-data.dictionary.md)

## Properties

- `artistName` (string) *(required)*: The name of the artist for this content.
- `artwork` (Artwork) *(required)*: The artwork for this content.
- `genreNames` ([string]) *(required)*: A list of genre names associated with this content.
- `isbn` (string): The ISBN of this book.
- `name` (string) *(required)*: The (potentially) censored name of the content.
- `offers` ([Books.Attributes.Offers]) *(required)*: A map of offer and asset information for the associated content.
- `seriesInfo` (Books.Attributes.SeriesInfo): Info about the series this book is a part of.
- `taxExclusivePrices` ([Books.Attributes.TaxExclusivePrices]): **(Personalized)** Tax-exclusive prices for this salable.
- `taxRate` (number): **(Personalized)** Tax rate for this salable for the current account.
- `url` (string) *(required)*: A canonical URL to the content that may be used for sharing or linking to the content externally.
- `userRating` (Books.Attributes.UserRating) *(required)*: User rating information for the content.

## See Also

- [object Books.Relationships](books/relationships-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/books/attributes-data.dictionary)*