# baselineAdjustment

**Framework**: UIKit  
**Kind**: property

An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var baselineAdjustment: UIBaselineAdjustment { get set }
```

#### Discussion

If [`adjustsFontSizeToFitWidth`](uilabel/adjustsfontsizetofitwidth.md) is [`true`](https://developer.apple.com/documentation/Swift/true), this property controls the behavior of the text baselines in situations where the text needs the font size adjusted in order to fit. The default value of this property is [`UIBaselineAdjustment.alignBaselines`](uibaselineadjustment/alignbaselines.md). This property is effective only when the [`numberOfLines`](uilabel/numberoflines.md) is `1`.

## See Also

- [var adjustsFontSizeToFitWidth: Bool](uilabel/adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [var allowsDefaultTighteningForTruncation: Bool](uilabel/allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the label tightens text before truncating.
- [var minimumScaleFactor: CGFloat](uilabel/minimumscalefactor.md)
  The minimum scale factor for the label’s text.
- [var numberOfLines: Int](uilabel/numberoflines.md)
  The maximum number of lines for rendering text.
- [var sizingRule: UILetterformAwareSizingRule](uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/baselineadjustment)*