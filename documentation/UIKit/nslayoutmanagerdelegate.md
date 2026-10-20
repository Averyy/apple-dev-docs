# NSLayoutManagerDelegate

**Framework**: UIKit  
**Kind**: protocol  
**Role**: Protocol

A set of optional methods that delegates of layout manager objects implement.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS

## Declaration

```swift
protocol NSLayoutManagerDelegate : NSObjectProtocol
```

```objc
@protocol NSLayoutManagerDelegate <NSObject>
```

## Topics

### Invalidating glyphs and layout
- [func layoutManagerDidInvalidateLayout(NSLayoutManager)](./nslayoutmanagerdelegate/layoutmanagerdidinvalidatelayout%28_%29.md)
  Informs the delegate when the specified layout manager invalidates layout information (not glyph information).
- [func layoutManager(NSLayoutManager, shouldGenerateGlyphs: UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: UIFont, forGlyphRange: NSRange) -> Int](./nslayoutmanagerdelegate/layoutmanager%28_,shouldgenerateglyphs,properties,characterindexes,font,forglyphrange%29.md)
  Enables customization of the initial glyph generation process.
- [func layoutManager(NSLayoutManager, shouldUse: NSLayoutManager.ControlCharacterAction, forControlCharacterAt: Int) -> NSLayoutManager.ControlCharacterAction](./nslayoutmanagerdelegate/layoutmanager%28_,shoulduse,forcontrolcharacterat%29.md)
  Returns the control character action for the control character at the specified character index.
- [NSLayoutManager.ControlCharacterAction](./nslayoutmanager/controlcharacteraction.md)
  Constants that describe actions for control characters.
### Responding to text container layout
- [func layoutManager(NSLayoutManager, didCompleteLayoutFor: NSTextContainer?, atEnd: Bool)](./nslayoutmanagerdelegate/layoutmanager%28_,didcompletelayoutfor,atend%29.md)
  Informs the delegate when the layout manager finishes laying out text in the specified text container.
- [func layoutManager(NSLayoutManager, textContainer: NSTextContainer, didChangeGeometryFrom: CGSize)](./nslayoutmanagerdelegate/layoutmanager%28_,textcontainer,didchangegeometryfrom%29.md)
  Informs the delegate when the layout manager invalidates layout due to a change in the geometry of the specified text container.
### Handling line fragments
- [func layoutManager(NSLayoutManager, shouldBreakLineByHyphenatingBeforeCharacterAt: Int) -> Bool](./nslayoutmanagerdelegate/layoutmanager%28_,shouldbreaklinebyhyphenatingbeforecharacterat%29.md)
  Asks the delegate whether to break the line at the specified character.
- [func layoutManager(NSLayoutManager, shouldBreakLineByWordBeforeCharacterAt: Int) -> Bool](./nslayoutmanagerdelegate/layoutmanager%28_,shouldbreaklinebywordbeforecharacterat%29.md)
  Asks the delegate whether to break the line at the specified word.
- [func layoutManager(NSLayoutManager, lineSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: CGRect) -> CGFloat](./nslayoutmanagerdelegate/layoutmanager%28_,linespacingafterglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add to the end of a line.
- [func layoutManager(NSLayoutManager, paragraphSpacingAfterGlyphAt: Int, withProposedLineFragmentRect: CGRect) -> CGFloat](./nslayoutmanagerdelegate/layoutmanager%28_,paragraphspacingafterglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add at the end of a paragraph.
- [func layoutManager(NSLayoutManager, paragraphSpacingBeforeGlyphAt: Int, withProposedLineFragmentRect: CGRect) -> CGFloat](./nslayoutmanagerdelegate/layoutmanager%28_,paragraphspacingbeforeglyphat,withproposedlinefragmentrect%29.md)
  Returns the amount of space to add at the beginning of a paragraph.
- [func layoutManager(NSLayoutManager, boundingBoxForControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: CGRect, glyphPosition: CGPoint, characterIndex: Int) -> CGRect](./nslayoutmanagerdelegate/layoutmanager%28_,boundingboxforcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md)
  Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [func layoutManager(NSLayoutManager, shouldSetLineFragmentRect: UnsafeMutablePointer<CGRect>, lineFragmentUsedRect: UnsafeMutablePointer<CGRect>, baselineOffset: UnsafeMutablePointer<CGFloat>, in: NSTextContainer, forGlyphRange: NSRange) -> Bool](./nslayoutmanagerdelegate/layoutmanager%28_,shouldsetlinefragmentrect,linefragmentusedrect,baselineoffset,in,forglyphrange%29.md)
  Customizes the line fragment geometry before committing it to the layout cache.
### Managing temporary attribute support
- [func layoutManager(NSLayoutManager, shouldUseTemporaryAttributes: [NSAttributedString.Key : Any], forDrawingToScreen: Bool, atCharacterIndex: Int, effectiveRange: NSRangePointer?) -> [NSAttributedString.Key : Any]?](../AppKit/nslayoutmanagerdelegate/layoutmanager%28_,shouldusetemporaryattributes,fordrawingtoscreen,atcharacterindex,effectiverange%29.md)
  Asks the delegate whether to use temporary attributes when drawing the text.
### Deprecated
- [Control Characters](./api-1619233-control-characters.md)
  Constants that describe actions for control characters.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Managing the layout process
- [var delegate: (any NSLayoutManagerDelegate)?](./nslayoutmanager/delegate.md)
  The layout manager’s delegate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanagerdelegate)*