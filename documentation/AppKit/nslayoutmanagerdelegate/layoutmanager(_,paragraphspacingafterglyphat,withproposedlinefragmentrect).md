# layoutManager(_:paragraphSpacingAfterGlyphAt:withProposedLineFragmentRect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the amount of space to add at the end of a paragraph.

**Availability**:
- macOS 10.11+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, paragraphSpacingAfterGlyphAt glyphIndex: Int, withProposedLineFragmentRect rect: NSRect) -> CGFloat
```

```objc
- (CGFloat) layoutManager:(NSLayoutManager *) layoutManager paragraphSpacingAfterGlyphAtIndex:(NSUInteger) glyphIndex withProposedLineFragmentRect:(NSRect) rect;
```

## Return Value

The paragraph spacing after the current line.

## Discussion

This message is sent while each line is laid out to enable the layout manager delegate to customize the shape of line.

## Parameters

- `layoutManager`: The layout manager doing the layout.
- `glyphIndex`: The index of the glyph at the end of the line.
- `rect`: The proposed line fragment rectangle for the current line.

## See Also

### Handling line fragments
- [func layoutManager(NSLayoutManager, shouldBreakLineByHyphenatingBeforeCharacterAt: Int) -> Bool](./layoutmanager%28_,shouldbreaklinebyhyphenatingbeforecharacterat%29.md)
  Asks the delegate whether to break the line at the specified character.
- [func layoutManager(NSLayoutManager, shouldBreakLineByWordBeforeCharacterAt: Int) -> Bool](./layoutmanager%28_,shouldbreaklinebywordbeforecharacterat%29.md)
  Asks the delegate whether to break the line at the specified word.
- [func layoutManager(NSLayoutManager, lineSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./layoutmanager%28_,linespacingafterglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add to the end of a line.
- [func layoutManager(NSLayoutManager, paragraphSpacingBeforeGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./layoutmanager%28_,paragraphspacingbeforeglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add at the beginning of a paragraph.
- [func layoutManager(NSLayoutManager, boundingBoxForControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](./layoutmanager%28_,boundingboxforcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md)
  Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [func layoutManager(NSLayoutManager, shouldSetLineFragmentRect: UnsafeMutablePointer<NSRect>, lineFragmentUsedRect: UnsafeMutablePointer<NSRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, in: NSTextContainer, forGlyphRange: NSRange) -> Bool](./layoutmanager%28_,shouldsetlinefragmentrect,linefragmentusedrect,baselineoffset,in,forglyphrange%29.md)
  Customizes the line fragment geometry before committing it to the layout cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/layoutmanager(_:paragraphspacingafterglyphat:withproposedlinefragmentrect:))*