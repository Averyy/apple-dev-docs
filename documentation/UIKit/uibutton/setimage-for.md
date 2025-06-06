# setImage(_:for:)

**Framework**: UIKit  
**Kind**: method

Sets the image to use for the specified state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func setImage(_ image: UIImage?, for state: UIControl.State)
```

#### Discussion

At a minimum, always set an image for the [`normal`](uicontrol/state-swift.struct/normal.md) state when associating images to a button. If you don’t specify an image for the other states, the button uses the image associated with [`normal`](uicontrol/state-swift.struct/normal.md). If you don’t specify an image for the [`normal`](uicontrol/state-swift.struct/normal.md) state, the button uses a system value.

> ❗ **Important**:  When the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md) and [`behavioralStyle`](uibutton/behavioralstyle.md) is [`UIBehavioralStyle.mac`](uibehavioralstyle/mac.md), your app throws an exception if you use this method to set the image for any state other than [`normal`](uicontrol/state-swift.struct/normal.md).

 When the user interface idiom is [`UIUserInterfaceIdiom.mac`](uiuserinterfaceidiom/mac.md) and [`behavioralStyle`](uibutton/behavioralstyle.md) is [`UIBehavioralStyle.mac`](uibehavioralstyle/mac.md), your app throws an exception if you use this method to set the image for any state other than [`normal`](uicontrol/state-swift.struct/normal.md).

## Parameters

- `image`: The image to use for the specified state.
- `state`: The state that uses the specified image. The values are described in  .

## See Also

- [func backgroundImage(for: UIControl.State) -> UIImage?](uibutton/backgroundimage(for:).md)
  Returns the background image used for a button state.
- [func image(for: UIControl.State) -> UIImage?](uibutton/image(for:).md)
  Returns the image used for a button state.
- [func setBackgroundImage(UIImage?, for: UIControl.State)](uibutton/setbackgroundimage(_:for:).md)
  Sets the background image to use for the specified button state.
- [func preferredSymbolConfigurationForImage(in: UIControl.State) -> UIImage.SymbolConfiguration?](uibutton/preferredsymbolconfigurationforimage(in:).md)
  Returns the preferred symbol configuration for a button state.
- [func setPreferredSymbolConfiguration(UIImage.SymbolConfiguration?, forImageIn: UIControl.State)](uibutton/setpreferredsymbolconfiguration(_:forimagein:).md)
  Sets the preferred symbol configuration for a button state.
- [var tintColor: UIColor!](uibutton/tintcolor.md)
  The tint color to apply to the button title and image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/setimage(_:for:))*