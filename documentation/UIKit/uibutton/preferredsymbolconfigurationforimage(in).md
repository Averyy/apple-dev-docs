# preferredSymbolConfigurationForImage(in:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the preferred symbol configuration for a button state.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func preferredSymbolConfigurationForImage(in state: UIControl.State) -> UIImage.SymbolConfiguration?
```

```objc
- (UIImageSymbolConfiguration *) preferredSymbolConfigurationForImageInState:(UIControlState) state;
```

## Parameters

- `state`: The state that uses the symbol configuration. Possible values are described in [`UIControl.State`](../uicontrol/state-swift.struct.md).

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
- [func setPreferredSymbolConfiguration(UIImage.SymbolConfiguration?, forImageIn: UIControl.State)](./setpreferredsymbolconfiguration%28_,forimagein%29.md)
  Sets the preferred symbol configuration for a button state.
- [var tintColor: UIColor!](./tintcolor.md)
  The tint color to apply to the button title and image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/preferredsymbolconfigurationforimage(in:))*