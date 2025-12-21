# limitsLayoutForSuspiciousContents

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- tvOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var limitsLayoutForSuspiciousContents: Bool { get set }
```

#### Discussion

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), which causes the layout manager to lay out whatever text you give it. Changing the value to [`true`](https://developer.apple.com/documentation/Swift/true) causes the layout manager to generate invalid layout information when it detects potentially suspicious content.

## See Also

- [var allowsNonContiguousLayout: Bool](nslayoutmanager/allowsnoncontiguouslayout.md)
  A Boolean value that indicates whether the layout manager allows noncontiguous layout.
- [var hasNonContiguousLayout: Bool](nslayoutmanager/hasnoncontiguouslayout.md)
  A Boolean value that indicates whether the layout manager currently has any areas of noncontiguous layout.
- [var showsInvisibleCharacters: Bool](nslayoutmanager/showsinvisiblecharacters.md)
  A Boolean value that indicates whether to substitute visible glyphs for whitespace and other typically invisible characters.
- [var showsControlCharacters: Bool](nslayoutmanager/showscontrolcharacters.md)
  A Boolean value that indicates whether the layout manager substitutes visible glyphs for control characters in the layout.
- [var usesFontLeading: Bool](nslayoutmanager/usesfontleading.md)
  A Boolean value that indicates whether the layout manager uses the leading of the font.
- [var backgroundLayoutEnabled: Bool](../AppKit/NSLayoutManager/backgroundLayoutEnabled.md)
  A Boolean value that indicates whether the layout manager generates glyphs and lays them out when the app’s run loop is idle.
- [var usesDefaultHyphenation: Bool](nslayoutmanager/usesdefaulthyphenation.md)
  A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/limitslayoutforsuspiciouscontents)*