# layoutManager(_:boundingBoxForControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns the bounding rectangle for the specified control glyph with the specified parameters.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, boundingBoxForControlGlyphAt glyphIndex: Int, for textContainer: NSTextContainer, proposedLineFragment proposedRect: CGRect, glyphPosition: CGPoint, characterIndex charIndex: Int) -> CGRect
```

```objc
- (CGRect) layoutManager:(NSLayoutManager *) layoutManager boundingBoxForControlGlyphAtIndex:(NSUInteger) glyphIndex forTextContainer:(NSTextContainer *) textContainer proposedLineFragment:(CGRect) proposedRect glyphPosition:(CGPoint) glyphPosition characterIndex:(NSUInteger) charIndex;
```

## Return Value

The bounding rectangle for the specified control glyph with the specified parameters.

## Discussion

Sent for resolving the glyph metrics for [`NSControlCharacterWhitespaceAction`](../nscontrolcharacterwhitespaceaction.md) control character.

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
- [func layoutManager(NSLayoutManager, lineSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: CGRect) -> CGFloat](./layoutmanager%28_,linespacingafterglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add to the end of a line.
- [func layoutManager(NSLayoutManager, paragraphSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: CGRect) -> CGFloat](./layoutmanager%28_,paragraphspacingafterglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add at the end of a paragraph.
- [func layoutManager(NSLayoutManager, paragraphSpacingBeforeGlyphAt: Int, withProposedLineFragmentRect: CGRect) -> CGFloat](./layoutmanager%28_,paragraphspacingbeforeglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add at the beginning of a paragraph.
- [func layoutManager(NSLayoutManager, shouldSetLineFragmentRect: UnsafeMutablePointer<CGRect>, lineFragmentUsedRect: UnsafeMutablePointer<CGRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, in: NSTextContainer, forGlyphRange: NSRange) -> Bool](./layoutmanager%28_,shouldsetlinefragmentrect,linefragmentusedrect,baselineoffset,in,forglyphrange%29.md)
  Customizes the line fragment geometry before committing it to the layout cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:boundingboxforcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:))*