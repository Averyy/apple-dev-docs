# setTitle(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the title to use for the specified state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setTitle(_ title: String?, for state: UIControl.State)
```

```objc
- (void) setTitle:(NSString *) title forState:(UIControlState) state;
```

## Discussion

Use this method to set the title for the button. The title you specify derives its formatting from the button’s associated label object. If you set both a title and an attributed title for the button, the button prefers the use of the attributed title over this one.

At a minimum, set the value for the [`normal`](../uicontrol/state-swift.struct/normal.md) state. If you don’t specify a title for the other states, the button uses the title associated with the [`normal`](../uicontrol/state-swift.struct/normal.md) state. If you don’t set the value for [`normal`](../uicontrol/state-swift.struct/normal.md), then the property defaults to a system value.

> ❗ **Important**:  When the user interface idiom is [`UIUserInterfaceIdiom.mac`](../uiuserinterfaceidiom/mac.md) and [`behavioralStyle`](./behavioralstyle.md) is [`UIBehavioralStyle.mac`](../uibehavioralstyle/mac.md), your app throws an exception if you use this method to set the title for any state other than [`normal`](../uicontrol/state-swift.struct/normal.md).

## Parameters

- `title`: The title to use for the specified state.
- `state`: The state that uses the specified title. [`UIControl.State`](../uicontrol/state-swift.struct.md) describes the possible values.

## See Also

### Managing the title
- [var titleLabel: UILabel?](./titlelabel.md)
  A view that displays the value of the `currentTitle` property for a button.
- [func title(for: UIControl.State) -> String?](./title%28for%29.md)
  Returns the title associated with the specified state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/settitle(_:for:))*