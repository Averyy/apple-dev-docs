# NSLayoutManagerDelegate

**Framework**: UIKit  
**Kind**: protocol

A set of optional methods that delegates of layout manager objects implement.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol NSLayoutManagerDelegate : NSObjectProtocol
```

## Topics

### Invalidating glyphs and layout
- [func layoutManagerDidInvalidateLayout(NSLayoutManager)](nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout(_:).md)
  Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [func layoutManager(NSLayoutManager, shouldGenerateGlyphs: UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: UIFont, forGlyphRange: NSRange) -> Int](nslayoutmanagerdelegate/layoutmanager(_:shouldgenerateglyphs:properties:characterindexes:font:forglyphrange:).md)
  Enables customization of the initial glyph generation process.
- [func layoutManager(NSLayoutManager, shouldUse: NSLayoutManager.ControlCharacterAction, forControlCharacterAt: Int) -> NSLayoutManager.ControlCharacterAction](nslayoutmanagerdelegate/layoutmanager(_:shoulduse:forcontrolcharacterat:).md)
  Returns the control character action for the control character at the specified character index.
- [NSLayoutManager.ControlCharacterAction](nslayoutmanager/controlcharacteraction.md)
  Constants that describe actions for control characters.
### Responding to text container layout
- [func layoutManager(NSLayoutManager, didCompleteLayoutFor: NSTextContainer?, atEnd: Bool)](nslayoutmanagerdelegate/layoutmanager(_:didcompletelayoutfor:atend:).md)
  Informs the delegate when the layout manager finishes laying out text in the specified text container.
- [func layoutManager(NSLayoutManager, textContainer: NSTextContainer, didChangeGeometryFrom: CGSize)](nslayoutmanagerdelegate/layoutmanager(_:textcontainer:didchangegeometryfrom:).md)
  Informs the delegate when the layout manager invalidates layout due to a change in the geometry of the specified text container.
### Handling line fragments
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
- [func layoutManager(NSLayoutManager, shouldSetLineFragmentRect: UnsafeMutablePointer<CGRect>, lineFragmentUsedRect: UnsafeMutablePointer<CGRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, in: NSTextContainer, forGlyphRange: NSRange) -> Bool](nslayoutmanagerdelegate/layoutmanager(_:shouldsetlinefragmentrect:linefragmentusedrect:baselineoffset:in:forglyphrange:).md)
  Customizes the line fragment geometry before committing it to the layout cache.
### Managing temporary attribute support
- [optional func layoutManager(_ layoutManager: NSLayoutManager, shouldUseTemporaryAttributes attrs: [NSAttributedString.Key : Any] = [:], forDrawingToScreen toScreen: Bool, atCharacterIndex charIndex: Int, effectiveRange effectiveCharRange: NSRangePointer?) -> [NSAttributedString.Key : Any]?](../AppKit/NSLayoutManagerDelegate/layoutManager(_:shouldUseTemporaryAttributes:forDrawingToScreen:atCharacterIndex:effectiveRange:).md)
  Asks the delegate whether to use temporary attributes when drawing the text.
### Deprecated
- [Control Characters](1619233-control-characters.md)
  Constants that describe actions for control characters.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var delegate: (any NSLayoutManagerDelegate)?](nslayoutmanager/delegate.md)
  The layout manager’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate)*