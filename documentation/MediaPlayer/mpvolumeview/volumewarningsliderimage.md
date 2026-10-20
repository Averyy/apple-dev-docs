# volumeWarningSliderImage

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

The image used to designate the European Union volume limit.

**Availability**:
- iOS 7.0+ - Deprecated in 17.0
- iPadOS 7.0+ - Deprecated in 17.0
- Mac Catalyst 13.1+ - Deprecated in 17.0
- tvOS - Deprecated in 17.0

> **Deprecated**: This is no longer supported

## Declaration

```swift
var volumeWarningSliderImage: UIImage? { get set }
```

```objc
@property (nonatomic, strong, nullable) UIImage * volumeWarningSliderImage;
```

#### Discussion

The system displays the image contained by this property on top of the [`maximumVolumeSliderImage(for:)`](./maximumvolumesliderimage%28for%29.md). The image must be visually distinct from the `maximumVolumeSliderImage` and use a color similar to the default in order to convey a sense of warning to the user.

For testing purposes, set the EU Volume Limit setting in the Developer menu of the Settings app to always enable the volume limit.

## See Also

### Deprecated
- [var showsRouteButton: Bool](./showsroutebutton.md)
  A Boolean value that indicates whether the route button is visible in the volume view.
- [var areWirelessRoutesAvailable: Bool](./arewirelessroutesavailable.md)
  A Boolean value indicating wireless routes are available.
- [var isWirelessRouteActive: Bool](./iswirelessrouteactive.md)
  A Boolean value that indicates whether the wireless route is active.
- [func routeButtonImage(for: UIControl.State) -> UIImage?](./routebuttonimage%28for%29.md)
  Returns the button image associated with the specified control state.
- [func routeButtonRect(forBounds: CGRect) -> CGRect](./routebuttonrect%28forbounds%29.md)
  Returns the drawing rectangle for the route button.
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](./setroutebuttonimage%28_,for%29.md)
  Assigns a button image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/volumewarningsliderimage)*