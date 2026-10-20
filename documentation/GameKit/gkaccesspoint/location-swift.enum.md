# GKAccessPoint.Location

**Framework**: GameKit  
**Kind**: enum  
**Role**: Enumeration

Specifies the corner of the screen to display the access point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
enum Location
```

```c
enum GKAccessPointLocation : NSInteger;
```

## Topics

### Corners
- [GKAccessPoint.Location.bottomLeading](./location-swift.enum/bottomleading.md)
  The lower-left corner of the screen.
- [GKAccessPoint.Location.bottomTrailing](./location-swift.enum/bottomtrailing.md)
  The lower-right corner of the screen.
- [GKAccessPoint.Location.topLeading](./location-swift.enum/topleading.md)
  The upper-left corner of the screen.
- [GKAccessPoint.Location.topTrailing](./location-swift.enum/toptrailing.md)
  The upper-right corner of the screen.
### Initializers
- [init?(rawValue: Int)](./location-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing the location
- [var location: GKAccessPoint.Location](./location-swift.property.md)
  The corner of the screen to display the access point.
- [var frameInScreenCoordinates: CGRect](./frameinscreencoordinates.md)
  The frame of the access point in screen coordinates.
- [var parentWindow: UIWindow?](./parentwindow.md)
  The window that contains the access point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/location-swift.enum)*