# SKOverlay.AppConfiguration

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

An object that represents the attributes of an overlay you use to recommend another app on the App Store.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class AppConfiguration
```

```objc
@interface SKOverlayAppConfiguration : SKOverlayConfiguration
```

## Topics

### Creating an App Configuration
- [init(appIdentifier: String, position: SKOverlay.Position)](./appconfiguration/init%28appidentifier,position%29.md)
  Creates an object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [var appIdentifier: String](./appconfiguration/appidentifier.md)
  The iTunes identifier of the recommended app.
- [var position: SKOverlay.Position](./appconfiguration/position.md)
  The position of the overlay on the screen.
- [SKOverlay.Position](./position.md)
  Constants that identify the position of an overlay on the screen.
### Dismissing the Overlay
- [var userDismissible: Bool](./appconfiguration/userdismissible.md)
  A Boolean value that indicates whether the user can dismiss the overlay.
### Verifying Advertising Campaigns
- [var campaignToken: String?](./appconfiguration/campaigntoken.md)
  A token you use to represent an ad campaign and measure its effectiveness.
- [var providerToken: String?](./appconfiguration/providertoken.md)
  A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [func setAdditionalValue(Any?, forKey: String)](./appconfiguration/setadditionalvalue%28_,forkey%29.md)
  Sets an additional value for a key; for example, a value for measuring the effectiveness of an ad campaign.
- [func additionalValue(forKey: String) -> Any?](./appconfiguration/additionalvalue%28forkey%29.md)
  Returns the object associated with the key.
### Promoting the Latest App Version
- [var latestReleaseID: String?](./appconfiguration/latestreleaseid.md)
  The release ID of the latest version of your app as displayed in App Store Connect.
### Advertising Another App
- [var customProductPageIdentifier: String?](./appconfiguration/customproductpageidentifier.md)
  An optional identifier for an app’s custom product page.
### Setting an Ad Impression
- [func setAdImpression(SKAdImpression)](./appconfiguration/setadimpression%28_%29.md)
### Instance Properties
- [var adAttributionReengagementURL: URL?](./appconfiguration/adattributionreengagementurl.md)
- [var appImpression: AppImpression?](./appconfiguration/appimpression.md)

## Relationships

### Inherits From
- [SKOverlay.Configuration](./configuration-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an overlay
- [init(configuration: SKOverlay.Configuration)](./init%28configuration%29.md)
  Creates an overlay you use to recommend another app on the App Store.
- [var configuration: SKOverlay.Configuration](./configuration-swift.property.md)
  An overlay’s attributes; for example, its position on the screen.
- [SKOverlay.AppClipConfiguration](./appclipconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.
- [SKOverlay.Configuration](./configuration-swift.class.md)
  The abstract superclass for all classes that represent an overlay’s attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration)*