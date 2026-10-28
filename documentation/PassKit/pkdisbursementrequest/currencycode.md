# currencyCode

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The currency code string for this disbursement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, copy) NSString * currencyCode;
```

## Discussion

Apple Pay interprets the amounts that this request’s summary items provide as amounts in this currency. For more information on currency codes, see [ISO 4127 Currency Codes](https://www.iso.org/iso-4217-currency-codes.html).

## See Also

### Setting currency and region information
- [regionCode](./regioncode.md)
  The merchant’s country code string.
- [supportedRegions](./supportedregions-j9ug.md)
  An array of two-letter region codes that describes the regions to support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/currencycode)*