# location

**Framework**: GameKit  
**Kind**: property

The corner of the screen to display the access point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var location: GKAccessPoint.Location { get set }
```

## Mentions

- [Adding an access point to your game](adding-an-access-point-to-your-game.md)

#### Discussion

Use this property to set one of four corners to display the access point in your game. The default for left-to-right languages is the upper-left corner, and for right-to-left languages, it’s the upper-right corner.

If the [`parentWindow`](gkaccesspoint/parentwindow.md) property is `nil` for volumetric and immersive visionOS games, GameKit doesn’t use the [`location`](gkaccesspoint/location-swift.property.md) property. For more information, see [`Configure the access point on visionOS`](adding-an-access-point-to-your-game#Configure-the-access-point-on-visionOS.md).

## See Also

- [GKAccessPoint.Location](gkaccesspoint/location-swift.enum.md)
  Specifies the corner of the screen to display the access point.
- [var frameInScreenCoordinates: CGRect](gkaccesspoint/frameinscreencoordinates.md)
  The frame of the access point in screen coordinates.
- [var parentWindow: UIWindow?](gkaccesspoint/parentwindow.md)
  The window that contains the access point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/location-swift.property)*