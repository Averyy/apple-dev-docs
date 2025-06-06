# parentWindow

**Framework**: GameKit  
**Kind**: property

The window that contains the access point.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
weak var parentWindow: NSWindow? { get set }
```

## Mentions

- [Adding an access point to your game](adding-an-access-point-to-your-game.md)

#### Discussion

For Mac games, use this property to specify the parent window of the access point. If you don’t specify a parent widow, GameKit tries to add the access point to the app’s main window. For iPadOS and iOS games, and for compatible iPad or iPhone games running in visionOS, GameKit adds the access point to the main window.

If this property is `nil` for a volumetric visionOS game, the access point doesn’t appear. For an immersive game, it appears below the HUD in front of the person and tracks their head position. If this property is non-`nil` for a volumetric or immersive game, the access point appears outside of the window in the specified location. For more information, see [`Configure the access point on visionOS`](adding-an-access-point-to-your-game#Configure-the-access-point-on-visionOS.md).

## See Also

- [var location: GKAccessPoint.Location](gkaccesspoint/location-swift.property.md)
  The corner of the screen to display the access point.
- [GKAccessPoint.Location](gkaccesspoint/location-swift.enum.md)
  Specifies the corner of the screen to display the access point.
- [var frameInScreenCoordinates: CGRect](gkaccesspoint/frameinscreencoordinates.md)
  The frame of the access point in screen coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamekit/gkaccesspoint/parentwindow)*