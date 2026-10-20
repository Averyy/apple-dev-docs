# SKANError.Code.impressionMissingRequiredValue

**Framework**: StoreKit  
**Kind**: case  
**Role**: Case

A required value is missing from a view-through ad impression.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- visionOS 1.0+

## Declaration

```swift
case impressionMissingRequiredValue
```

```c
SKANErrorImpressionMissingRequiredValue
```

#### Discussion

Check that your instance of [`SKAdImpression`](../../skadimpression.md) provides all of the required values.

## See Also

### Error Codes
- [SKANError.Code.adNetworkIdMissing](./adnetworkidmissing.md)
  The ad network identifier in the ad impression doesn’t match the value in the information property list.
- [SKANError.Code.impressionNotFound](./impressionnotfound.md)
  The system can’t find the ad impression.
- [SKANError.Code.impressionTooShort](./impressiontooshort.md)
- [SKANError.Code.invalidAdvertisedAppId](./invalidadvertisedappid.md)
  The App Store ID of the advertised app is invalid.
- [SKANError.Code.invalidCampaignId](./invalidcampaignid.md)
  The campaign identifier that you provided is invalid.
- [SKANError.Code.invalidConversionValue](./invalidconversionvalue.md)
  The conversion value is invalid.
- [SKANError.Code.invalidSourceAppId](./invalidsourceappid.md)
  The App Store ID of the app displaying the ad is invalid.
- [SKANError.Code.invalidVersion](./invalidversion.md)
  The SKAdNetwork version number is invalid.
- [SKANError.Code.mismatchedSourceAppId](./mismatchedsourceappid.md)
  The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [SKANError.Code.unknown](./unknown.md)
  An unknown error occurred.
- [SKANError.Code.unsupported](./unsupported.md)
  Your app attempted to use functionality that isn’t supported in the specified version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skanerror-swift.struct/code/impressionmissingrequiredvalue)*