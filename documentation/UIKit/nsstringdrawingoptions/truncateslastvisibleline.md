# truncatesLastVisibleLine

**Framework**: UIKit  
**Kind**: property

Truncates and adds the ellipsis character to the last visible line if the text doesn’t fit into the specified bounds.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static var truncatesLastVisibleLine: NSStringDrawingOptions { get }
```

#### Discussion

This option is ignored if `NSStringDrawingUsesLineFragmentOrigin` is not also set. In addition, the line break mode must be either `NSLineBreakByWordWrapping` or `NSLineBreakByCharWrapping` for this option to take effect. The line break mode can be specified in a paragraph style passed in the attributes dictionary argument of the drawing methods.

## See Also

- [static var usesLineFragmentOrigin: NSStringDrawingOptions](nsstringdrawingoptions/useslinefragmentorigin.md)
  Uses the line fragment origin instead of the baseline origin.
- [static var usesFontLeading: NSStringDrawingOptions](nsstringdrawingoptions/usesfontleading.md)
  Uses the font leading for calculating line heights.
- [static var usesDeviceMetrics: NSStringDrawingOptions](nsstringdrawingoptions/usesdevicemetrics.md)
  Uses image glyph bounds instead of typographic bounds.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nsstringdrawingoptions/truncateslastvisibleline)*