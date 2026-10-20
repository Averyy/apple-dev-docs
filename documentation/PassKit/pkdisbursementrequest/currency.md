# currency

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

The currency to use for this disbursement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS

## Declaration

```swift
var currency: Locale.Currency { get set }
```

#### Discussion

Apple Pay interprets the amounts that this request’s summary items provide as amounts in this currency.

## See Also

### Setting currency and region information
- [var region: Locale.Region](./region.md)
  The geographic region that describes the location for this disbursement.
- [var supportedRegions: [Locale.Region]?](./supportedregions-1cl0f.md)
  An array of regions that describe the locations to support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/currency)*