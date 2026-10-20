# limitsLayoutForSuspiciousContents

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.

**Availability**:
- macOS 10.14+

## Declaration

```swift
var limitsLayoutForSuspiciousContents: Bool { get set }
```

```objc
@property BOOL limitsLayoutForSuspiciousContents;
```

#### Discussion

The default value of this property is [`false`](../../Swift/false.md), which causes the layout manager to lay out whatever text you give it. Changing the value to [`true`](../../Swift/true.md) causes the layout manager to generate invalid layout information when it detects potentially suspicious content.

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
- [var usesDefaultHyphenation: Bool](./usesdefaulthyphenation.md)
  A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/limitslayoutforsuspiciouscontents)*