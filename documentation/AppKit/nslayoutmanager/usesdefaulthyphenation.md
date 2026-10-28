# usesDefaultHyphenation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var usesDefaultHyphenation: Bool { get set }
```

```objc
@property BOOL usesDefaultHyphenation;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the layout manager makes a best-effort attempt to hyphenate text when wrapping lines. You may override this hyphenation behavior on a per-paragraph basis using the [`hyphenationFactor`](./hyphenationfactor.md) property of [`NSParagraphStyle`](../nsparagraphstyle.md) The default value of this property is [`false`](../../Swift/false.md), which prevents the layout manager from hyphenating text.

## See Also

### Configuring the global layout manager options
- [var allowsNonContiguousLayout: Bool](./allowsnoncontiguouslayout.md)
  A Boolean value that indicates whether the layout manager allows noncontiguous layout.
- [var hasNonContiguousLayout: Bool](./hasnoncontiguouslayout.md)
  A Boolean value that indicates whether the layout manager currently has any areas of noncontiguous layout.
- [var showsInvisibleCharacters: Bool](./showsinvisiblecharacters.md)
  A Boolean value that indicates whether to substitute visible glyphs for whitespace and other typically invisible characters.
- [var showsControlCharacters: Bool](./showscontrolcharacters.md)
  A Boolean value that indicates whether the layout manager substitutes visible glyphs for control characters in the layout.
- [var usesFontLeading: Bool](./usesfontleading.md)
  A Boolean value that indicates whether the layout manager uses the leading of the font.
- [var backgroundLayoutEnabled: Bool](./backgroundlayoutenabled.md)
  A Boolean value that indicates whether the layout manager generates glyphs and lays them out when the app’s run loop is idle.
- [var limitsLayoutForSuspiciousContents: Bool](./limitslayoutforsuspiciouscontents.md)
  A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/usesdefaulthyphenation)*