# NSControlCharacterWhitespaceAction

**Framework**: UIKit  
**Kind**: var

An action that programmatically changes the white space around the glyph.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
var NSControlCharacterWhitespaceAction: Int { get }
```

#### Discussion

The width for a glyph with this action is determined by the delegate method [`layoutManager(_:boundingBoxForControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)`](nslayoutmanagerdelegate/layoutmanager(_:boundingboxforcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md) if the method is implemented; otherwise, it’s the same as `NSControlCharacterZeroAdvancementAction`.

## See Also

- [var NSControlCharacterContainerBreakAction: Int](nscontrolcharactercontainerbreakaction.md)
  A character that causes a break in layout.
- [var NSControlCharacterHorizontalTabAction: Int](nscontrolcharacterhorizontaltabaction.md)
  An action that inserts a horizontal tab.
- [var NSControlCharacterLineBreakAction: Int](nscontrolcharacterlinebreakaction.md)
  An action that causes a line break.
- [var NSControlCharacterParagraphBreakAction: Int](nscontrolcharacterparagraphbreakaction.md)
  An action that causes a paragraph break.
- [var NSControlCharacterZeroAdvancementAction: Int](nscontrolcharacterzeroadvancementaction.md)
  An action that removes the glyph from layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nscontrolcharacterwhitespaceaction)*