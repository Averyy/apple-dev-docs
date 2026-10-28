# imageView

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The button’s image view.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var imageView: UIImageView? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIImageView * imageView;
```

## Discussion

Although this property is read-only, its own properties are read/write. Use these properties to configure the appearance and behavior of the button’s view. For example:

```objc
UIButton *button                   = [UIButton buttonWithType: UIButtonTypeSystem];
button.imageView.exclusiveTouch    = YES;
```

The `imageView` property returns a value even if the button has not been displayed yet. The value of the property is `nil` for system buttons.

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
- [var subtitleLabel: UILabel?](./subtitlelabel.md)
  The label that displays the text of the subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/imageview)*