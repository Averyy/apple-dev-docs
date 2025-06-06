# adNetworkIdMissing

**Framework**: StoreKit  
**Kind**: property

The ad network identifier in the ad impression doesn’t match the value in the information property list.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- visionOS 1.0+

## Declaration

```swift
static var adNetworkIdMissing: SKANError.Code { get }
```

#### Discussion

The value you specify for your ad network identifier in your ad impresion must match the value in the `Info.plist`. ``An app that participates in ad campaigns by displaying ads must include the ad network identifiers in its `Info.plist`. For more information, see [`Configuring a source app`](configuring-a-source-app.md).

## See Also

- [static var impressionMissingRequiredValue: SKANError.Code](skanerror-swift.struct/impressionmissingrequiredvalue.md)
  A required value is missing from a view-through ad impression.
- [static var impressionNotFound: SKANError.Code](skanerror-swift.struct/impressionnotfound.md)
  The system can’t find the ad impression.
- [static var impressionTooShort: SKANError.Code](skanerror-swift.struct/impressiontooshort.md)
- [static var invalidAdvertisedAppId: SKANError.Code](skanerror-swift.struct/invalidadvertisedappid.md)
  The App Store ID of the advertised app is invalid.
- [static var invalidCampaignId: SKANError.Code](skanerror-swift.struct/invalidcampaignid.md)
  The campaign identifier that you provided is invalid.
- [static var invalidConversionValue: SKANError.Code](skanerror-swift.struct/invalidconversionvalue.md)
  The conversion value is invalid.
- [static var invalidSourceAppId: SKANError.Code](skanerror-swift.struct/invalidsourceappid.md)
  The App Store ID of the app displaying the ad is invalid.
- [static var invalidVersion: SKANError.Code](skanerror-swift.struct/invalidversion.md)
  The SKAdNetwork version number is invalid.
- [static var mismatchedSourceAppId: SKANError.Code](skanerror-swift.struct/mismatchedsourceappid.md)
  The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [static var unknown: SKANError.Code](skanerror-swift.struct/unknown.md)
  An unknown error occurred.
- [static var unsupported: SKANError.Code](skanerror-swift.struct/unsupported.md)
  Your app attempted to use functionality that isn’t supported in the specified version.
- [SKANError.Code](skanerror-swift.struct/code.md)
  Constants that indicate the type of error for an ad network attribution operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skanerror-swift.struct/adnetworkidmissing)*