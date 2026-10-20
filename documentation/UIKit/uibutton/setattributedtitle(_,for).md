# setAttributedTitle(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the styled title to use for the specified state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setAttributedTitle(_ title: NSAttributedString?, for state: UIControl.State)
```

```objc
- (void) setAttributedTitle:(NSAttributedString *) title forState:(UIControlState) state;
```

#### Discussion

Use this method to set the title of the button, including any relevant formatting information. If you set both a title and an attributed title for the button, the button prefers the use of the attributed title.

At a minimum, you should set the value for the normal state. If a title is not specified for a state, the default behavior is to use the title associated with the [`normal`](../uicontrol/state-swift.struct/normal.md) state. If the value for [`normal`](../uicontrol/state-swift.struct/normal.md) is not set, then the property defaults to a system value.

## Parameters

- `title`: The styled text string so use for the title.
- `state`: The state that uses the specified title. The possible values are described in [`UIControl.State`](../uicontrol/state-swift.struct.md).

## See Also

### Managing the title
- [var titleLabel: UILabel?](./titlelabel.md)
  A view that displays the value of the `currentTitle` property for a button.
- [func title(for: UIControl.State) -> String?](./title%28for%29.md)
  Returns the title associated with the specified state.
- [func setTitle(String?, for: UIControl.State)](./settitle%28_,for%29.md)
  Sets the title to use for the specified state.
- [func attributedTitle(for: UIControl.State) -> NSAttributedString?](./attributedtitle%28for%29.md)
  Returns the styled title associated with the specified state.
- [func titleColor(for: UIControl.State) -> UIColor?](./titlecolor%28for%29.md)
  Returns the title color used for a state.
- [func setTitleColor(UIColor?, for: UIControl.State)](./settitlecolor%28_,for%29.md)
  Sets the color of the title to use for the specified state.
- [func titleShadowColor(for: UIControl.State) -> UIColor?](./titleshadowcolor%28for%29.md)
  Returns the shadow color of the title used for a state.
- [func setTitleShadowColor(UIColor?, for: UIControl.State)](./settitleshadowcolor%28_,for%29.md)
  Sets the color of the title shadow to use for the specified state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/setattributedtitle(_:for:))*