# numberOfLines

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of lines for rendering text.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var numberOfLines: Int { get set }
```

```objc
@property (nonatomic) NSInteger numberOfLines;
```

#### Discussion

This property controls the maximum number of lines to use in order to fit the label’s text into its bounding rectangle. The default value for this property is `1`. To remove any maximum limit, and use as many lines as needed, set the value of this property to `0`.

If you constrain your text using this property, the label truncates any text that doesn’t fit within the maximum number of lines and inside the bounding rectangle. To specify which part of the text the label should truncate, set the [`lineBreakMode`](./linebreakmode.md) property.

When the [`sizeToFit()`](../uiview/sizetofit%28%29.md) method resizes a label, resizing takes into account the value stored in this property. For example, if the number of lines is `3`, the [`sizeToFit()`](../uiview/sizetofit%28%29.md) method resizes the label so that it’s big enough to display three lines of text in the current font.

## See Also

### Related Documentation
- [func sizeToFit()](../uiview/sizetofit%28%29.md)
  Resizes and moves the receiver view so it just encloses its subviews.
- [var isEnabled: Bool](./isenabled.md)
  A Boolean value that determines whether the label draws its text in an enabled state.
### Sizing the label’s text
- [var adjustsFontSizeToFitWidth: Bool](./adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [var allowsDefaultTighteningForTruncation: Bool](./allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the label tightens text before truncating.
- [var baselineAdjustment: UIBaselineAdjustment](./baselineadjustment.md)
  An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [var minimumScaleFactor: CGFloat](./minimumscalefactor.md)
  The minimum scale factor for the label’s text.
- [var sizingRule: UILetterformAwareSizingRule](../uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.
- [adjustsLetterSpacingToFitWidth](./adjustsletterspacingtofitwidth.md)
  A Boolean value that indicates whether the label adjusts spacing between letters to fit the string within the label’s bounds rectangle.
- [minimumFontSize](./minimumfontsize.md)
  The size of the smallest permissible font when drawing the label’s text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/numberoflines)*