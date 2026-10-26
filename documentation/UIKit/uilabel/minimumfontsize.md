# minimumFontSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The size of the smallest permissible font when drawing the label’s text.

**Availability**:
- iOS 2.0+ - Deprecated in 6.0
- iPadOS 2.0+ - Deprecated in 6.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Use [`minimumScaleFactor`](./minimumscalefactor.md) instead.

## Declaration

```objc
@property (nonatomic) CGFloat minimumFontSize;
```

#### Discussion

When drawing text that might not fit within the bounding rectangle of the label, you can use this property to prevent the label from reducing the font size to a point where it’s no longer legible.

The default value for this property is `0.0`. If you enable font adjustment for the label, you should always increase this value. This property is effective only when the [`numberOfLines`](./numberoflines.md) is `1`.

## See Also

### Sizing the label’s text
- [var adjustsFontSizeToFitWidth: Bool](./adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [var allowsDefaultTighteningForTruncation: Bool](./allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the label tightens text before truncating.
- [var baselineAdjustment: UIBaselineAdjustment](./baselineadjustment.md)
  An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [var minimumScaleFactor: CGFloat](./minimumscalefactor.md)
  The minimum scale factor for the label’s text.
- [var numberOfLines: Int](./numberoflines.md)
  The maximum number of lines for rendering text.
- [var sizingRule: UILetterformAwareSizingRule](../uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
- [adjustsLetterSpacingToFitWidth](./adjustsletterspacingtofitwidth.md)
  A Boolean value that indicates whether the label adjusts spacing between letters to fit the string within the label’s bounds rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/minimumfontsize)*