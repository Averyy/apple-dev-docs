# init(configuration:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

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

```objc
- (instancetype) initWithConfiguration:(SKOverlayConfiguration *) configuration;
```

#### Discussion

Pass an [`SKOverlay.AppConfiguration`](./appconfiguration.md) as the `configuration` parameter if you want to display the overlay in an app. To recommend an App Clip’s corresponding app, pass an [`SKOverlay.AppClipConfiguration`](./appclipconfiguration.md) object to the initializer. For more information, see [Recommending your app to App Clip users](../../AppClip/recommending-your-app-to-app-clip-users.md).

## Parameters

- `configuration`: The object that represents the overlay’s attributes; for example, its position on the screen.

## See Also

### Creating an overlay
- [var configuration: SKOverlay.Configuration](./configuration-swift.property.md)
  An overlay’s attributes; for example, its position on the screen.
- [SKOverlay.AppConfiguration](./appconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [SKOverlay.AppClipConfiguration](./appclipconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.
- [SKOverlay.Configuration](./configuration-swift.class.md)
  The abstract superclass for all classes that represent an overlay’s attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/init(configuration:))*