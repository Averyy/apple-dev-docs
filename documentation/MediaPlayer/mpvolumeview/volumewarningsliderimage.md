# volumeWarningSliderImage

**Framework**: Media Player  
**Kind**: property

The image used to designate the European Union volume limit.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var volumeWarningSliderImage: UIImage? { get set }
```

#### Discussion

The system displays the image contained by this property on top of the [`maximumVolumeSliderImage(for:)`](mpvolumeview/maximumvolumesliderimage(for:).md). The image must be visually distinct from the `maximumVolumeSliderImage` and use a color similar to the default in order to convey a sense of warning to the user.

For testing purposes, set the EU Volume Limit setting in the Developer menu of the Settings app to always enable the volume limit.

## See Also

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
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](mpvolumeview/setroutebuttonimage(_:for:).md)
  Assigns a button image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/volumewarningsliderimage)*