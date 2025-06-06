# currency

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The currency to use for this disbursement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
var currency: Locale.Currency { get set }
```

#### Discussion

Apple Pay interprets the amounts that this request’s summary items provide as amounts in this currency.

## See Also

- [var region: Locale.Region](pkdisbursementrequest/region.md)
  The geographic region that describes the location for this disbursement.
- [var supportedRegions: [Locale.Region]?](pkdisbursementrequest/supportedregions-1cl0f.md)
  An array of regions that describe the locations to support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/currency)*