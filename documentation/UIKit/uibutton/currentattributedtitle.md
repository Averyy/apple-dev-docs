# currentAttributedTitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current styled title that is displayed on the button.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var currentAttributedTitle: NSAttributedString? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSAttributedString * currentAttributedTitle;
```

## Discussion

The value for this property reflects the title associated with the control’s current state. For states that do not have a custom title string associated with them, this method returns the attributed title that is currently displayed, which is typically the one associated with the [`normal`](../uicontrol/state-swift.struct/normal.md) state.

## See Also

### Getting the current state
- [var buttonType: UIButton.ButtonType](./buttontype-swift.property.md)
  The button type.
- [var currentTitle: String?](./currenttitle.md)
  The current title that is displayed on the button.
- [var currentTitleColor: UIColor](./currenttitlecolor.md)
  The color used to display the title.
- [var currentTitleShadowColor: UIColor?](./currenttitleshadowcolor.md)
  The color of the title’s shadow.
- [var currentImage: UIImage?](./currentimage.md)
  The current image displayed on the button.
- [var currentBackgroundImage: UIImage?](./currentbackgroundimage.md)
  The current background image displayed on the button.
- [var currentPreferredSymbolConfiguration: UIImage.SymbolConfiguration?](./currentpreferredsymbolconfiguration.md)
  The current symbol size, style, and weight.
- [var imageView: UIImageView?](./imageview.md)
  The button’s image view.
- [var subtitleLabel: UILabel?](./subtitlelabel.md)
  The label that displays the text of the subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/currentattributedtitle)*