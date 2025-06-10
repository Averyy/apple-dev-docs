# region

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property

The geographic region that describes the location for this disbursement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
var region: Locale.Region { get set }
```

#### Discussion

Set this property to the [`Locale.Region`](https://developer.apple.com/documentation/Foundation/Locale/Region-swift.struct) for the country or region of the merchant’s principal place of business. Consult with your payment service provider (PSP) to determine the appropriate country or region code.

Apple Pay may use the `region` to generate payment and disbursement data that complies with local regulations. For more information on regional compliance, see [`Complying with regional regulations`](complying-with-regional-regulations.md).

## See Also

- [var currency: Locale.Currency](pkdisbursementrequest/currency.md)
  The currency to use for this disbursement.
- [var supportedRegions: [Locale.Region]?](pkdisbursementrequest/supportedregions-1cl0f.md)
  An array of regions that describe the locations to support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdisbursementrequest/region)*