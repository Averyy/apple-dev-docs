# adjustsFontSizeToFitWidth

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var adjustsFontSizeToFitWidth: Bool { get set }
```

```objc
@property (nonatomic) BOOL adjustsFontSizeToFitWidth;
```

#### Discussion

Normally, the label draws the text with the font you specify in the [`font`](./font.md) property. If this property is [`true`](../../Swift/true.md), and the text in the [`text`](./text.md) property exceeds the label’s bounding rectangle, the label reduces the font size until the text fits or it has scaled the font down to the minimum font size. The default value for this property is [`false`](../../Swift/false.md). If you change it to [`true`](../../Swift/true.md), be sure that you also set an appropriate minimum font scale by modifying the [`minimumScaleFactor`](./minimumscalefactor.md) property. This autoshrinking behavior is only intended for use with a single-line label.

To enable [`adjustsFontSizeToFitWidth`](./adjustsfontsizetofitwidth.md) in Interface Builder, choose Minimum Font Scale from the Autoshrink pop-up menu in the label’s Attributes inspector.

## See Also

### Related Documentation
- [var font: UIFont!](./font.md)
  The font of the text.
- [var enablesMarqueeWhenAncestorFocused: Bool](./enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
- [minimumFontSize](./minimumfontsize.md)
  The size of the smallest permissible font when drawing the label’s text.
### Sizing the label’s text
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/adjustsfontsizetofitwidth)*