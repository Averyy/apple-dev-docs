# showsRouteButton

**Framework**: Media Player  
**Kind**: property

A Boolean value that indicates whether the route button is visible in the volume view.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var showsRouteButton: Bool { get set }
```

#### Discussion

The route button is visible by default when there’s more than one audio output route available. To hide the route button, set this property’s value to [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var volumeWarningSliderImage: UIImage?](mpvolumeview/volumewarningsliderimage.md)
  The image used to designate the European Union volume limit.
- [var areWirelessRoutesAvailable: Bool](mpvolumeview/arewirelessroutesavailable.md)
  A Boolean value indicating wireless routes are available.
- [var isWirelessRouteActive: Bool](mpvolumeview/iswirelessrouteactive.md)
  A Boolean value that indicates whether the wireless route is active.
- [func routeButtonImage(for: UIControl.State) -> UIImage?](mpvolumeview/routebuttonimage(for:).md)
  Returns the button image associated with the specified control state.
- [func routeButtonRect(forBounds: CGRect) -> CGRect](mpvolumeview/routebuttonrect(forbounds:).md)
  Returns the drawing rectangle for the route button.
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](mpvolumeview/setroutebuttonimage(_:for:).md)
  Assigns a button image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/showsroutebutton)*