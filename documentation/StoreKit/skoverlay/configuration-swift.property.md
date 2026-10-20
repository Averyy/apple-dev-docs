# configuration

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

An overlay’s attributes; for example, its position on the screen.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@NSCopying
var configuration: SKOverlay.Configuration { get }
```

```objc
@property (copy, readonly) SKOverlayConfiguration * configuration;
```

## See Also

### Creating an overlay
- [init(configuration: SKOverlay.Configuration)](./init%28configuration%29.md)
  Creates an overlay you use to recommend another app on the App Store.
- [SKOverlay.AppConfiguration](./appconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [SKOverlay.AppClipConfiguration](./appclipconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.
- [SKOverlay.Configuration](./configuration-swift.class.md)
  The abstract superclass for all classes that represent an overlay’s attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/configuration-swift.property)*