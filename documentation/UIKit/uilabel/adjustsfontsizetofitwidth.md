# adjustsFontSizeToFitWidth

**Framework**: UIKit  
**Kind**: property

A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var adjustsFontSizeToFitWidth: Bool { get set }
```

#### Discussion

Normally, the label draws the text with the font you specify in the [`font`](uilabel/font.md) property. If this property is [`true`](https://developer.apple.com/documentation/Swift/true), and the text in the [`text`](uilabel/text.md) property exceeds the label’s bounding rectangle, the label reduces the font size until the text fits or it has scaled the font down to the minimum font size. The default value for this property is [`false`](https://developer.apple.com/documentation/Swift/false). If you change it to [`true`](https://developer.apple.com/documentation/Swift/true), be sure that you also set an appropriate minimum font scale by modifying the [`minimumScaleFactor`](uilabel/minimumscalefactor.md) property. This autoshrinking behavior is only intended for use with a single-line label.

To enable [`adjustsFontSizeToFitWidth`](uilabel/adjustsfontsizetofitwidth.md) in Interface Builder, choose Minimum Font Scale from the Autoshrink pop-up menu in the label’s Attributes inspector.

## See Also

- [var font: UIFont!](uilabel/font.md)
  The font of the text.
- [var enablesMarqueeWhenAncestorFocused: Bool](uilabel/enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [var allowsDefaultTighteningForTruncation: Bool](uilabel/allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the label tightens text before truncating.
- [var baselineAdjustment: UIBaselineAdjustment](uilabel/baselineadjustment.md)
  An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [var minimumScaleFactor: CGFloat](uilabel/minimumscalefactor.md)
  The minimum scale factor for the label’s text.
- [var numberOfLines: Int](uilabel/numberoflines.md)
  The maximum number of lines for rendering text.
- [var sizingRule: UILetterformAwareSizingRule](uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/adjustsfontsizetofitwidth)*