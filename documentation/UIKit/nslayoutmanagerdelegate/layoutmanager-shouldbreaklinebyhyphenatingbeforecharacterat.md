# layoutManager(_:shouldBreakLineByHyphenatingBeforeCharacterAt:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate whether to break the line at the specified character.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
optional func layoutManager(_ layoutManager: NSLayoutManager, shouldBreakLineByHyphenatingBeforeCharacterAt charIndex: Int) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the current hyphenation point is acceptable; [`false`](https://developer.apple.com/documentation/swift/false) if the layout manager should find the next hyphenation opportunity before `charIndex`.

## Parameters

- `layoutManager`: The layout manager doing the layout.
- `charIndex`: Index of the character delimiting the hyphenation point search.

## See Also

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
- [func layoutManager(NSLayoutManager, shouldSetLineFragmentRect: UnsafeMutablePointer<CGRect>, lineFragmentUsedRect: UnsafeMutablePointer<CGRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, in: NSTextContainer, forGlyphRange: NSRange) -> Bool](nslayoutmanagerdelegate/layoutmanager(_:shouldsetlinefragmentrect:linefragmentusedrect:baselineoffset:in:forglyphrange:).md)
  Customizes the line fragment geometry before committing it to the layout cache.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate/layoutmanager(_:shouldbreaklinebyhyphenatingbeforecharacterat:))*