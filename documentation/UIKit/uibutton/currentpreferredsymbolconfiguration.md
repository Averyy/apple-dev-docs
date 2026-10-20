# currentPreferredSymbolConfiguration

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current symbol size, style, and weight.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var currentPreferredSymbolConfiguration: UIImage.SymbolConfiguration? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIImageSymbolConfiguration * currentPreferredSymbolConfiguration;
```

#### Discussion

This can be `nil` or `unspecifiedConfiguration`, which is essentially the same as `nil` but more explicit.

## See Also

### Getting the current state
- [var buttonType: UIButton.ButtonType](./buttontype-swift.property.md)
  The button type.
- [var currentTitle: String?](./currenttitle.md)
  The current title that is displayed on the button.
- [var currentAttributedTitle: NSAttributedString?](./currentattributedtitle.md)
  The current styled title that is displayed on the button.
- [var currentTitleColor: UIColor](./currenttitlecolor.md)
  The color used to display the title.
- [var currentTitleShadowColor: UIColor?](./currenttitleshadowcolor.md)
  The color of the title’s shadow.
- [var currentImage: UIImage?](./currentimage.md)
  The current image displayed on the button.
- [var currentBackgroundImage: UIImage?](./currentbackgroundimage.md)
  The current background image displayed on the button.
- [var imageView: UIImageView?](./imageview.md)
  The button’s image view.
- [var subtitleLabel: UILabel?](./subtitlelabel.md)
  The label that displays the text of the subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/currentpreferredsymbolconfiguration)*