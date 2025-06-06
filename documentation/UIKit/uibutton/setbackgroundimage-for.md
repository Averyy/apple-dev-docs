# setBackgroundImage(_:for:)

**Framework**: UIKit  
**Kind**: method

Sets the background image to use for the specified button state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setBackgroundImage(_ image: UIImage?, for state: UIControl.State)
```

#### Discussion

In general, if a property is not specified for a state, the default is to use the [`normal`](uicontrol/state-swift.struct/normal.md) value. If the [`normal`](uicontrol/state-swift.struct/normal.md) value is not set, then the property defaults to a system value. Therefore, at a minimum, you should set the value for the normal state.

## Parameters

- `image`: The background image to use for the specified state.
- `state`: The state that uses the specified image. The values are described in  .

## See Also

- [func backgroundImage(for: UIControl.State) -> UIImage?](uibutton/backgroundimage(for:).md)
  Returns the background image used for a button state.
- [func image(for: UIControl.State) -> UIImage?](uibutton/image(for:).md)
  Returns the image used for a button state.
- [func setImage(UIImage?, for: UIControl.State)](uibutton/setimage(_:for:).md)
  Sets the image to use for the specified state.
- [func preferredSymbolConfigurationForImage(in: UIControl.State) -> UIImage.SymbolConfiguration?](uibutton/preferredsymbolconfigurationforimage(in:).md)
  Returns the preferred symbol configuration for a button state.
- [func setPreferredSymbolConfiguration(UIImage.SymbolConfiguration?, forImageIn: UIControl.State)](uibutton/setpreferredsymbolconfiguration(_:forimagein:).md)
  Sets the preferred symbol configuration for a button state.
- [var tintColor: UIColor!](uibutton/tintcolor.md)
  The tint color to apply to the button title and image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/setbackgroundimage(_:for:))*