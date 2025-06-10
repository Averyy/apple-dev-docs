# SKCloudServiceCapability

**Framework**: StoreKit  
**Kind**: struct

Constants that specify the current capabilities of the customer’s Music library on the device.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.0+
- macOS 11.0+
- tvOS 9.3+
- watchOS 7.0+

## Declaration

```swift
struct SKCloudServiceCapability
```

## Topics

### Initializing
- [init(rawValue: UInt)](skcloudservicecapability/init(rawvalue:).md)
  Initializes a cloud service capability with the provided raw value.
### Identifying Cloud Service Capabilities
- [static var musicCatalogPlayback: SKCloudServiceCapability](skcloudservicecapability/musiccatalogplayback.md)
  The device allows playback of Apple Music catalog tracks.
- [static var musicCatalogSubscriptionEligible: SKCloudServiceCapability](skcloudservicecapability/musiccatalogsubscriptioneligible.md)
  The device allows subscription to the Apple Music catalog.
- [static var addToCloudMusicLibrary: SKCloudServiceCapability](skcloudservicecapability/addtocloudmusiclibrary.md)
  The device allows tracks to be added to the user’s music library.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Determining a person’s Apple Music capabilities](determining-a-person-s-apple-music-capabilities.md)
  Determine which Apple Music capabilities are available on a customer’s device.
- [func requestUserToken(forDeveloperToken: String, completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requestusertoken(fordevelopertoken:completionhandler:).md)
  Returns a user token that you use to access personalized Apple Music content.
- [func requestStorefrontCountryCode(completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requeststorefrontcountrycode(completionhandler:).md)
  Gets the country code for the storefront associated with a customer’s iTunes account.
- [func requestCapabilities(completionHandler: (SKCloudServiceCapability, (any Error)?) -> Void)](skcloudservicecontroller/requestcapabilities(completionhandler:).md)
  Gets the current capabilities associated with the Music library on the device.
- [func requestStorefrontIdentifier(completionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requeststorefrontidentifier(completionhandler:).md)
  Gets the device’s storefront identifier.
- [func requestPersonalizationToken(forClientToken: String, withCompletionHandler: (String?, (any Error)?) -> Void)](skcloudservicecontroller/requestpersonalizationtoken(forclienttoken:withcompletionhandler:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skcloudservicecapability)*