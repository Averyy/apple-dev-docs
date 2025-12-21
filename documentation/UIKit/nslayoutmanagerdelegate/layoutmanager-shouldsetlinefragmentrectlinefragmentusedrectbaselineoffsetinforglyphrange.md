# layoutManager(_:shouldSetLineFragmentRect:lineFragmentUsedRect:baselineOffset:in:forGlyphRange:)

**Framework**: UIKit  
**Kind**: method

Customizes the line fragment geometry before committing it to the layout cache.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldSetLineFragmentRect lineFragmentRect: UnsafeMutablePointer<CGRect>, lineFragmentUsedRect: UnsafeMutablePointer<CGRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, in textContainer: NSTextContainer, forGlyphRange glyphRange: NSRange) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if you modified the layout information and want your modifications to be used or [`false`](https://developer.apple.com/documentation/Swift/false) if the original layout information should be used.

#### Discussion

Use this method to modify the line fragment rectangles associated with the text container. It is your responsibility to ensure that the modified rectangles remain valid and still lie within the text container.

## Parameters

- `layoutManager`: The layout manager doing the work.
- `lineFragmentRect`: The proposed rectangle that contains the glyphs. You may modify this rectangle as needed.
- `lineFragmentUsedRect`: The portion of   that actually contains glyphs or other rendered marks, including the text container’s line fragment padding. This rectangle must be equal to   or wholly contained by it. You may modify this rectangle as needed.
- `baselineOffset`: The vertical distance (in pixels) from the line fragment origin to the baseline on which the glyphs align.
- `textContainer`: The text container for the line fragments.
- `glyphRange`: The range of glyphs being laid out.

## See Also

- [func layoutManager(NSLayoutManager, shouldBreakLineByHyphenatingBeforeCharacterAt: Int) -> Bool](nslayoutmanagerdelegate/layoutmanager(_:shouldbreaklinebyhyphenatingbeforecharacterat:).md)
  Asks the delegate whether to break the line at the specified character.
- [func layoutManager(NSLayoutManager, shouldBreakLineByWordBeforeCharacterAt: Int) -> Bool](nslayoutmanagerdelegate/layoutmanager(_:shouldbreaklinebywordbeforecharacterat:).md)
  Asks the delegate whether to break the line at the specified word.
- [func layoutManager(NSLayoutManager, lineSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: CGRect) -> CGFloat](nslayoutmanagerdelegate/layoutmanager(_:linespacingafterglyphat:withproposedlinefragmentrect:).md)
  Returns the amount of space to add to the end of a line.
- [func layoutManager(NSLayoutManager, paragraphSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: CGRect) -> CGFloat](nslayoutmanagerdelegate/layoutmanager(_:paragraphspacingafterglyphat:withproposedlinefragmentrect:).md)
  Returns the amount of space to add at the end of a paragraph.
- [func layoutManager(NSLayoutManager, paragraphSpacingBeforeGlyphAt: Int, withProposedLineFragmentRect: CGRect) -> CGFloat](nslayoutmanagerdelegate/layoutmanager(_:paragraphspacingbeforeglyphat:withproposedlinefragmentrect:).md)
  Returns the amount of space to add at the beginning of a paragraph.
- [func layoutManager(NSLayoutManager, boundingBoxForControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: CGRect, glyphPosition: CGPoint, characterIndex: Int) -> CGRect](nslayoutmanagerdelegate/layoutmanager(_:boundingboxforcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the bounding rectangle for the specified control glyph with the specified parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldsetlinefragmentrect:linefragmentusedrect:baselineoffset:in:forglyphrange:))*