# unsupported

**Framework**: StoreKit  
**Kind**: property  
**Role**: Type Property

Your app attempted to use functionality that isn’t supported in the specified version.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- visionOS 1.0+

## Declaration

```swift
static var unsupported: SKANError.Code { get }
```

## Discussion

For information about supported features by version number, see [SKAdNetwork release notes](../skadnetwork-release-notes.md). For example, to provide view-through ads, use SKAdNetwork version 2.2 or later.

## See Also

### Getting Error Codes
- [static var adNetworkIdMissing: SKANError.Code](./adnetworkidmissing.md)
  The ad network identifier in the ad impression doesn’t match the value in the information property list.
- [static var impressionMissingRequiredValue: SKANError.Code](./impressionmissingrequiredvalue.md)
  A required value is missing from a view-through ad impression.
- [static var impressionNotFound: SKANError.Code](./impressionnotfound.md)
  The system can’t find the ad impression.
- [static var impressionTooShort: SKANError.Code](./impressiontooshort.md)
- [static var invalidAdvertisedAppId: SKANError.Code](./invalidadvertisedappid.md)
  The App Store ID of the advertised app is invalid.
- [static var invalidCampaignId: SKANError.Code](./invalidcampaignid.md)
  The campaign identifier that you provided is invalid.
- [static var invalidConversionValue: SKANError.Code](./invalidconversionvalue.md)
  The conversion value is invalid.
- [static var invalidSourceAppId: SKANError.Code](./invalidsourceappid.md)
  The App Store ID of the app displaying the ad is invalid.
- [static var invalidVersion: SKANError.Code](./invalidversion.md)
  The SKAdNetwork version number is invalid.
- [static var mismatchedSourceAppId: SKANError.Code](./mismatchedsourceappid.md)
  The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [static var unknown: SKANError.Code](./unknown.md)
  An unknown error occurred.
- [SKANError.Code](./code.md)
  Constants that indicate the type of error for an ad network attribution operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skanerror-swift.struct/unsupported)*