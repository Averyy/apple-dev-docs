# hasNonContiguousLayout

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the layout manager currently has any areas of noncontiguous layout.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var hasNonContiguousLayout: Bool { get }
```

#### Discussion

There may be times at which there is no noncontiguous layout, such as when layout is complete; this method enables the layout manager to report that to clients.

For more information about noncontiguous layout, see [`Noncontiguous Layout`](nslayoutmanager#Noncontiguous-Layout.md).

## See Also

- [var allowsNonContiguousLayout: Bool](nslayoutmanager/allowsnoncontiguouslayout.md)
  A Boolean value that indicates whether the layout manager allows noncontiguous layout.
- [var showsInvisibleCharacters: Bool](nslayoutmanager/showsinvisiblecharacters.md)
  A Boolean value that indicates whether to substitute visible glyphs for whitespace and other typically invisible characters.
- [var showsControlCharacters: Bool](nslayoutmanager/showscontrolcharacters.md)
  A Boolean value that indicates whether the layout manager substitutes visible glyphs for control characters in the layout.
- [var usesFontLeading: Bool](nslayoutmanager/usesfontleading.md)
  A Boolean value that indicates whether the layout manager uses the leading of the font.
- [var backgroundLayoutEnabled: Bool](nslayoutmanager/backgroundlayoutenabled.md)
  A Boolean value that indicates whether the layout manager generates glyphs and lays them out when the app’s run loop is idle.
- [var limitsLayoutForSuspiciousContents: Bool](nslayoutmanager/limitslayoutforsuspiciouscontents.md)
  A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.
- [var usesDefaultHyphenation: Bool](nslayoutmanager/usesdefaulthyphenation.md)
  A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/hasnoncontiguouslayout)*