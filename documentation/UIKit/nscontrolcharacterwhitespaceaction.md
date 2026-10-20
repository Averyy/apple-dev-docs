# NSControlCharacterWhitespaceAction

**Framework**: UIKit  
**Kind**: var  
**Role**: Global Variable

An action that programmatically changes the white space around the glyph.

**Availability**:
- iOS 7.0+ - Deprecated in 9.0 (renamed: NSLayoutManager.ControlCharacterAction.whitespace)
- iPadOS 7.0+ - Deprecated in 9.0 (renamed: NSLayoutManager.ControlCharacterAction.whitespace)
- Mac Catalyst 13.1+ - Deprecated in 13.1 (renamed: NSLayoutManager.ControlCharacterAction.whitespace)
- tvOS - Deprecated in 9.0 (renamed: NSLayoutManager.ControlCharacterAction.whitespace)

## Declaration

```swift
var NSControlCharacterWhitespaceAction: Int { get }
```

```c
NSControlCharacterWhitespaceAction
```

#### Discussion

The width for a glyph with this action is determined by the delegate method [`layoutManager(_:boundingBoxForControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)`](./nslayoutmanagerdelegate/layoutmanager%28_,boundingboxforcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md) if the method is implemented; otherwise, it’s the same as `NSControlCharacterZeroAdvancementAction`.

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
- [var NSControlCharacterZeroAdvancementAction: Int](./nscontrolcharacterzeroadvancementaction.md)
  An action that removes the glyph from layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscontrolcharacterwhitespaceaction)*