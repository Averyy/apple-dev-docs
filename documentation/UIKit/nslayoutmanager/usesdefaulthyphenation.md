# usesDefaultHyphenation

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var usesDefaultHyphenation: Bool { get set }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the layout manager makes a best-effort attempt to hyphenate text when wrapping lines. You may override this hyphenation behavior on a per-paragraph basis using the [`hyphenationFactor`](nsparagraphstyle/hyphenationfactor.md) property of [`NSParagraphStyle`](nsparagraphstyle.md) The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false), which prevents the layout manager from hyphenating text.

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
- [var limitsLayoutForSuspiciousContents: Bool](nslayoutmanager/limitslayoutforsuspiciouscontents.md)
  A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/usesdefaulthyphenation)*