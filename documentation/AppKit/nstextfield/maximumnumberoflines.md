# maximumNumberOfLines

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The maximum number of lines a wrapping text field displays before clipping or truncating the text.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var maximumNumberOfLines: Int { get set }
```

```objc
@property NSInteger maximumNumberOfLines;
```

#### Discussion

The default value of `0` indicates no limit to the number of lines, and the text fills the bounds of the text field cell.

If the text field reaches the maximum number of lines, or if the height of the container can’t accommodate the number of lines, the text field clips or truncates the text, depending on the cell’s [`truncatesLastVisibleLine`](../nscell/truncateslastvisibleline.md) setting.

> ❗ **Important**:  This value also affects [`sizeThatFits(_:)`](../nscontrol/sizethatfits%28_%29.md), [`fittingSize`](../nsview/fittingsize.md), and [`intrinsicContentSize`](../nsview/intrinsiccontentsize.md). If the value of this property isn’t `1`, the text field may use multiple lines to determine its intrinsic content size.

## See Also

### Configuring line wrapping
- [var lineBreakStrategy: NSParagraphStyle.LineBreakStrategy](./linebreakstrategy.md)
  The strategy that the system uses to break lines when laying out multiple lines of text.
- [var allowsDefaultTighteningForTruncation: Bool](./allowsdefaulttighteningfortruncation.md)
  A Boolean value that controls whether single-line text fields tighten intercharacter spacing before truncating the text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextfield/maximumnumberoflines)*