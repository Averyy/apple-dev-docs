# SKOverlay.AppClipConfiguration

**Framework**: StoreKit  
**Kind**: class

An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class AppClipConfiguration
```

## Topics

### Creating an App Clip Configuration
- [init(position: SKOverlay.Position)](skoverlay/appclipconfiguration/init(position:).md)
  Creates an object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding app.
- [var position: SKOverlay.Position](skoverlay/appclipconfiguration/position.md)
  The position of the overlay on the screen.
- [SKOverlay.Position](skoverlay/position.md)
  Constants that identify the position of an overlay on the screen.
### Verifying Advertising Campaigns
- [var campaignToken: String?](skoverlay/appclipconfiguration/campaigntoken.md)
  A token you use to represent an ad campaign and measure its effectiveness.
- [var providerToken: String?](skoverlay/appclipconfiguration/providertoken.md)
  A token that represents the provider of an app promotion campaign, and that you use to measure the campaign’s effectiveness.
- [func setAdditionalValue(Any?, forKey: String)](skoverlay/appclipconfiguration/setadditionalvalue(_:forkey:).md)
  Sets an additional value for a key, such as a value for measuring the effectiveness of an ad campaign.
- [func additionalValue(forKey: String) -> Any?](skoverlay/appclipconfiguration/additionalvalue(forkey:).md)
  Returns the object associated with the key.
### Promoting the Latest App Version
- [var latestReleaseID: String?](skoverlay/appclipconfiguration/latestreleaseid.md)
  The release ID of the latest version of your parent app as displayed in App Store Connect.
### Advertising Another App
- [var customProductPageIdentifier: String?](skoverlay/appclipconfiguration/customproductpageidentifier.md)
  An identifier for a parent app’s custom product page.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(configuration: SKOverlay.Configuration)](skoverlay/init(configuration:).md)
  Creates an overlay you use to recommend another app on the App Store.
- [var configuration: SKOverlay.Configuration](skoverlay/configuration-swift.property.md)
  An overlay’s attributes; for example, its position on the screen.
- [SKOverlay.AppConfiguration](skoverlay/appconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [SKOverlay.Configuration](skoverlay/configuration-swift.class.md)
  The abstract superclass for all classes that represent an overlay’s attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appclipconfiguration)*