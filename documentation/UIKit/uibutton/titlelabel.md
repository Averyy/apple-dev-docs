# titleLabel

**Framework**: UIKit  
**Kind**: property

A view that displays the value of the `currentTitle` property for a button.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var titleLabel: UILabel? { get }
```

#### Discussion

Although this property is read-only, its own properties are read/write. Use these properties primarily to configure the text of the button. For example:

```objc
UIButton *button                  = [UIButton buttonWithType: UIButtonTypeSystem];
button.titleLabel.font            = [UIFont systemFontOfSize: 12];
button.titleLabel.lineBreakMode   = NSLineBreakByTruncatingTail;
```

Do not use the label object to set the text color or the shadow color. Instead, use the [`setTitleColor(_:for:)`](uibutton/settitlecolor(_:for:).md) and [`setTitleShadowColor(_:for:)`](uibutton/settitleshadowcolor(_:for:).md) methods of this class to make those changes. To set the actual text of the label, use [`setTitle(_:for:)`](uibutton/settitle(_:for:).md) (`button.titleLabel.text` does not let you set the text).

The `titleLabel` property returns a value even if the button has not been displayed yet. The value of the property is  `nil` for system buttons.

## See Also

- [var currentTitle: String?](uibutton/currenttitle.md)
  The current title that is displayed on the button.
- [func title(for: UIControl.State) -> String?](uibutton/title(for:).md)
  Returns the title associated with the specified state.
- [func setTitle(String?, for: UIControl.State)](uibutton/settitle(_:for:).md)
  Sets the title to use for the specified state.
- [func attributedTitle(for: UIControl.State) -> NSAttributedString?](uibutton/attributedtitle(for:).md)
  Returns the styled title associated with the specified state.
- [func setAttributedTitle(NSAttributedString?, for: UIControl.State)](uibutton/setattributedtitle(_:for:).md)
  Sets the styled title to use for the specified state.
- [func titleColor(for: UIControl.State) -> UIColor?](uibutton/titlecolor(for:).md)
  Returns the title color used for a state.
- [func setTitleColor(UIColor?, for: UIControl.State)](uibutton/settitlecolor(_:for:).md)
  Sets the color of the title to use for the specified state.
- [func titleShadowColor(for: UIControl.State) -> UIColor?](uibutton/titleshadowcolor(for:).md)
  Returns the shadow color of the title used for a state.
- [func setTitleShadowColor(UIColor?, for: UIControl.State)](uibutton/settitleshadowcolor(_:for:).md)
  Sets the color of the title shadow to use for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/titlelabel)*