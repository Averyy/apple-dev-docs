# attributedTitle(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the styled title associated with the specified state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func attributedTitle(for state: UIControl.State) -> NSAttributedString?
```

```objc
- (NSAttributedString *) attributedTitleForState:(UIControlState) state;
```

## Return Value

The title for the specified state. If no attributed title has been set for the specific state, this method returns the attributed title associated with the [`normal`](../uicontrol/state-swift.struct/normal.md) state. If no attributed title has been set for [`normal`](../uicontrol/state-swift.struct/normal.md), returns `nil`.

## Parameters

- `state`: The state that uses the styled title. The possible values are described in [`UIControl.State`](../uicontrol/state-swift.struct.md).

## See Also

### Managing the title
- [var titleLabel: UILabel?](./titlelabel.md)
  A view that displays the value of the `currentTitle` property for a button.
- [func title(for: UIControl.State) -> String?](./title%28for%29.md)
  Returns the title associated with the specified state.
- [func setTitle(String?, for: UIControl.State)](./settitle%28_,for%29.md)
  Sets the title to use for the specified state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/attributedtitle(for:))*