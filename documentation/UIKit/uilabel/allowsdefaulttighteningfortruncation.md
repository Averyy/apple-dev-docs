# allowsDefaultTighteningForTruncation

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the label tightens text before truncating.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allowsDefaultTighteningForTruncation: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the label tightens intercharacter spacing of its text before allowing any truncation to occur. The label determines the maximum amount of tightening automatically based on the font, current line width, line break mode, and other relevant information. This autoshrinking behavior is only intended for use with a single-line label.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var enablesMarqueeWhenAncestorFocused: Bool](uilabel/enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [var adjustsFontSizeToFitWidth: Bool](uilabel/adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [var baselineAdjustment: UIBaselineAdjustment](uilabel/baselineadjustment.md)
  An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [var minimumScaleFactor: CGFloat](uilabel/minimumscalefactor.md)
  The minimum scale factor for the label’s text.
- [var numberOfLines: Int](uilabel/numberoflines.md)
  The maximum number of lines for rendering text.
- [var sizingRule: UILetterformAwareSizingRule](uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/allowsdefaulttighteningfortruncation)*