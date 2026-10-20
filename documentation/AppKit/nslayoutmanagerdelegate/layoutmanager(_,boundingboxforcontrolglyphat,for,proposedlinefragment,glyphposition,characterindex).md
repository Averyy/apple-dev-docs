# layoutManager(_:boundingBoxForControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the bounding rectangle for the specified control glyph with the specified parameters.

**Availability**:
- macOS 10.11+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, boundingBoxForControlGlyphAt glyphIndex: Int, for textContainer: NSTextContainer, proposedLineFragment proposedRect: NSRect, glyphPosition: NSPoint, characterIndex charIndex: Int) -> NSRect
```

```objc
- (NSRect) layoutManager:(NSLayoutManager *) layoutManager boundingBoxForControlGlyphAtIndex:(NSUInteger) glyphIndex forTextContainer:(NSTextContainer *) textContainer proposedLineFragment:(NSRect) proposedRect glyphPosition:(NSPoint) glyphPosition characterIndex:(NSUInteger) charIndex;
```

#### Return Value

The bounding rectangle for the specified control glyph with the specified parameters.

#### Discussion

Sent for resolving the glyph metrics for [`NSControlCharacterWhitespaceAction`](../../UIKit/nscontrolcharacterwhitespaceaction.md) control character.

## Parameters

- `layoutManager`: The layout manager doing the layout.
- `glyphIndex`: The index of the control glyph in question.
- `textContainer`: The text container to use to calculate the position.
- `proposedRect`: The proposed line fragment rectangle.
- `glyphPosition`: The position of the glyph in `textContainer`.
- `charIndex`: The character index in `textContainer`.

## See Also

### Handling line fragments
- [func layoutManager(NSLayoutManager, shouldBreakLineByHyphenatingBeforeCharacterAt: Int) -> Bool](./layoutmanager%28_,shouldbreaklinebyhyphenatingbeforecharacterat%29.md)
  Asks the delegate whether to break the line at the specified character.
- [func layoutManager(NSLayoutManager, shouldBreakLineByWordBeforeCharacterAt: Int) -> Bool](./layoutmanager%28_,shouldbreaklinebywordbeforecharacterat%29.md)
  Asks the delegate whether to break the line at the specified word.
- [func layoutManager(NSLayoutManager, lineSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./layoutmanager%28_,linespacingafterglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add to the end of a line.
- [func layoutManager(NSLayoutManager, paragraphSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./layoutmanager%28_,paragraphspacingafterglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add at the end of a paragraph.
- [func layoutManager(NSLayoutManager, paragraphSpacingBeforeGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./layoutmanager%28_,paragraphspacingbeforeglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add at the beginning of a paragraph.
- [func layoutManager(NSLayoutManager, shouldSetLineFragmentRect: UnsafeMutablePointer<NSRect>, lineFragmentUsedRect: UnsafeMutablePointer<NSRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, in: NSTextContainer, forGlyphRange: NSRange) -> Bool](./layoutmanager%28_,shouldsetlinefragmentrect,linefragmentusedrect,baselineoffset,in,forglyphrange%29.md)
  Customizes the line fragment geometry before committing it to the layout cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/layoutmanager(_:boundingboxforcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:))*