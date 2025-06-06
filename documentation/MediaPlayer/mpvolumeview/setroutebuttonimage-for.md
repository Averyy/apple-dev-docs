# setRouteButtonImage(_:for:)

**Framework**: Media Player  
**Kind**: method

Assigns a button image to the specified control states.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func setRouteButtonImage(_ image: UIImage?, for state: UIControl.State)
```

#### Discussion

Use this to customize the appearance of the route button for various states such as enabled, disabled, and highlighted.

## Parameters

- `image`: The image to associate with the specified states.
- `state`: The control state with which to associate the image.

## See Also

- [var volumeWarningSliderImage: UIImage?](mpvolumeview/volumewarningsliderimage.md)
  The image used to designate the European Union volume limit.
- [var showsRouteButton: Bool](mpvolumeview/showsroutebutton.md)
  A Boolean value that indicates whether the route button is visible in the volume view.
- [var areWirelessRoutesAvailable: Bool](mpvolumeview/arewirelessroutesavailable.md)
  A Boolean value indicating wireless routes are available.
- [var isWirelessRouteActive: Bool](mpvolumeview/iswirelessrouteactive.md)
  A Boolean value that indicates whether the wireless route is active.
- [func routeButtonImage(for: UIControl.State) -> UIImage?](mpvolumeview/routebuttonimage(for:).md)
  Returns the button image associated with the specified control state.
- [func routeButtonRect(forBounds: CGRect) -> CGRect](mpvolumeview/routebuttonrect(forbounds:).md)
  Returns the drawing rectangle for the route button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/setroutebuttonimage(_:for:))*