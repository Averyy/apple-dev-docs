# setTitleShadowColor(_:for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the color of the title shadow to use for the specified state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setTitleShadowColor(_ color: UIColor?, for state: UIControl.State)
```

```objc
- (void) setTitleShadowColor:(UIColor *) color forState:(UIControlState) state;
```

#### Discussion

In general, if a property is not specified for a state, the default is to use the [`normal`](../uicontrol/state-swift.struct/normal.md) value. If the [`normal`](../uicontrol/state-swift.struct/normal.md) value is not set, then the property defaults to a system value. Therefore, at a minimum, you should set the value for the normal state.

## Parameters

- `color`: The color of the title shadow to use for the specified state.
- `state`: The state that uses the specified color. The possible values are described in [`UIControl.State`](../uicontrol/state-swift.struct.md).

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
- [func setAttributedTitle(NSAttributedString?, for: UIControl.State)](./setattributedtitle%28_,for%29.md)
  Sets the styled title to use for the specified state.
- [func titleColor(for: UIControl.State) -> UIColor?](./titlecolor%28for%29.md)
  Returns the title color used for a state.
- [func setTitleColor(UIColor?, for: UIControl.State)](./settitlecolor%28_,for%29.md)
  Sets the color of the title to use for the specified state.
- [func titleShadowColor(for: UIControl.State) -> UIColor?](./titleshadowcolor%28for%29.md)
  Returns the shadow color of the title used for a state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/settitleshadowcolor(_:for:))*