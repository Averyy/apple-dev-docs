# sizingRule

**Framework**: UIKit  
**Kind**: property  
**Required**: Yes

The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var sizingRule: UILetterformAwareSizingRule { get set }
```

#### Discussion

For more information on sizing behaviors, see [`UILetterformAwareAdjusting`](uiletterformawareadjusting.md).

## See Also

- [var adjustsFontSizeToFitWidth: Bool](uilabel/adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [var allowsDefaultTighteningForTruncation: Bool](uilabel/allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the label tightens text before truncating.
- [var baselineAdjustment: UIBaselineAdjustment](uilabel/baselineadjustment.md)
  An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [var minimumScaleFactor: CGFloat](uilabel/minimumscalefactor.md)
  The minimum scale factor for the label’s text.
- [var numberOfLines: Int](uilabel/numberoflines.md)
  The maximum number of lines for rendering text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiletterformawareadjusting/sizingrule)*