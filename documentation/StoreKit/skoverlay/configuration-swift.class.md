# SKOverlay.Configuration

**Framework**: StoreKit  
**Kind**: class  
**Role**: Class

The abstract superclass for all classes that represent an overlay’s attributes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
class Configuration
```

```objc
@interface SKOverlayConfiguration : NSObject
```

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [SKOverlay.AppClipConfiguration](./appclipconfiguration.md)
- [SKOverlay.AppConfiguration](./appconfiguration.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating an overlay
- [init(configuration: SKOverlay.Configuration)](./init%28configuration%29.md)
  Creates an overlay you use to recommend another app on the App Store.
- [var configuration: SKOverlay.Configuration](./configuration-swift.property.md)
  An overlay’s attributes; for example, its position on the screen.
- [SKOverlay.AppConfiguration](./appconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [SKOverlay.AppClipConfiguration](./appclipconfiguration.md)
  An object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding full app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/configuration-swift.class)*