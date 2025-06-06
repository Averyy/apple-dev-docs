# minimumScaleFactor

**Framework**: UIKit  
**Kind**: property

The minimum scale factor for the label’s text.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var minimumScaleFactor: CGFloat { get set }
```

#### Discussion

If the [`adjustsFontSizeToFitWidth`](uilabel/adjustsfontsizetofitwidth.md) is [`true`](https://developer.apple.com/documentation/swift/true), use this property to specify the smallest multiplier for the current font size that yields an acceptable font size for the label’s text. If you specify a value of `0` for this property, the label doesn’t scale the text down. The default value of this property is `0`.

To reveal the text field for editing minimum scale factor in Interface Builder, choose Minimum Font Scale from the Autoshrink pop-up menu in the label’s Attributes inspector.

## See Also

- [var adjustsFontSizeToFitWidth: Bool](uilabel/adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [var allowsDefaultTighteningForTruncation: Bool](uilabel/allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the label tightens text before truncating.
- [var baselineAdjustment: UIBaselineAdjustment](uilabel/baselineadjustment.md)
  An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [var numberOfLines: Int](uilabel/numberoflines.md)
  The maximum number of lines for rendering text.
- [var sizingRule: UILetterformAwareSizingRule](uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/minimumscalefactor)*