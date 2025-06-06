# routeButtonImage(for:)

**Framework**: Media Player  
**Kind**: method

Returns the button image associated with the specified control state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
func routeButtonImage(for state: UIControl.State) -> UIImage?
```

#### Return Value

The button image associated with the specified state, or [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if an appropriate image could not be retrieved. This method might return [`nil`](https://developer.apple.com/documentation/ObjectiveC/nil-227m0) if you specify multiple control states in the state parameter.

#### Discussion

Use this method to retrieve the corresponding button image for a specific state.

## Parameters

- `state`: The control state whose thumb image you want. You should specify only one control state value for this parameter.

## See Also

- [var volumeWarningSliderImage: UIImage?](mpvolumeview/volumewarningsliderimage.md)
  The image used to designate the European Union volume limit.
- [var showsRouteButton: Bool](mpvolumeview/showsroutebutton.md)
  A Boolean value that indicates whether the route button is visible in the volume view.
- [var areWirelessRoutesAvailable: Bool](mpvolumeview/arewirelessroutesavailable.md)
  A Boolean value indicating wireless routes are available.
- [var isWirelessRouteActive: Bool](mpvolumeview/iswirelessrouteactive.md)
  A Boolean value that indicates whether the wireless route is active.
- [func routeButtonRect(forBounds: CGRect) -> CGRect](mpvolumeview/routebuttonrect(forbounds:).md)
  Returns the drawing rectangle for the route button.
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](mpvolumeview/setroutebuttonimage(_:for:).md)
  Assigns a button image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/routebuttonimage(for:))*