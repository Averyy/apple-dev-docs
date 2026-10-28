# backgroundImage(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the background image used for a button state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func backgroundImage(for state: UIControl.State) -> UIImage?
```

```objc
- (UIImage *) backgroundImageForState:(UIControlState) state;
```

## Return Value

The background image used for the specified state.

## Parameters

- `state`: The state that uses the background image. Possible values are described in [`UIControl.State`](../uicontrol/state-swift.struct.md).

## See Also

### Managing images and tint color
- [func image(for: UIControl.State) -> UIImage?](./image%28for%29.md)
  Returns the image used for a button state.
- [func setBackgroundImage(UIImage?, for: UIControl.State)](./setbackgroundimage%28_,for%29.md)
  Sets the background image to use for the specified button state.
- [func setImage(UIImage?, for: UIControl.State)](./setimage%28_,for%29.md)
  Sets the image to use for the specified state.
- [func preferredSymbolConfigurationForImage(in: UIControl.State) -> UIImage.SymbolConfiguration?](./preferredsymbolconfigurationforimage%28in%29.md)
  Returns the preferred symbol configuration for a button state.
- [func setPreferredSymbolConfiguration(UIImage.SymbolConfiguration?, forImageIn: UIControl.State)](./setpreferredsymbolconfiguration%28_,forimagein%29.md)
  Sets the preferred symbol configuration for a button state.
- [var tintColor: UIColor!](./tintcolor.md)
  The tint color to apply to the button title and image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/backgroundimage(for:))*