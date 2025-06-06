# isWirelessRouteActive

**Framework**: Media Player  
**Kind**: property

A Boolean value that indicates whether the wireless route is active.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var isWirelessRouteActive: Bool { get }
```

#### Discussion

When set to [`true`](https://developer.apple.com/documentation/swift/true), the wireless route is active.

## See Also

- [var volumeWarningSliderImage: UIImage?](mpvolumeview/volumewarningsliderimage.md)
  The image used to designate the European Union volume limit.
- [var showsRouteButton: Bool](mpvolumeview/showsroutebutton.md)
  A Boolean value that indicates whether the route button is visible in the volume view.
- [var areWirelessRoutesAvailable: Bool](mpvolumeview/arewirelessroutesavailable.md)
  A Boolean value indicating wireless routes are available.
- [func routeButtonImage(for: UIControl.State) -> UIImage?](mpvolumeview/routebuttonimage(for:).md)
  Returns the button image associated with the specified control state.
- [func routeButtonRect(forBounds: CGRect) -> CGRect](mpvolumeview/routebuttonrect(forbounds:).md)
  Returns the drawing rectangle for the route button.
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](mpvolumeview/setroutebuttonimage(_:for:).md)
  Assigns a button image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/iswirelessrouteactive)*