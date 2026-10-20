# isWirelessRouteActive

**Framework**: Media Player  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the wireless route is active.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 13.0

> **Deprecated**: Use AVPlayer.externalPlaybackActive instead.

## Declaration

```swift
var isWirelessRouteActive: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isWirelessRouteActive) BOOL wirelessRouteActive;
```

#### Discussion

When set to [`true`](../../Swift/true.md), the wireless route is active.

## See Also

### Deprecated
- [var volumeWarningSliderImage: UIImage?](./volumewarningsliderimage.md)
  The image used to designate the European Union volume limit.
- [var showsRouteButton: Bool](./showsroutebutton.md)
  A Boolean value that indicates whether the route button is visible in the volume view.
- [var areWirelessRoutesAvailable: Bool](./arewirelessroutesavailable.md)
  A Boolean value indicating wireless routes are available.
- [func routeButtonImage(for: UIControl.State) -> UIImage?](./routebuttonimage%28for%29.md)
  Returns the button image associated with the specified control state.
- [func routeButtonRect(forBounds: CGRect) -> CGRect](./routebuttonrect%28forbounds%29.md)
  Returns the drawing rectangle for the route button.
- [func setRouteButtonImage(UIImage?, for: UIControl.State)](./setroutebuttonimage%28_,for%29.md)
  Assigns a button image to the specified control states.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mediaplayer/mpvolumeview/iswirelessrouteactive)*