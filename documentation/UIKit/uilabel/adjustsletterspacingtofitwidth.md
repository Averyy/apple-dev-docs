# adjustsLetterSpacingToFitWidth

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the label adjusts spacing between letters to fit the string within the label’s bounds rectangle.

**Availability**:
- iOS 6.0+ - Deprecated in 7.0
- iPadOS 6.0+ - Deprecated in 7.0
- Mac Catalyst 13.1+ - Deprecated in 13.1

> **Deprecated**: Hand tune instead by using [`NSKernAttributeName`](../nskernattributename.md) to affect tracking.

## Declaration

```objc
@property (nonatomic) BOOL adjustsLetterSpacingToFitWidth;
```

## Discussion

When this property is [`true`](../../Swift/true.md), the label may alter the letter spacing of the text to make that text fit better within the label’s bounds. The label applies letter spacing to the text regardless of the current line break mode. The default value of this property is [`false`](../../Swift/false.md).

If this property’s value is [`true`](../../Swift/true.md), the label to ignore values value returned by the [`tighteningFactorForTruncation`](../../AppKit/nsparagraphstyle/tighteningfactorfortruncation.md) method of any [`NSParagraphStyle`](../nsparagraphstyle.md) objects associated with the label text.

> ❗ **Important**:  If this property’s value is [`true`](../../Swift/true.md), it’s a programmer error to set the [`lineBreakMode`](./linebreakmode.md) property to a value that causes text to wrap to another line.

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
- [minimumFontSize](./minimumfontsize.md)
  The size of the smallest permissible font when drawing the label’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/adjustsletterspacingtofitwidth)*