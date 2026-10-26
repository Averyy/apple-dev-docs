# SKCloudServiceCapability

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Constants that specify the current capabilities of the customer’s Music library on the device.

**Availability**:
- iOS 9.3+ - Deprecated in 18.0
- iPadOS 9.3+ - Deprecated in 18.0
- Mac Catalyst 13.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 9.3+ - Deprecated in 18.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use MusicSubscription from MusicKit.

## Declaration

```swift
struct SKCloudServiceCapability
```

```c
enum SKCloudServiceCapability : NSUInteger;
```

## Topics

### Initializing
- [init(rawValue: UInt)](./skcloudservicecapability/init%28rawvalue%29.md)
  Initializes a cloud service capability with the provided raw value.
### Identifying Cloud Service Capabilities
- [static var musicCatalogPlayback: SKCloudServiceCapability](./skcloudservicecapability/musiccatalogplayback.md)
  The device allows playback of Apple Music catalog tracks.
- [static var musicCatalogSubscriptionEligible: SKCloudServiceCapability](./skcloudservicecapability/musiccatalogsubscriptioneligible.md)
  The device allows subscription to the Apple Music catalog.
- [static var addToCloudMusicLibrary: SKCloudServiceCapability](./skcloudservicecapability/addtocloudmusiclibrary.md)
  The device allows tracks to be added to the user’s music library.
### Enumeration Cases
- [SKCloudServiceCapabilityNone](./skcloudservicecapability/skcloudservicecapabilitynone.md)
  The device does not allow playback of Apple Music content or the addition of tracks to the music library.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Determining capabilities
- [Determining a person’s Apple Music capabilities](./determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestUserToken(forDeveloperToken: String, completionHandler: (String?, (any Error)?) -> Void)](./skcloudservicecontroller/requestusertoken%28fordevelopertoken,completionhandler%29.md)
  Returns a user token that you use to access personalized Apple Music content.
- [func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?) -> Void)](./skcloudservicecontroller/requeststorefrontcountrycode%28completionhandler%29.md)
  Gets the country code for the storefront associated with a customer’s iTunes account.
- [func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any Error)?) -> Void)](./skcloudservicecontroller/requestcapabilities%28completionhandler%29.md)
  Gets the current capabilities associated with the Music library on the device.
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](./skcloudservicecontroller/requeststorefrontidentifier%28completionhandler%29.md)
  Gets the device’s storefront identifier.
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](./skcloudservicecontroller/requestpersonalizationtoken%28forclienttoken,withcompletionhandler%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecapability)*