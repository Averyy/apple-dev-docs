# currentAttributedTitle

**Framework**: UIKit  
**Kind**: property

The current styled title that is displayed on the button.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var currentAttributedTitle: NSAttributedString? { get }
```

#### Discussion

The value for this property reflects the title associated with the control’s current state. For states that do not have a custom title string associated with them, this method returns the attributed title that is currently displayed, which is typically the one associated with the [`normal`](uicontrol/state-swift.struct/normal.md) state.

## See Also

- [var buttonType: UIButton.ButtonType](uibutton/buttontype-swift.property.md)
  The button type.
- [var currentTitle: String?](uibutton/currenttitle.md)
  The current title that is displayed on the button.
- [var currentTitleColor: UIColor](uibutton/currenttitlecolor.md)
  The color used to display the title.
- [var currentTitleShadowColor: UIColor?](uibutton/currenttitleshadowcolor.md)
  The color of the title’s shadow.
- [var currentImage: UIImage?](uibutton/currentimage.md)
  The current image displayed on the button.
- [var currentBackgroundImage: UIImage?](uibutton/currentbackgroundimage.md)
  The current background image displayed on the button.
- [var currentPreferredSymbolConfiguration: UIImage.SymbolConfiguration?](uibutton/currentpreferredsymbolconfiguration.md)
  The current symbol size, style, and weight.
- [var imageView: UIImageView?](uibutton/imageview.md)
  The button’s image view.
- [var subtitleLabel: UILabel?](uibutton/subtitlelabel.md)
  The label that displays the text of the subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/currentattributedtitle)*