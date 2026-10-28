# NSControlCharacterZeroAdvancementAction

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

An action that removes the glyph from layout.

**Availability**:
- iOS 7.0+ - Deprecated in 9.0 (renamed: NSLayoutManager.ControlCharacterAction.zeroAdvancement)
- iPadOS 7.0+ - Deprecated in 9.0 (renamed: NSLayoutManager.ControlCharacterAction.zeroAdvancement)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: NSLayoutManager.ControlCharacterAction.zeroAdvancement)
- tvOS - Deprecated in 9.0 (renamed: NSLayoutManager.ControlCharacterAction.zeroAdvancement)

## Declaration

```swift
var NSControlCharacterZeroAdvancementAction: Int { get }
```

```c
NSControlCharacterZeroAdvancementAction
```

## Discussion

Glyphs with this action are filtered out from layout ([`notShownAttribute(forGlyphAt:)`](./nslayoutmanager/notshownattribute%28forglyphat%29.md) `== YES` for the glyph).

## See Also

### Deprecated symbols
- [var NSControlCharacterContainerBreakAction: Int](./nscontrolcharactercontainerbreakaction.md)
  A character that causes a break in layout.
- [var NSControlCharacterHorizontalTabAction: Int](./nscontrolcharacterhorizontaltabaction.md)
  An action that inserts a horizontal tab.
- [var NSControlCharacterLineBreakAction: Int](./nscontrolcharacterlinebreakaction.md)
  An action that causes a line break.
- [var NSControlCharacterParagraphBreakAction: Int](./nscontrolcharacterparagraphbreakaction.md)
  An action that causes a paragraph break.
- [var NSControlCharacterWhitespaceAction: Int](./nscontrolcharacterwhitespaceaction.md)
  An action that programmatically changes the white space around the glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscontrolcharacterzeroadvancementaction)*