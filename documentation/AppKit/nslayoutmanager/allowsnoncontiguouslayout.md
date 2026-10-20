# allowsNonContiguousLayout

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the layout manager allows noncontiguous layout.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var allowsNonContiguousLayout: Bool { get set }
```

```objc
@property BOOL allowsNonContiguousLayout;
```

#### Discussion

For more information about noncontiguous layout, see [Noncontiguous Layout](../nslayoutmanager.md#Noncontiguous-Layout).

## See Also

### Configuring the global layout manager options
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
- [var usesDefaultHyphenation: Bool](./usesdefaulthyphenation.md)
  A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/allowsnoncontiguouslayout)*