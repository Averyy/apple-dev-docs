# zeroAdvancement

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

An action that removes the glyph from layout.

**Availability**:
- macOS 10.11+

## Declaration

```swift
static var zeroAdvancement: NSLayoutManager.ControlCharacterAction { get }
```

```c
NSControlCharacterActionZeroAdvancement
```

## Discussion

Glyphs with this action are filtered out from layout ([`notShownAttribute(forGlyphAt:)`](../notshownattribute%28forglyphat%29.md) `== YES` for the glyph).

## See Also

### Actions
- [static var containerBreak: NSLayoutManager.ControlCharacterAction](./containerbreak.md)
  An action that triggers a break in layout for the current container.
- [static var horizontalTab: NSLayoutManager.ControlCharacterAction](./horizontaltab.md)
  An action that inserts a horizontal tab.
- [static var lineBreak: NSLayoutManager.ControlCharacterAction](./linebreak.md)
  An action that causes a line break.
- [static var paragraphBreak: NSLayoutManager.ControlCharacterAction](./paragraphbreak.md)
  An action that causes a paragraph break.
- [static var whitespace: NSLayoutManager.ControlCharacterAction](./whitespace.md)
  An action that adds whitespace.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/controlcharacteraction/zeroadvancement)*