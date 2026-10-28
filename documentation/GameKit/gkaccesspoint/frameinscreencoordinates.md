# frameInScreenCoordinates

**Framework**: GameKit  
**Kind**: property  
**Role**: Instance Property

The frame of the access point in screen coordinates.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```swift
var frameInScreenCoordinates: CGRect { get }
```

*macOS*

```swift
var frameInScreenCoordinates: NSRect { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) CGRect frameInScreenCoordinates;
```

*macOS*

```objc
@property (nonatomic, readonly) NSRect frameInScreenCoordinates;
```

## Mentions

- [Adding an access point to your game](../adding-an-access-point-to-your-game.md)

## Discussion

This is an observable property.

## See Also

### Managing the location
- [var location: GKAccessPoint.Location](./location-swift.property.md)
  The corner of the screen to display the access point.
- [GKAccessPoint.Location](./location-swift.enum.md)
  Specifies the corner of the screen to display the access point.
- [var parentWindow: UIWindow?](./parentwindow.md)
  The window that contains the access point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/frameinscreencoordinates)*