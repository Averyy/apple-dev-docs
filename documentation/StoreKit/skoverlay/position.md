# SKOverlay.Position

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Constants that identify the position of an overlay on the screen.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Position
```

```c
enum SKOverlayPosition : NSInteger;
```

## Topics

### Describing the Overlay’s Position
- [SKOverlay.Position.bottom](./position/bottom.md)
  Specifies that the overlay is at the bottom of the screen.
- [SKOverlay.Position.bottomRaised](./position/bottomraised.md)
  Specifies that the overlay is at a raised position at the bottom of the screen.
### Initializers
- [init?(rawValue: Int)](./position/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an App Clip Configuration
- [init(position: SKOverlay.Position)](./appclipconfiguration/init%28position%29.md)
  Creates an object that represents the attributes of an overlay you use to recommend an App Clip’s corresponding app.
- [var position: SKOverlay.Position](./appclipconfiguration/position.md)
  The position of the overlay on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/skoverlay/position)*