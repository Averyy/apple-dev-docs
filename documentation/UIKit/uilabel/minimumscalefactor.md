# minimumScaleFactor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The minimum scale factor for the label’s text.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var minimumScaleFactor: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat minimumScaleFactor;
```

#### Discussion

If the [`adjustsFontSizeToFitWidth`](./adjustsfontsizetofitwidth.md) is [`true`](../../Swift/true.md), use this property to specify the smallest multiplier for the current font size that yields an acceptable font size for the label’s text. If you specify a value of `0` for this property, the label doesn’t scale the text down. The default value of this property is `0`.

To reveal the text field for editing minimum scale factor in Interface Builder, choose Minimum Font Scale from the Autoshrink pop-up menu in the label’s Attributes inspector.

## See Also

### Sizing the label’s text
- [var adjustsFontSizeToFitWidth: Bool](./adjustsfontsizetofitwidth.md)
  A Boolean value that determines whether the label reduces the text’s font size to fit the title string into the label’s bounding rectangle.
- [var allowsDefaultTighteningForTruncation: Bool](./allowsdefaulttighteningfortruncation.md)
  A Boolean value that determines whether the label tightens text before truncating.
- [var baselineAdjustment: UIBaselineAdjustment](./baselineadjustment.md)
  An option that controls whether the text’s baseline remains fixed when text needs to shrink to fit in the label.
- [var numberOfLines: Int](./numberoflines.md)
  The maximum number of lines for rendering text.
- [var sizingRule: UILetterformAwareSizingRule](../uiletterformawareadjusting/sizingrule.md)
  The typographic bounds-sizing behavior that handles text with fonts that contain oversize characters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilabel/minimumscalefactor)*