# layoutManager(_:shouldBreakLineByWordBeforeCharacterAt:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate whether to break the line at the specified word.

**Availability**:
- macOS 10.11+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldBreakLineByWordBeforeCharacterAt charIndex: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the current line break point is acceptable; [`false`](https://developer.apple.com/documentation/Swift/false) if the layout manager should find the next break point opportunity before `charIndex`.

## Parameters

- `layoutManager`: The layout manager doing the layout.
- `charIndex`: Index of the character delimiting the break point search.

## See Also

- [func layoutManager(NSLayoutManager, shouldBreakLineByHyphenatingBeforeCharacterAt: Int) -> Bool](nslayoutmanagerdelegate/layoutmanager(_:shouldbreaklinebyhyphenatingbeforecharacterat:).md)
  Asks the delegate whether to break the line at the specified character.
- [func layoutManager(NSLayoutManager, lineSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nslayoutmanagerdelegate/layoutmanager(_:linespacingafterglyphat:withproposedlinefragmentrect:).md)
  Returns the amount of space to add to the end of a line.
- [func layoutManager(NSLayoutManager, paragraphSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nslayoutmanagerdelegate/layoutmanager(_:paragraphspacingafterglyphat:withproposedlinefragmentrect:).md)
  Returns the amount of space to add at the end of a paragraph.
- [func layoutManager(NSLayoutManager, paragraphSpacingBeforeGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nslayoutmanagerdelegate/layoutmanager(_:paragraphspacingbeforeglyphat:withproposedlinefragmentrect:).md)
  Returns the amount of space to add at the beginning of a paragraph.
- [func layoutManager(NSLayoutManager, boundingBoxForControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](nslayoutmanagerdelegate/layoutmanager(_:boundingboxforcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [func layoutManager(NSLayoutManager, shouldSetLineFragmentRect: UnsafeMutablePointer<NSRect>, lineFragmentUsedRect: UnsafeMutablePointer<NSRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, in: NSTextContainer, forGlyphRange: NSRange) -> Bool](nslayoutmanagerdelegate/layoutmanager(_:shouldsetlinefragmentrect:linefragmentusedrect:baselineoffset:in:forglyphrange:).md)
  Customizes the line fragment geometry before committing it to the layout cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanagerdelegate/layoutmanager(_:shouldbreaklinebywordbeforecharacterat:))*