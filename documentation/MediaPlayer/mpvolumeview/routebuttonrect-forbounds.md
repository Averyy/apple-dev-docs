# routeButtonRect(forBounds:)

**Framework**: Media Player  
**Kind**: method

Returns the drawing rectangle for the route button.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func routeButtonRect(forBounds bounds: CGRect) -> CGRect
```

#### Return Value

The computed drawing rectangle for the route button.

#### Discussion

Use this method to retrieve the bounding rectangle for the route button.

## Parameters

- `bounds`: The bounding rectangle of the receiver.

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
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](mpvolumeview/setroutebuttonimage(_:for:).md)
  Assigns a button image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/routebuttonrect(forbounds:))*