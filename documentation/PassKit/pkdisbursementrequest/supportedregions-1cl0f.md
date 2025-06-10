# supportedRegions

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

An array of regions that describe the locations to support.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
var supportedRegions: [Locale.Region]? { get set }
```

#### Discussion

If you provide this array, the system filters the selectable payment passes to those the payment service providers (PSP) issued in the supported regions. Indicate the supported countries or regions by using [`Locale.Region`](https://developer.apple.com/documentation/Foundation/Locale/Region-swift.struct) structures that represent the [`ISO 3166`](https://developer.apple.comhttps://www.iso.org/iso-3166-country-codes.html) country codes to filter.

The ordering of the elements you provide doesn’t affect the filtering of the cards. For example, debit cards may expect transactions only in the country or region of issuance for the card.

The supported countries or regions list doesn’t affect the currency of the transaction.

For more information on region codes, see [`ISO 3166`](https://developer.apple.comhttps://www.iso.org/iso-3166-country-codes.html).

## See Also

- [var currency: Locale.Currency](pkdisbursementrequest/currency.md)
  The currency to use for this disbursement.
- [var region: Locale.Region](pkdisbursementrequest/region.md)
  The geographic region that describes the location for this disbursement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/supportedregions-1cl0f)*