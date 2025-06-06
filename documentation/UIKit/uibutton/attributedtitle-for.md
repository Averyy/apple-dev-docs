# attributedTitle(for:)

**Framework**: UIKit  
**Kind**: method

Returns the styled title associated with the specified state.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func attributedTitle(for state: UIControl.State) -> NSAttributedString?
```

#### Return Value

The title for the specified state. If no attributed title has been set for the specific state, this method returns the attributed title associated with the [`normal`](uicontrol/state-swift.struct/normal.md) state. If no attributed title has been set for [`normal`](uicontrol/state-swift.struct/normal.md), returns `nil`.

## Parameters

- `state`: The state that uses the styled title. The possible values are described in  .

## See Also

- [var titleLabel: UILabel?](uibutton/titlelabel.md)
  A view that displays the value of the `currentTitle` property for a button.
- [func title(for: UIControl.State) -> String?](uibutton/title(for:).md)
  Returns the title associated with the specified state.
- [func setTitle(String?, for: UIControl.State)](uibutton/settitle(_:for:).md)
  Sets the title to use for the specified state.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/attributedtitle(for:))*