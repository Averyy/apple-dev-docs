# routeButtonImage(for:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Returns the button image associated with the specified control state.

**Availability**:
- iOS 6.0+ - Deprecated in 13.0
- iPadOS 6.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: See AVRoutePickerView for possible replacements.

## Declaration

```swift
func routeButtonImage(for state: UIControl.State) -> UIImage?
```

```objc
- (UIImage *) routeButtonImageForState:(UIControlState) state;
```

#### Return Value

The button image associated with the specified state, or [`nil`](../../ObjectiveC/nil-227m0.md) if an appropriate image could not be retrieved. This method might return [`nil`](../../ObjectiveC/nil-227m0.md) if you specify multiple control states in the state parameter.

#### Discussion

Use this method to retrieve the corresponding button image for a specific state.

## Parameters

- `state`: The control state whose thumb image you want. You should specify only one control state value for this parameter.

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
- [func routeButtonRect(forBounds: CGRect) -> CGRect](./routebuttonrect%28forbounds%29.md)
  Returns the drawing rectangle for the route button.
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](./setroutebuttonimage%28_,for%29.md)
  Assigns a button image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/routebuttonimage(for:))*