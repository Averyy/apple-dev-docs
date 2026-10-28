# supportedRegions

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

An array of two-letter region codes that describes the regions to support.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy, nullable) NSArray<NSString *> * supportedRegions;
```

## Discussion

If you provide this array, the system filters the selectable payment passes to those the payment service providers (PSP) issued in the supported regions. Indicate the supported countries or regions by using [ISO 3166](https://www.iso.org/iso-3166-country-codes.html) country codes.

The ordering of the elements you provide doesn’t affect the filtering of the cards. For example, debit cards may expect transactions only in the country or region of issuance for the card.

The supported countries or regions list doesn’t affect the currency of the transaction.

For more information on region codes, see [ISO 3166 region codes](https://www.iso.org/iso-3166-country-codes.html).

## See Also

### Setting currency and region information
- [currencyCode](./currencycode.md)
  The currency code string for this disbursement.
- [regionCode](./regioncode.md)
  The merchant’s country code string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/supportedregions-j9ug)*