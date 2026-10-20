# currentTitleColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The color used to display the title.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var currentTitleColor: UIColor { get }
```

```objc
@property (nonatomic, strong, readonly) UIColor * currentTitleColor;
```

#### Discussion

This value is guaranteed not to be `nil`. The default value is `white`.

## See Also

### Getting the current state
- [var buttonType: UIButton.ButtonType](./buttontype-swift.property.md)
  The button type.
- [var currentTitle: String?](./currenttitle.md)
  The current title that is displayed on the button.
- [var currentAttributedTitle: NSAttributedString?](./currentattributedtitle.md)
  The current styled title that is displayed on the button.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/currenttitlecolor)*