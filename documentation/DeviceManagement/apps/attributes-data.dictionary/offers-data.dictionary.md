# Apps.Attributes.Offers

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- VPP License Management 2.1+

## Declaration

```
object Apps.Attributes.Offers
```

## Topics

### Related Objects
- [object Apps.Attributes.Offers.Assets](./offers-data.dictionary/assets-data.dictionary.md)
- [object Apps.Attributes.Offers.Discounts](./offers-data.dictionary/discounts-data.dictionary.md)
- [object Apps.Attributes.Offers.Download](./offers-data.dictionary/download-data.dictionary.md)

## Properties

- `assets` ([Apps.Attributes.Offers.Assets])
- `buyParams` (string)
- `currencyCode` (string)
- `discounts` ([Apps.Attributes.Offers.Discounts])
- `download` (Apps.Attributes.Offers.Download)
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
- [object Apps.Attributes.ContentRatingsBySystem](./contentratingsbysystem-data.dictionary.md)
- [object Apps.Attributes.FileSizeByDevice](./filesizebydevice-data.dictionary.md)
- [object Apps.Attributes.LatestVersionInfo](./latestversioninfo-data.dictionary.md)
- [object Apps.Attributes.RequirementsByDeviceFamily](./requirementsbydevicefamily-data.dictionary.md)
- [object Apps.Attributes.ScreenshotsByType](./screenshotsbytype-data.dictionary.md)
- [object Apps.Attributes.TaxExclusivePrices](./taxexclusiveprices-data.dictionary.md)
- [object Apps.Attributes.UserRating](./userrating-data.dictionary.md)
- [object Apps.Attributes.VersionHistory](./versionhistory-data.dictionary.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/apps/attributes-data.dictionary/offers-data.dictionary)*