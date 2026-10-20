# zeroAdvancement

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

An action that removes the glyph from layout.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
static var zeroAdvancement: NSLayoutManager.ControlCharacterAction { get }
```

```c
NSControlCharacterActionZeroAdvancement
```

#### Discussion

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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/controlcharacteraction/zeroadvancement)*