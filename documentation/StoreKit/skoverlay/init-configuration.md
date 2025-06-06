# init(configuration:)

**Framework**: StoreKit  
**Kind**: init

Creates an overlay you use to recommend another app on the App Store.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
init(configuration: SKOverlay.Configuration)
```

#### Discussion

Pass an [`SKOverlay.AppConfiguration`](skoverlay/appconfiguration.md) as the `configuration` parameter if you want to display the overlay in an app. To recommend an App Clip’s corresponding app, pass an [`SKOverlay.AppClipConfiguration`](skoverlay/appclipconfiguration.md) object to the initializer. For more information, see [`Recommending your app to App Clip users`](https://developer.apple.com/documentation/AppClip/recommending-your-app-to-app-clip-users).

## Parameters

- `configuration`: The object that represents the overlay’s attributes; for example, its position on the screen.

## See Also

- [var configuration: SKOverlay.Configuration](skoverlay/configuration-swift.property.md)
  An overlay’s attributes; for example, its position on the screen.
- [SKOverlay.AppConfiguration](skoverlay/appconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [SKOverlay.AppClipConfiguration](skoverlay/appclipconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.
- [SKOverlay.Configuration](skoverlay/configuration-swift.class.md)
  The abstract superclass for all classes that represent an overlay’s attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/init(configuration:))*