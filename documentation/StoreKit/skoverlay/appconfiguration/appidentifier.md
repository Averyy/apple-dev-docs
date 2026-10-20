# appIdentifier

**Framework**: StoreKit  
**Kind**: property  
**Role**: Instance Property

The iTunes identifier of the recommended app.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var appIdentifier: String { get set }
```

```objc
@property (nonatomic, retain) NSString * appIdentifier;
```

## See Also

### Creating an App Configuration
- [init(appIdentifier: String, position: SKOverlay.Position)](./init%28appidentifier,position%29.md)
  Creates an object that represents the attributes of an overlay you use to recommend another app on the App Store.
- [var position: SKOverlay.Position](./position.md)
  The position of the overlay on the screen.
- [SKOverlay.Position](../position.md)
  Constants that identify the position of an overlay on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/appconfiguration/appidentifier)*