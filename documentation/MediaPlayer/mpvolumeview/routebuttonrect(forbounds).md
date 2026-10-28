# routeButtonRect(forBounds:)

**Framework**: Media Player  
**Kind**: method  
**Role**: Instance Method

Returns the drawing rectangle for the route button.

**Availability**:
- iOS 6.0+ - Deprecated in 13.0
- iPadOS 6.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: See AVRoutePickerView for possible replacements.

## Declaration

```swift
func routeButtonRect(forBounds bounds: CGRect) -> CGRect
```

```objc
- (CGRect) routeButtonRectForBounds:(CGRect) bounds;
```

## Return Value

The computed drawing rectangle for the route button.

## Discussion

Use this method to retrieve the bounding rectangle for the route button.

## Parameters

- `bounds`: The bounding rectangle of the receiver.

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
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](./setroutebuttonimage%28_,for%29.md)
  Assigns a button image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/routebuttonrect(forbounds:))*