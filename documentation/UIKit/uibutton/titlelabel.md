# titleLabel

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A view that displays the value of the `currentTitle` property for a button.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var titleLabel: UILabel? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UILabel * titleLabel;
```

## Discussion

Although this property is read-only, its own properties are read/write. Use these properties primarily to configure the text of the button. For example:

```objc
UIButton *button                  = [UIButton buttonWithType: UIButtonTypeSystem];
button.titleLabel.font            = [UIFont systemFontOfSize: 12];
button.titleLabel.lineBreakMode   = NSLineBreakByTruncatingTail;
```

Do not use the label object to set the text color or the shadow color. Instead, use the [`setTitleColor(_:for:)`](./settitlecolor%28_,for%29.md) and [`setTitleShadowColor(_:for:)`](./settitleshadowcolor%28_,for%29.md) methods of this class to make those changes. To set the actual text of the label, use [`setTitle(_:for:)`](./settitle%28_,for%29.md) (`button.titleLabel.text` does not let you set the text).

The `titleLabel` property returns a value even if the button has not been displayed yet. The value of the property is  `nil` for system buttons.

## See Also

### Related Documentation
- [var currentTitle: String?](./currenttitle.md)
  The current title that is displayed on the button.
### Managing the title
- [func title(for: UIControl.State) -> String?](./title%28for%29.md)
  Returns the title associated with the specified state.
- [func setTitle(String?, for: UIControl.State)](./settitle%28_,for%29.md)
  Sets the title to use for the specified state.
- [func attributedTitle(for: UIControl.State) -> NSAttributedString?](./attributedtitle%28for%29.md)
  Returns the styled title associated with the specified state.
- [func setAttributedTitle(NSAttributedString?, for: UIControl.State)](./setattributedtitle%28_,for%29.md)
  Sets the styled title to use for the specified state.
- [func titleColor(for: UIControl.State) -> UIColor?](./titlecolor%28for%29.md)
  Returns the title color used for a state.
- [func setTitleColor(UIColor?, for: UIControl.State)](./settitlecolor%28_,for%29.md)
  Sets the color of the title to use for the specified state.
- [func titleShadowColor(for: UIControl.State) -> UIColor?](./titleshadowcolor%28for%29.md)
  Returns the shadow color of the title used for a state.
- [func setTitleShadowColor(UIColor?, for: UIControl.State)](./settitleshadowcolor%28_,for%29.md)
  Sets the color of the title shadow to use for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/titlelabel)*