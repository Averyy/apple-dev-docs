# SKOverlay.AppConfiguration

**Framework**: StoreKit  
**Kind**: class

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

## Topics

### Creating an App Configuration
- [init(appIdentifier: String, position: SKOverlay.Position)](skoverlay/appconfiguration/init(appidentifier:position:).md)
  Creates an object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [var appIdentifier: String](skoverlay/appconfiguration/appidentifier.md)
  The iTunes identifier of the recommended app.
- [var position: SKOverlay.Position](skoverlay/appconfiguration/position.md)
  The position of the overlay on the screen.
- [SKOverlay.Position](skoverlay/position.md)
  Constants that identify the position of an overlay on the screen.
### Dismissing the Overlay
- [var userDismissible: Bool](skoverlay/appconfiguration/userdismissible.md)
  A Boolean value that indicates whether the user can dismiss the overlay.
### Verifying Advertising Campaigns
- [var campaignToken: String?](skoverlay/appconfiguration/campaigntoken.md)
  A token you use to represent an ad campaign and measure its effectiveness.
- [var providerToken: String?](skoverlay/appconfiguration/providertoken.md)
  A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [func setAdditionalValue(Any?, forKey: String)](skoverlay/appconfiguration/setadditionalvalue(_:forkey:).md)
  Sets an additional value for a key; for example, a value for measuring the effectiveness of an ad campaign.
- [func additionalValue(forKey: String) -> Any?](skoverlay/appconfiguration/additionalvalue(forkey:).md)
  Returns the object associated with the key.
### Promoting the Latest App Version
- [var latestReleaseID: String?](skoverlay/appconfiguration/latestreleaseid.md)
  The release ID of the latest version of your app as displayed in App Store Connect.
### Advertising Another App
- [var customProductPageIdentifier: String?](skoverlay/appconfiguration/customproductpageidentifier.md)
  An optional identifier for an app’s custom product page.
### Setting an Ad Impression
- [func setAdImpression(SKAdImpression)](skoverlay/appconfiguration/setadimpression(_:).md)
### Instance Properties
- [var adAttributionReengagementURL: URL?](skoverlay/appconfiguration/adattributionreengagementurl.md)
- [var appImpression: AppImpression?](skoverlay/appconfiguration/appimpression.md)

## Relationships

### Inherits From
- [SKOverlay.Configuration](skoverlay/configuration-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [init(configuration: SKOverlay.Configuration)](skoverlay/init(configuration:).md)
  Creates an overlay you use to recommend another app on the App Store.
- [var configuration: SKOverlay.Configuration](skoverlay/configuration-swift.property.md)
  An overlay’s attributes; for example, its position on the screen.
- [SKOverlay.AppClipConfiguration](skoverlay/appclipconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.
- [SKOverlay.Configuration](skoverlay/configuration-swift.class.md)
  The abstract superclass for all classes that represent an overlay’s attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration)*