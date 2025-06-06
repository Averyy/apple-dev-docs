# backgroundImage(for:)

**Framework**: UIKit  
**Kind**: method

Returns the background image used for a button state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func backgroundImage(for state: UIControl.State) -> UIImage?
```

#### Return Value

The background image used for the specified state.

## Parameters

- `state`: The state that uses the background image. Possible values are described in  .

## See Also

- [func image(for: UIControl.State) -> UIImage?](uibutton/image(for:).md)
  Returns the image used for a button state.
- [func setBackgroundImage(UIImage?, for: UIControl.State)](uibutton/setbackgroundimage(_:for:).md)
  Sets the background image to use for the specified button state.
- [func setImage(UIImage?, for: UIControl.State)](uibutton/setimage(_:for:).md)
  Sets the image to use for the specified state.
- [func preferredSymbolConfigurationForImage(in: UIControl.State) -> UIImage.SymbolConfiguration?](uibutton/preferredsymbolconfigurationforimage(in:).md)
  Returns the preferred symbol configuration for a button state.
- [func setPreferredSymbolConfiguration(UIImage.SymbolConfiguration?, forImageIn: UIControl.State)](uibutton/setpreferredsymbolconfiguration(_:forimagein:).md)
  Sets the preferred symbol configuration for a button state.
- [var tintColor: UIColor!](uibutton/tintcolor.md)
  The tint color to apply to the button title and image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/backgroundimage(for:))*