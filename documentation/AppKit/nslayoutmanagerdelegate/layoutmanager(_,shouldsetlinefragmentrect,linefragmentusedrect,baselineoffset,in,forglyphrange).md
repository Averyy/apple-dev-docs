# layoutManager(_:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:in:forGlyphRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Customizes the line fragment geometry before committing it to the layout cache.

**Availability**:
- macOS 10.11+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldSetLineFragmentRect lineFragmentRect: UnsafeMutablePointer<NSRect>, lineFragmentUsedRect: UnsafeMutablePointer<NSRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, in textContainer: NSTextContainer, forGlyphRange glyphRange: NSRange) -> Bool
```

```objc
- (BOOL) layoutManager:(NSLayoutManager *) layoutManager shouldSetLineFragmentRect:(NSRect *) lineFragmentRect lineFragmentUsedRect:(NSRect *) lineFragmentUsedRect baselineOffset:(CGFloat *) baselineOffset inTextContainer:(NSTextContainer *) textContainer forGlyphRange:(NSRange) glyphRange;
```

## Return Value

[`true`](../../Swift/true.md) if you modified the layout information and want your modifications to be used or [`false`](../../Swift/false.md) if the original layout information should be used.

## Discussion

Use this method to modify the line fragment rectangles associated with the text container. It is your responsibility to ensure that the modified rectangles remain valid and still lie within the text container.

## Parameters

- `layoutManager`: The layout manager doing the work.
- `lineFragmentRect`: The proposed rectangle that contains the glyphs. You may modify this rectangle as needed.
- `lineFragmentUsedRect`: The portion of `lineFragmentRect` that actually contains glyphs or other rendered marks, including the text container’s line fragment padding. This rectangle must be equal to `lineFragmentRect` or wholly contained by it. You may modify this rectangle as needed.
- `baselineOffset`: The vertical distance (in pixels) from the line fragment origin to the baseline on which the glyphs align.
- `textContainer`: The text container for the line fragments.
- `glyphRange`: The range of glyphs being laid out.

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
- [func layoutManager(NSLayoutManager, boundingBoxForControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](./layoutmanager%28_,boundingboxforcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md)
  Returns the bounding rectangle for the specified control glyph with the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/layoutmanager(_:shouldsetlinefragmentrect:linefragmentusedrect:baselineoffset:in:forglyphrange:))*