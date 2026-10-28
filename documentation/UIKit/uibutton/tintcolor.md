# tintColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The tint color to apply to the button title and image.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var tintColor: UIColor! { get set }
```

```objc
@property (nonatomic, strong, null_resettable) UIColor * tintColor;
```

## Discussion

All subclasses of [`UIView`](../uiview.md) derive their behavior for [`tintColor`](../uiview/tintcolor.md) from the base class. See the discussion of [`tintColor`](../uiview/tintcolor.md) at the [`UIView`](../uiview.md) level for more information.

This property has no default effect for buttons with type [`UIButton.ButtonType.custom`](./buttontype-swift.enum/custom.md). For custom buttons, you must implement any behavior related to [`tintColor`](./tintcolor.md) yourself.

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
- [func setPreferredSymbolConfiguration(UIImage.SymbolConfiguration?, forImageIn: UIControl.State)](./setpreferredsymbolconfiguration%28_,forimagein%29.md)
  Sets the preferred symbol configuration for a button state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/tintcolor)*