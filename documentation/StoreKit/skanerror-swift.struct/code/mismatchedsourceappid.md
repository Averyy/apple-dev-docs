# SKANError.Code.mismatchedSourceAppId

**Framework**: StoreKit  
**Kind**: case

The source app identifier in the ad impression doesn’t match the app identifier in the source app.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- visionOS 1.0+

## Declaration

```swift
case mismatchedSourceAppId
```

#### Discussion

Check that the [`sourceAppStoreItemIdentifier`](skadimpression/sourceappstoreitemidentifier.md) you provide in the [`SKAdImpression`](skadimpression.md) object matches the app identifier of the app displaying the ad.

## See Also

- [SKANError.Code.adNetworkIdMissing](skanerror-swift.struct/code/adnetworkidmissing.md)
  The ad network identifier in the ad impression doesn’t match the value in the information property list.
- [SKANError.Code.impressionMissingRequiredValue](skanerror-swift.struct/code/impressionmissingrequiredvalue.md)
  A required value is missing from a view-through ad impression.
- [SKANError.Code.impressionNotFound](skanerror-swift.struct/code/impressionnotfound.md)
  The system can’t find the ad impression.
- [SKANError.Code.impressionTooShort](skanerror-swift.struct/code/impressiontooshort.md)
- [SKANError.Code.invalidAdvertisedAppId](skanerror-swift.struct/code/invalidadvertisedappid.md)
  The App Store ID of the advertised app is invalid.
- [SKANError.Code.invalidCampaignId](skanerror-swift.struct/code/invalidcampaignid.md)
  The campaign identifier that you provided is invalid.
- [SKANError.Code.invalidConversionValue](skanerror-swift.struct/code/invalidconversionvalue.md)
  The conversion value is invalid.
- [SKANError.Code.invalidSourceAppId](skanerror-swift.struct/code/invalidsourceappid.md)
  The App Store ID of the app displaying the ad is invalid.
- [SKANError.Code.invalidVersion](skanerror-swift.struct/code/invalidversion.md)
  The SKAdNetwork version number is invalid.
- [SKANError.Code.unknown](skanerror-swift.struct/code/unknown.md)
  An unknown error occurred.
- [SKANError.Code.unsupported](skanerror-swift.struct/code/unsupported.md)
  Your app attempted to use functionality that isn’t supported in the specified version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skanerror-swift.struct/code/mismatchedsourceappid)*