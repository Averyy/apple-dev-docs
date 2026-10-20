# setPreferredSymbolConfiguration(_:forImageIn:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the preferred symbol configuration for a button state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setPreferredSymbolConfiguration(_ configuration: UIImage.SymbolConfiguration?, forImageIn state: UIControl.State)
```

```objc
- (void) setPreferredSymbolConfiguration:(UIImageSymbolConfiguration *) configuration forImageInState:(UIControlState) state;
```

## Parameters

- `configuration`: The image symbol configuration for the specified state.
- `state`: The state that uses the specified image symbol configuration. Possible values are described in [`UIControl.State`](../uicontrol/state-swift.struct.md).

## See Also

### Managing images and tint color
- [func backgroundImage(for: UIControl.State) -> UIImage?](./backgroundimage%28for%29.md)
  Returns the background image used for a button state.
- [func image(for: UIControl.State) -> UIImage?](./image%28for%29.md)
  Returns the image used for a button state.
- [func setBackgroundImage(UIImage?, for: UIControl.State)](./setbackgroundimage%28_,for%29.md)
  Sets the background image to use for the specified button state.
- [func setImage(UIImage?, for: UIControl.State)](./setimage%28_,for%29.md)
  Sets the image to use for the specified state.
- [func preferredSymbolConfigurationForImage(in: UIControl.State) -> UIImage.SymbolConfiguration?](./preferredsymbolconfigurationforimage%28in%29.md)
  Returns the preferred symbol configuration for a button state.
- [var tintColor: UIColor!](./tintcolor.md)
  The tint color to apply to the button title and image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/setpreferredsymbolconfiguration(_:forimagein:))*