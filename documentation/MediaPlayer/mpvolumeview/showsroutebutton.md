# showsRouteButton

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the route button is visible in the volume view.

**Availability**:
- iOS 4.2+ - Deprecated in 13.0
- iPadOS 4.2+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: Use AVRoutePickerView instead.

## Declaration

```swift
var showsRouteButton: Bool { get set }
```

```objc
@property (nonatomic) BOOL showsRouteButton;
```

#### Discussion

The route button is visible by default when there’s more than one audio output route available. To hide the route button, set this property’s value to [`false`](../../Swift/false.md).

## See Also

### Deprecated
- [var volumeWarningSliderImage: UIImage?](./volumewarningsliderimage.md)
  The image used to designate the European Union volume limit.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/showsroutebutton)*