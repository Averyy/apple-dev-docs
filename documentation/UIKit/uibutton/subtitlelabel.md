# subtitleLabel

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The label that displays the text of the subtitle.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var subtitleLabel: UILabel? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UILabel * subtitleLabel;
```

#### Discussion

If [`configuration`](./configuration-5rlyb.md) is `nil`, this property is `nil`.

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
- [var currentPreferredSymbolConfiguration: UIImage.SymbolConfiguration?](./currentpreferredsymbolconfiguration.md)
  The current symbol size, style, and weight.
- [var imageView: UIImageView?](./imageview.md)
  The button’s image view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/subtitlelabel)*