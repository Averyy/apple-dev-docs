# title(for:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the title associated with the specified state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func title(for state: UIControl.State) -> String?
```

```objc
- (NSString *) titleForState:(UIControlState) state;
```

## Return Value

The title for the specified state. If no title has been set for the specific state, this method returns the title associated with the [`normal`](../uicontrol/state-swift.struct/normal.md) state.

## Parameters

- `state`: The state that uses the title. The possible values are described in [`UIControl.State`](../uicontrol/state-swift.struct.md).

## See Also

### Managing the title
- [var titleLabel: UILabel?](./titlelabel.md)
  A view that displays the value of the `currentTitle` property for a button.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/title(for:))*