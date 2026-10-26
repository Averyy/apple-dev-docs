# allowsDefaultTighteningForTruncation

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that determines whether the label tightens text before truncating.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var allowsDefaultTighteningForTruncation: Bool { get set }
```

```objc
@property (nonatomic) BOOL allowsDefaultTighteningForTruncation;
```

#### Discussion

When the value of this property is [`true`](../../Swift/true.md), the label tightens intercharacter spacing of its text before allowing any truncation to occur. The label determines the maximum amount of tightening automatically based on the font, current line width, line break mode, and other relevant information. This autoshrinking behavior is only intended for use with a single-line label.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Related Documentation
- [var enablesMarqueeWhenAncestorFocused: Bool](./enablesmarqueewhenancestorfocused.md)
  A Boolean value that determines whether the label scrolls its text while one of its containing views has focus.
### Sizing the label’s text
- [var adjustsFontSizeToFitWidth: Bool](./adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
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
- [minimumFontSize](./minimumfontsize.md)
  The size of the smallest permissible font when drawing the label’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/allowsdefaulttighteningfortruncation)*