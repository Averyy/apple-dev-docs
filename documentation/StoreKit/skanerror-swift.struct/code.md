# SKANError.Code

**Framework**: StoreKit  
**Kind**: enum

Constants that indicate the type of error for an ad network attribution operation.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error Codes
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
- [SKANError.Code.mismatchedSourceAppId](skanerror-swift.struct/code/mismatchedsourceappid.md)
  The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [SKANError.Code.unknown](skanerror-swift.struct/code/unknown.md)
  An unknown error occurred.
- [SKANError.Code.unsupported](skanerror-swift.struct/code/unsupported.md)
  Your app attempted to use functionality that isn’t supported in the specified version.
### Initializers
- [init?(rawValue: Int)](skanerror-swift.struct/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let SKANErrorDomain: String](skanerrordomain.md)
  A string that identifies the SKAdNetwork error domain.
- [struct SKANError](skanerror-swift.struct.md)
  An error that an ad network attribution operation returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skanerror-swift.struct/code)*