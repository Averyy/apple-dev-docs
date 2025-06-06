# zeroAdvancement

**Framework**: AppKit  
**Kind**: property

An action that removes the glyph from layout.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var zeroAdvancement: NSLayoutManager.ControlCharacterAction { get }
```

#### Discussion

Glyphs with this action are filtered out from layout ([`notShownAttribute(forGlyphAt:)`](nslayoutmanager/notshownattribute(forglyphat:).md) `== YES` for the glyph).

## See Also

- [static var containerBreak: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/containerbreak.md)
  An action that triggers a break in layout for the current container.
- [static var horizontalTab: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/horizontaltab.md)
  An action that inserts a horizontal tab.
- [static var lineBreak: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/linebreak.md)
  An action that causes a line break.
- [static var paragraphBreak: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/paragraphbreak.md)
  An action that causes a paragraph break.
- [static var whitespace: NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction/whitespace.md)
  An action that adds whitespace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/controlcharacteraction/zeroadvancement)*