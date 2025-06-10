# SKANError

**Framework**: StoreKit  
**Kind**: struct

An error that an ad network attribution operation returns.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- visionOS 1.0+

## Declaration

```swift
struct SKANError
```

## Topics

### Getting Error Codes
- [static var adNetworkIdMissing: SKANError.Code](skanerror-swift.struct/adnetworkidmissing.md)
  The ad network identifier in the ad impression doesn’t match the value in the information property list.
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
### Type Properties
- [static var errorDomain: String](skanerror-swift.struct/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let SKANErrorDomain: String](skanerrordomain.md)
  A string that identifies the SKAdNetwork error domain.
- [SKANError.Code](skanerror-swift.struct/code.md)
  Constants that indicate the type of error for an ad network attribution operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skanerror-swift.struct)*