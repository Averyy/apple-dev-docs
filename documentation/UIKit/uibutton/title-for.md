# title(for:)

**Framework**: UIKit  
**Kind**: method

Returns the title associated with the specified state.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func title(for state: UIControl.State) -> String?
```

#### Return Value

The title for the specified state. If no title has been set for the specific state, this method returns the title associated with the [`normal`](uicontrol/state-swift.struct/normal.md) state.

## Parameters

- `state`: The state that uses the title. The possible values are described in  .

## See Also

- [var titleLabel: UILabel?](uibutton/titlelabel.md)
  A view that displays the value of the `currentTitle` property for a button.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uibutton/title(for:))*