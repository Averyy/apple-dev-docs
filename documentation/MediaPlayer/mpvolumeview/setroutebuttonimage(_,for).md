# setRouteButtonImage(_:for:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Assigns a button image to the specified control states.

**Availability**:
- iOS 6.0+ - Deprecated in 13.0
- iPadOS 6.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: Use AVRoutePickerView.routePickerButtonStyle instead.

## Declaration

```swift
func setRouteButtonImage(_ image: UIImage?, for state: UIControl.State)
```

```objc
- (void) setRouteButtonImage:(UIImage *) image forState:(UIControlState) state;
```

#### Discussion

Use this to customize the appearance of the route button for various states such as enabled, disabled, and highlighted.

## Parameters

- `image`: The image to associate with the specified states.
- `state`: The control state with which to associate the image.

## See Also

### Deprecated
- [var volumeWarningSliderImage: UIImage?](./volumewarningsliderimage.md)
  The image used to designate the European Union volume limit.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/setroutebuttonimage(_:for:))*