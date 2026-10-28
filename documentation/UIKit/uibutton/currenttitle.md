# currentTitle

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The current title that is displayed on the button.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var currentTitle: String? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSString * currentTitle;
```

## Discussion

The value for this property is set automatically whenever the button state changes. For states that do not have a custom title string associated with them, this method returns the title that is currently displayed, which is typically the one associated with the [`normal`](../uicontrol/state-swift.struct/normal.md) state. The value may be `nil`.

## See Also

### Related Documentation
- [var titleLabel: UILabel?](./titlelabel.md)
  A view that displays the value of the `currentTitle` property for a button.
- [func setTitle(String?, for: UIControl.State)](./settitle%28_,for%29.md)
  Sets the title to use for the specified state.
### Getting the current state
- [var buttonType: UIButton.ButtonType](./buttontype-swift.property.md)
  The button type.
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
- [var subtitleLabel: UILabel?](./subtitlelabel.md)
  The label that displays the text of the subtitle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/currenttitle)*