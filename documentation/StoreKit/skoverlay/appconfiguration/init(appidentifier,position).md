# init(appIdentifier:position:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

Creates an object that represents the attributes of an overlay you use to recommend another app on the App Store.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
init(appIdentifier: String, position: SKOverlay.Position)
```

```objc
- (instancetype) initWithAppIdentifier:(NSString *) appIdentifier position:(SKOverlayPosition) position;
```

## Parameters

- `appIdentifier`: The iTunes identifier of the recommended app.
- `position`: The position of the overlay on the screen.

## See Also

### Creating an App Configuration
- [var appIdentifier: String](./appidentifier.md)
  The iTunes identifier of the recommended app.
- [var position: SKOverlay.Position](./position.md)
  The position of the overlay on the screen.
- [SKOverlay.Position](../position.md)
  Constants that identify the position of an overlay on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration/init(appidentifier:position:))*