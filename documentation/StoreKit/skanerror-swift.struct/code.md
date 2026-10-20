# SKANError.Code

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum SKANError : NSInteger;
```

## Topics

### Error Codes
- [SKANError.Code.adNetworkIdMissing](./code/adnetworkidmissing.md)
  The ad network identifier in the ad impression doesn’t match the value in the information property list.
- [SKANError.Code.impressionMissingRequiredValue](./code/impressionmissingrequiredvalue.md)
  A required value is missing from a view-through ad impression.
- [SKANError.Code.impressionNotFound](./code/impressionnotfound.md)
  The system can’t find the ad impression.
- [SKANError.Code.impressionTooShort](./code/impressiontooshort.md)
- [SKANError.Code.invalidAdvertisedAppId](./code/invalidadvertisedappid.md)
  The App Store ID of the advertised app is invalid.
- [SKANError.Code.invalidCampaignId](./code/invalidcampaignid.md)
  The campaign identifier that you provided is invalid.
- [SKANError.Code.invalidConversionValue](./code/invalidconversionvalue.md)
  The conversion value is invalid.
- [SKANError.Code.invalidSourceAppId](./code/invalidsourceappid.md)
  The App Store ID of the app displaying the ad is invalid.
- [SKANError.Code.invalidVersion](./code/invalidversion.md)
  The SKAdNetwork version number is invalid.
- [SKANError.Code.mismatchedSourceAppId](./code/mismatchedsourceappid.md)
  The source app identifier in the ad impression doesn’t match the app identifier in the source app.
- [SKANError.Code.unknown](./code/unknown.md)
  An unknown error occurred.
- [SKANError.Code.unsupported](./code/unsupported.md)
  Your app attempted to use functionality that isn’t supported in the specified version.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Error handling
- [let SKANErrorDomain: String](../skanerrordomain.md)
  A string that identifies the SKAdNetwork error domain.
- [struct SKANError](../skanerror-swift.struct.md)
  An error that an ad network attribution operation returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skanerror-swift.struct/code)*