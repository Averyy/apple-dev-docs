# NSLayoutManager

**Framework**: UIKit  
**Kind**: class

An object that coordinates the layout and display of text characters.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class NSLayoutManager
```

#### Overview

[`NSLayoutManager`](nslayoutmanager.md) maps Unicode character codes to glyphs, sets the glyphs in a series of [`NSTextContainer`](nstextcontainer.md) objects, and displays them in a series of [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView) objects. In addition to its core function of laying out text, a layout manager object coordinates its text view objects, provides services to those text views to support [`NSRulerView`](https://developer.apple.com/documentation/AppKit/NSRulerView) instances for editing paragraph styles, and handles the layout and display of text attributes not inherent in glyphs (such as underline or strikethrough). You can create a subclass of [`NSLayoutManager`](nslayoutmanager.md) to handle additional text attributes, whether inherent or not.

##### Text Antialiasing

[`NSLayoutManager`](nslayoutmanager.md) provides the threshold for text antialiasing. It looks at the `AppleAntiAliasingThreshold` default value. If the font size is smaller than or equal to this threshold size, the text is rendered aliased by [`NSLayoutManager`](nslayoutmanager.md). In macOS, you can change the threshold value from the Appearance pane of System Preferences.

##### Thread Safety of Nslayoutmanager

Generally speaking, a specific layout manager (and associated objects) should not be used in more than one block, operation, or thread at a time. Most layout managers are used on the main thread, since it is the main thread on which their text views are displayed, and since background layout occurs on the main thread.

If you want to use a layout manager on a background thread, first make sure that text views associated with that layout manager (if any) are not displayed while the layout manager is being used on the background thread, and, second, turn off background layout for that layout manager while it is being used on the background thread. The most effective way to ensure that no text view is displayed, without knowing deep implementation, is just not to connect a text view to the layout manager.

##### Noncontiguous Layout

Noncontiguous layout is an optional layout manager behavior. Previously, both glyph generation and layout were always performed, in order, from the beginning to the end of the document. When noncontiguous layout is turned on, however, the layout manager gains the option of performing glyph generation or layout for one portion of the document without having done so for previous sections. This can provide significant performance improvements for large documents.

Noncontiguous layout is not turned on automatically because direct clients of `NSLayoutManager` typically have relied on the previous behavior—for example, by forcing layout for a specific glyph range, and then assuming that previous glyphs would therefore be laid out. Clients who use [`NSLayoutManager`](nslayoutmanager.md) only indirectly—for example, those who use [`NSTextView`](https://developer.apple.com/documentation/AppKit/NSTextView) without directly calling the underlying layout manager—can usually turn on noncontiguous layout without difficulty. Clients using [`NSLayoutManager`](nslayoutmanager.md) directly need to examine their usage before turning on noncontiguous layout.

Enable noncontiguous layout using the [`allowsNonContiguousLayout`](nslayoutmanager/allowsnoncontiguouslayout.md) property. In addition, see the other methods in [`Causing glyph generation and layout`](nslayoutmanager#Causing-glyph-generation-and-layout.md), many of which enable you to ensure that glyph generation and layout are performed for specified portions of the text. The behavior of a number of other layout manager methods is affected by the state of noncontiguous layout, as noted in the discussion sections of those method descriptions.

## Topics

### Creating a layout manager
- [init()](nslayoutmanager/init.md)
  Initializes a newly created layout manager object.
- [init?(coder: NSCoder)](nslayoutmanager/init(coder:).md)
  Creates a layout manager from data in an unarchiver.
### Managing the layout process
- [var delegate: (any NSLayoutManagerDelegate)?](nslayoutmanager/delegate.md)
  The layout manager’s delegate.
- [protocol NSLayoutManagerDelegate](nslayoutmanagerdelegate.md)
  A set of optional methods that delegates of layout manager objects implement.
### Accessing the text storage
- [var textStorage: NSTextStorage?](nslayoutmanager/textstorage.md)
  The text storage object that contains the content to lay out.
- [func replaceTextStorage(_ newTextStorage: NSTextStorage)](../AppKit/NSLayoutManager/replaceTextStorage(_:).md)
  Replaces the layout manager’s current text storage object with the specified object.
### Configuring the global layout manager options
- [var allowsNonContiguousLayout: Bool](nslayoutmanager/allowsnoncontiguouslayout.md)
  A Boolean value that indicates whether the layout manager allows noncontiguous layout.
- [var hasNonContiguousLayout: Bool](nslayoutmanager/hasnoncontiguouslayout.md)
  A Boolean value that indicates whether the layout manager currently has any areas of noncontiguous layout.
- [var showsInvisibleCharacters: Bool](nslayoutmanager/showsinvisiblecharacters.md)
  A Boolean value that indicates whether to substitute visible glyphs for whitespace and other typically invisible characters.
- [var showsControlCharacters: Bool](nslayoutmanager/showscontrolcharacters.md)
  A Boolean value that indicates whether the layout manager substitutes visible glyphs for control characters in the layout.
- [var usesFontLeading: Bool](nslayoutmanager/usesfontleading.md)
  A Boolean value that indicates whether the layout manager uses the leading of the font.
- [var backgroundLayoutEnabled: Bool { get set }](../AppKit/NSLayoutManager/backgroundLayoutEnabled.md)
  A Boolean value that indicates whether the layout manager generates glyphs and lays them out when the app’s run loop is idle.
- [var limitsLayoutForSuspiciousContents: Bool](nslayoutmanager/limitslayoutforsuspiciouscontents.md)
  A Boolean value that indicates whether the layout manager avoids laying out unusually long or suspicious input.
- [var usesDefaultHyphenation: Bool](nslayoutmanager/usesdefaulthyphenation.md)
  A Boolean value that indicates whether the layout manager uses the default hyphenation rules to wrap lines.
### Managing the text containers
- [var textContainers: [NSTextContainer]](nslayoutmanager/textcontainers.md)
  The current text containers of the layout manager.
- [func addTextContainer(NSTextContainer)](nslayoutmanager/addtextcontainer(_:).md)
  Appends the specified text container to the series of text containers where the layout manager arranges text.
- [func insertTextContainer(NSTextContainer, at: Int)](nslayoutmanager/inserttextcontainer(_:at:).md)
  Inserts a text container at the specified index in the list of text containers.
- [func removeTextContainer(at: Int)](nslayoutmanager/removetextcontainer(at:).md)
  Removes the text container at the specified index and invalidates the layout as necessary.
- [func setTextContainer(NSTextContainer, forGlyphRange: NSRange)](nslayoutmanager/settextcontainer(_:forglyphrange:).md)
  Associates a text container with the specified range of glyphs.
- [func textContainerChangedGeometry(NSTextContainer)](nslayoutmanager/textcontainerchangedgeometry(_:).md)
  Invalidates the layout information, and possibly glyphs, for the specified text container and all subsequent text container objects.
- [func textContainerChangedTextView(_ container: NSTextContainer)](../AppKit/NSLayoutManager/textContainerChangedTextView(_:).md)
  Updates the information necessary to manage text view objects for the specified text container.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> NSTextContainer?](nslayoutmanager/textcontainer(forglyphat:effectiverange:).md)
  Returns the text container that manages the layout for the specified glyph, causing layout to happen as necessary.
- [func textContainer(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> NSTextContainer?](nslayoutmanager/textcontainer(forglyphat:effectiverange:withoutadditionallayout:).md)
  Returns the text container that manages the layout for the specified glyph.
- [func usedRect(for: NSTextContainer) -> CGRect](nslayoutmanager/usedrect(for:).md)
  Returns the bounding rectangle for the glyphs in the specified text container.
### Invalidating glyphs and layout
- [func invalidateDisplay(forCharacterRange: NSRange)](nslayoutmanager/invalidatedisplay(forcharacterrange:).md)
  Invalidates display for the specified character range.
- [func invalidateDisplay(forGlyphRange: NSRange)](nslayoutmanager/invalidatedisplay(forglyphrange:).md)
  Invalidates a range of glyphs, requiring new layout information, and updates the appropriate regions of any text views that display those glyphs.
- [func invalidateGlyphs(forCharacterRange: NSRange, changeInLength: Int, actualCharacterRange: NSRangePointer?)](nslayoutmanager/invalidateglyphs(forcharacterrange:changeinlength:actualcharacterrange:).md)
  Invalidates and adjusts the glyphs in the specified character range.
- [func invalidateLayout(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?)](nslayoutmanager/invalidatelayout(forcharacterrange:actualcharacterrange:).md)
  Invalidates the layout information for the glyphs that map to the specified character range.
- [func processEditing(for: NSTextStorage, edited: NSTextStorage.EditActions, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](nslayoutmanager/processediting(for:edited:range:changeinlength:invalidatedrange:).md)
  Notifies the layout manager when an edit action changes the contents of its text storage object.
### Causing glyph generation and layout
- [func ensureGlyphs(forCharacterRange: NSRange)](nslayoutmanager/ensureglyphs(forcharacterrange:).md)
  Forces the layout manager to generate glyphs for the specified character range if it hasn’t already.
- [func ensureGlyphs(forGlyphRange: NSRange)](nslayoutmanager/ensureglyphs(forglyphrange:).md)
  Forces the layout manager to generate glyphs for the specified glyph range if it hasn’t already.
- [func ensureLayout(forBoundingRect: CGRect, in: NSTextContainer)](nslayoutmanager/ensurelayout(forboundingrect:in:).md)
  Forces the layout manager to perform layout for the specified area in the specified text container if it hasn’t already.
- [func ensureLayout(forCharacterRange: NSRange)](nslayoutmanager/ensurelayout(forcharacterrange:).md)
  Forces the layout manager to perform layout for the specified character range if it hasn’t already.
- [func ensureLayout(forGlyphRange: NSRange)](nslayoutmanager/ensurelayout(forglyphrange:).md)
  Forces the layout manager to perform layout for the specified glyph range if it hasn’t already.
- [func ensureLayout(for: NSTextContainer)](nslayoutmanager/ensurelayout(for:).md)
  Forces the layout manager to perform layout for the specified text container if it hasn’t already.
- [var glyphGenerator: NSGlyphGenerator { get set }](../AppKit/NSLayoutManager/glyphGenerator.md)
  The glyph generator that the layout manager uses.
### Accessing glyphs
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<CGGlyph>?, properties: UnsafeMutablePointer<NSLayoutManager.GlyphProperty>?, characterIndexes: UnsafeMutablePointer<Int>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](nslayoutmanager/getglyphs(in:glyphs:properties:characterindexes:bidilevels:).md)
  Fills a passed-in buffer with a sequence of glyphs.
- [func cgGlyph(at: Int) -> CGGlyph](nslayoutmanager/cgglyph(at:).md)
  Returns the glyph at the specified index.
- [func cgGlyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph](nslayoutmanager/cgglyph(at:isvalidindex:).md)
  Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [func setGlyphs(UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: UIFont, forGlyphRange: NSRange)](nslayoutmanager/setglyphs(_:properties:characterindexes:font:forglyphrange:).md)
  Stores the initial glyphs and glyph properties for a character range.
- [func characterIndexForGlyph(at: Int) -> Int](nslayoutmanager/characterindexforglyph(at:).md)
  Returns the index in the text storage for the first character of the specified glyph.
- [func glyphIndexForCharacter(at: Int) -> Int](nslayoutmanager/glyphindexforcharacter(at:).md)
  Returns the index of the first glyph of the character at the specified index.
- [func isValidGlyphIndex(Int) -> Bool](nslayoutmanager/isvalidglyphindex(_:).md)
  Indicates whether the specified index refers to a valid glyph.
- [var numberOfGlyphs: Int](nslayoutmanager/numberofglyphs.md)
  The number of glyphs in the layout manager.
- [func propertyForGlyph(at: Int) -> NSLayoutManager.GlyphProperty](nslayoutmanager/propertyforglyph(at:).md)
  Returns the glyph property of the glyph at the specified index.
- [NSLayoutManager.GlyphProperty](nslayoutmanager/glyphproperty.md)
  Glyph properties.
### Setting layout information
- [func setAttachmentSize(CGSize, forGlyphRange: NSRange)](nslayoutmanager/setattachmentsize(_:forglyphrange:).md)
  Sets the size to use when drawing a glyph that represents an attachment.
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](nslayoutmanager/setdrawsoutsidelinefragment(_:forglyphat:).md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setExtraLineFragmentRect(CGRect, usedRect: CGRect, textContainer: NSTextContainer)](nslayoutmanager/setextralinefragmentrect(_:usedrect:textcontainer:).md)
  Sets the bounds and container for the extra line fragment.
- [func setLineFragmentRect(CGRect, forGlyphRange: NSRange, usedRect: CGRect)](nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:).md)
  Associates the line fragment bounds for the specified range of glyphs.
- [func setLocation(CGPoint, forStartOfGlyphRange: NSRange)](nslayoutmanager/setlocation(_:forstartofglyphrange:).md)
  Sets the location for the first glyph in the specified range.
- [func setNotShownAttribute(Bool, forGlyphAt: Int)](nslayoutmanager/setnotshownattribute(_:forglyphat:).md)
  Sets the visibility of the glyph at the specified index.
### Getting layout information
- [func attachmentSize(forGlyphAt: Int) -> CGSize](nslayoutmanager/attachmentsize(forglyphat:).md)
  Returns the size of the attachment glyph at the specified index.
- [func drawsOutsideLineFragment(forGlyphAt: Int) -> Bool](nslayoutmanager/drawsoutsidelinefragment(forglyphat:).md)
  Indicates whether the glyph draws outside its line fragment rectangle.
- [var extraLineFragmentRect: CGRect](nslayoutmanager/extralinefragmentrect.md)
  The rectangle for the extra line fragment at the end of a document.
- [var extraLineFragmentTextContainer: NSTextContainer?](nslayoutmanager/extralinefragmenttextcontainer.md)
  The text container for the extra line fragment rectangle.
- [var extraLineFragmentUsedRect: CGRect](nslayoutmanager/extralinefragmentusedrect.md)
  The rectangle that encloses the insertion point in the extra line fragment rectangle.
- [func firstUnlaidCharacterIndex() -> Int](nslayoutmanager/firstunlaidcharacterindex.md)
  Returns the index for the first character in the layout manager that isn’t in the layout.
- [func firstUnlaidGlyphIndex() -> Int](nslayoutmanager/firstunlaidglyphindex.md)
  Returns the index for the first glyph in the layout manager that isn’t in the layout.
- [func getFirstUnlaidCharacterIndex(UnsafeMutablePointer<Int>?, glyphIndex: UnsafeMutablePointer<Int>?)](nslayoutmanager/getfirstunlaidcharacterindex(_:glyphindex:).md)
  Returns the indexes for the first character and glyph that have invalid layout information.
- [func lineFragmentRect(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> CGRect](nslayoutmanager/linefragmentrect(forglyphat:effectiverange:).md)
  Returns the rectangle for the line fragment where the glyph lies and (optionally), by reference, the entire range of glyphs in that fragment.
- [func lineFragmentRect(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> CGRect](nslayoutmanager/linefragmentrect(forglyphat:effectiverange:withoutadditionallayout:).md)
  Returns the line fragment rectangle that contains the glyph at the specified glyph index.
- [func lineFragmentUsedRect(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> CGRect](nslayoutmanager/linefragmentusedrect(forglyphat:effectiverange:).md)
  Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [func lineFragmentUsedRect(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> CGRect](nslayoutmanager/linefragmentusedrect(forglyphat:effectiverange:withoutadditionallayout:).md)
  Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [func location(forGlyphAt: Int) -> CGPoint](nslayoutmanager/location(forglyphat:).md)
  Returns the location for the specified glyph within its line fragment.
- [func notShownAttribute(forGlyphAt: Int) -> Bool](nslayoutmanager/notshownattribute(forglyphat:).md)
  Indicates whether the glyph at the specified index has a visible representation.
- [func truncatedGlyphRange(inLineFragmentForGlyphAt: Int) -> NSRange](nslayoutmanager/truncatedglyphrange(inlinefragmentforglyphat:).md)
  Returns the range of truncated glyphs for a line fragment that contains the specified index.
### Performing advanced layout queries
- [func boundingRect(forGlyphRange: NSRange, in: NSTextContainer) -> CGRect](nslayoutmanager/boundingrect(forglyphrange:in:).md)
  Returns the bounding rectangle for the specified glyphs in a container.
- [func characterIndex(for: CGPoint, in: NSTextContainer, fractionOfDistanceBetweenInsertionPoints: UnsafeMutablePointer<CGFloat>?) -> Int](nslayoutmanager/characterindex(for:in:fractionofdistancebetweeninsertionpoints:).md)
  Returns the index of the character that lies beneath the specified point using the specified container’s coordinate system.
- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](nslayoutmanager/characterrange(forglyphrange:actualglyphrange:).md)
  Returns the range of characters that correspond to the glyphs in the specified glyph range.
- [func enumerateEnclosingRects(forGlyphRange: NSRange, withinSelectedGlyphRange: NSRange, in: NSTextContainer, using: (CGRect, UnsafeMutablePointer<ObjCBool>) -> Void)](nslayoutmanager/enumerateenclosingrects(forglyphrange:withinselectedglyphrange:in:using:).md)
  Enumerates enclosing rectangles for the specified glyph range in a text container.
- [func enumerateLineFragments(forGlyphRange: NSRange, using: (CGRect, CGRect, NSTextContainer, NSRange, UnsafeMutablePointer<ObjCBool>) -> Void)](nslayoutmanager/enumeratelinefragments(forglyphrange:using:).md)
  Enumerates line fragments intersecting with the specified glyph range.
- [func fractionOfDistanceThroughGlyph(for: CGPoint, in: NSTextContainer) -> CGFloat](nslayoutmanager/fractionofdistancethroughglyph(for:in:).md)
  Returns the fraction of the distance between the glyph at the specified point and the next glyph.
- [func getLineFragmentInsertionPoints(forCharacterAt: Int, alternatePositions: Bool, inDisplayOrder: Bool, positions: UnsafeMutablePointer<CGFloat>?, characterIndexes: UnsafeMutablePointer<Int>?) -> Int](nslayoutmanager/getlinefragmentinsertionpoints(forcharacterat:alternatepositions:indisplayorder:positions:characterindexes:).md)
  Returns insertion points in bulk for a specified line fragment.
- [func glyphIndex(for: CGPoint, in: NSTextContainer) -> Int](nslayoutmanager/glyphindex(for:in:).md)
  Returns the index of the glyph at the specified location in a text container.
- [func glyphIndex(for: CGPoint, in: NSTextContainer, fractionOfDistanceThroughGlyph: UnsafeMutablePointer<CGFloat>?) -> Int](nslayoutmanager/glyphindex(for:in:fractionofdistancethroughglyph:).md)
  Returns the index of the glyph at the specified point using the container’s coordinate system.
- [func glyphRange(forBoundingRect: CGRect, in: NSTextContainer) -> NSRange](nslayoutmanager/glyphrange(forboundingrect:in:).md)
  Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [func glyphRange(forBoundingRectWithoutAdditionalLayout: CGRect, in: NSTextContainer) -> NSRange](nslayoutmanager/glyphrange(forboundingrectwithoutadditionallayout:in:).md)
  Returns the smallest contiguous range for glyphs lying wholly or partially within the specified rectangle of the text container.
- [func glyphRange(for: NSTextContainer) -> NSRange](nslayoutmanager/glyphrange(for:).md)
  Returns the range of glyphs lying within the specified text container.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](nslayoutmanager/glyphrange(forcharacterrange:actualcharacterrange:).md)
  Returns the range of glyphs that the specified range of characters generates.
- [func range(ofNominallySpacedGlyphsContaining: Int) -> NSRange](nslayoutmanager/range(ofnominallyspacedglyphscontaining:).md)
  Returns the range of displayable glyphs that surround the glyph at the specified index.
### Drawing
- [func drawBackground(forGlyphRange: NSRange, at: CGPoint)](nslayoutmanager/drawbackground(forglyphrange:at:).md)
  Draws background marks for the specified glyphs, which must lie completely within a single text container.
- [func drawGlyphs(forGlyphRange: NSRange, at: CGPoint)](nslayoutmanager/drawglyphs(forglyphrange:at:).md)
  Draws the specified glyphs, which must lie completely within a single text container.
- [func drawStrikethrough(forGlyphRange: NSRange, strikethroughType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](nslayoutmanager/drawstrikethrough(forglyphrange:strikethroughtype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Draws a strikethrough for the specified glyphs.
- [func drawUnderline(forGlyphRange: NSRange, underlineType: NSUnderlineStyle, baselineOffset: CGFloat, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](nslayoutmanager/drawunderline(forglyphrange:underlinetype:baselineoffset:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Draws underlining for the glyphs in a specified range.
- [func fillBackgroundRectArray(UnsafePointer<CGRect>, count: Int, forCharacterRange: NSRange, color: UIColor)](nslayoutmanager/fillbackgroundrectarray(_:count:forcharacterrange:color:).md)
  Fills background rectangles with a color.
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: UIFont, textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](nslayoutmanager/showcgglyphs(_:positions:count:font:textmatrix:attributes:in:).md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func strikethroughGlyphRange(NSRange, strikethroughType: NSUnderlineStyle, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](nslayoutmanager/strikethroughglyphrange(_:strikethroughtype:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Calculates and draws strikethrough for the specified glyphs.
- [func underlineGlyphRange(NSRange, underlineType: NSUnderlineStyle, lineFragmentRect: CGRect, lineFragmentGlyphRange: NSRange, containerOrigin: CGPoint)](nslayoutmanager/underlineglyphrange(_:underlinetype:linefragmentrect:linefragmentglyphrange:containerorigin:).md)
  Calculates subranges to underline for the specified glyphs and draws the underlining as appropriate.
### Handling layout for text blocks
- [func setLayoutRect(_ rect: NSRect, for block: NSTextBlock, glyphRange: NSRange)](../AppKit/NSLayoutManager/setLayoutRect(_:for:glyphRange:).md)
  Sets the layout rectangle that encloses the specified text block and glyph range.
- [func layoutRect(for block: NSTextBlock, glyphRange: NSRange) -> NSRect](../AppKit/NSLayoutManager/layoutRect(for:glyphRange:).md)
  Returns the rectangle for the layout of the specified text block and glyph range.
- [func setBoundsRect(_ rect: NSRect, for block: NSTextBlock, glyphRange: NSRange)](../AppKit/NSLayoutManager/setBoundsRect(_:for:glyphRange:).md)
  Sets the bounding rectangle that encloses the specified text block and glyph range.
- [func boundsRect(for block: NSTextBlock, glyphRange: NSRange) -> NSRect](../AppKit/NSLayoutManager/boundsRect(for:glyphRange:).md)
  Returns the bounding rectangle that encloses the specified text block and glyph range.
- [func layoutRect(for block: NSTextBlock, at glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?) -> NSRect](../AppKit/NSLayoutManager/layoutRect(for:at:effectiveRange:).md)
  Returns the rectangle for the layout of the specified text block and glyph.
- [func boundsRect(for block: NSTextBlock, at glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?) -> NSRect](../AppKit/NSLayoutManager/boundsRect(for:at:effectiveRange:).md)
  Returns the bounding rectangle for the specified text block and glyph.
### Managing attachments
- [var defaultAttachmentScaling: NSImageScaling { get set }](../AppKit/NSLayoutManager/defaultAttachmentScaling.md)
  The default amount of scaling to apply when an attachment image is too large to fit in a text container.
- [func showAttachmentCell(_ cell: NSCell, in rect: NSRect, characterIndex attachmentIndex: Int)](../AppKit/NSLayoutManager/showAttachmentCell(_:in:characterIndex:).md)
  Draws an attachment cell.
### Handling Rulers
- [func rulerAccessoryView(for view: NSTextView, paragraphStyle style: NSParagraphStyle, ruler: NSRulerView, enabled isEnabled: Bool) -> NSView?](../AppKit/NSLayoutManager/rulerAccessoryView(for:paragraphStyle:ruler:enabled:).md)
  Returns the accessory view that the text system uses for its ruler.
- [func rulerMarkers(for view: NSTextView, paragraphStyle style: NSParagraphStyle, ruler: NSRulerView) -> [NSRulerMarker]](../AppKit/NSLayoutManager/rulerMarkers(for:paragraphStyle:ruler:).md)
  Returns an array of text ruler objects for the current selection.
### Managing the responder chain
- [func layoutManagerOwnsFirstResponder(in window: NSWindow) -> Bool](../AppKit/NSLayoutManager/layoutManagerOwnsFirstResponder(in:).md)
  Indicates whether the first responder in the specified window is a text view for the layout manager.
- [unowned(unsafe) var firstTextView: NSTextView? { get }](../AppKit/NSLayoutManager/firstTextView.md)
  The first text view in the layout manager’s series of text views.
- [unowned(unsafe) var textViewForBeginningOfSelection: NSTextView? { get }](../AppKit/NSLayoutManager/textViewForBeginningOfSelection.md)
  The text view that contains the first glyph in the selection.
### Managing the typesetter
- [var typesetter: NSTypesetter { get set }](../AppKit/NSLayoutManager/typesetter.md)
  The current typesetter.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior { get set }](../AppKit/NSLayoutManager/typesetterBehavior-swift.property.md)
  The default typesetter behavior.
- [NSLayoutManager.TypesetterBehavior](../AppKit/NSLayoutManager/TypesetterBehavior-swift.enum.md)
  Constants that determine the layout manager’s behavior during layout.
- [func defaultLineHeight(for theFont: NSFont) -> CGFloat](../AppKit/NSLayoutManager/defaultLineHeight(for:).md)
  Returns the default line height for a line of text that uses a specified font.
- [func defaultBaselineOffset(for theFont: NSFont) -> CGFloat](../AppKit/NSLayoutManager/defaultBaselineOffset(for:).md)
  Returns the default baseline offset that the layout manager’s typesetter uses for the specified font.
### Managing temporary attribute support
- [func addTemporaryAttributes(_ attrs: [NSAttributedString.Key : Any] = [:], forCharacterRange charRange: NSRange)](../AppKit/NSLayoutManager/addTemporaryAttributes(_:forCharacterRange:).md)
  Appends one or more temporary attributes to the attributes dictionary of the specified character range.
- [func addTemporaryAttribute(_ attrName: NSAttributedString.Key, value: Any, forCharacterRange charRange: NSRange)](../AppKit/NSLayoutManager/addTemporaryAttribute(_:value:forCharacterRange:).md)
  Adds a temporary attribute to the characters in the specified range.
- [func setTemporaryAttributes(_ attrs: [NSAttributedString.Key : Any], forCharacterRange charRange: NSRange)](../AppKit/NSLayoutManager/setTemporaryAttributes(_:forCharacterRange:).md)
  Sets one or more temporary attributes for the specified character range.
- [func removeTemporaryAttribute(_ attrName: NSAttributedString.Key, forCharacterRange charRange: NSRange)](../AppKit/NSLayoutManager/removeTemporaryAttribute(_:forCharacterRange:).md)
  Removes a temporary attribute from the list of attributes for the specified character range.
- [func temporaryAttribute(_ attrName: NSAttributedString.Key, atCharacterIndex location: Int, effectiveRange range: NSRangePointer?) -> Any?](../AppKit/NSLayoutManager/temporaryAttribute(_:atCharacterIndex:effectiveRange:).md)
  Returns the value for the temporary attribute of a character, and the range it applies to.
- [func temporaryAttribute(_ attrName: NSAttributedString.Key, atCharacterIndex location: Int, longestEffectiveRange range: NSRangePointer?, in rangeLimit: NSRange) -> Any?](../AppKit/NSLayoutManager/temporaryAttribute(_:atCharacterIndex:longestEffectiveRange:in:).md)
  Returns the value for the temporary attribute of a character, and the maximum range it applies to.
- [func temporaryAttributes(atCharacterIndex charIndex: Int, effectiveRange effectiveCharRange: NSRangePointer?) -> [NSAttributedString.Key : Any]](../AppKit/NSLayoutManager/temporaryAttributes(atCharacterIndex:effectiveRange:).md)
  Returns the dictionary of temporary attributes for the specified character range.
- [func temporaryAttributes(atCharacterIndex location: Int, longestEffectiveRange range: NSRangePointer?, in rangeLimit: NSRange) -> [NSAttributedString.Key : Any]](../AppKit/NSLayoutManager/temporaryAttributes(atCharacterIndex:longestEffectiveRange:in:).md)
  Returns the temporary attributes for a character, and the maximum range they apply to.
### Supporting types
- [NSLayoutManager.TextLayoutOrientation](nslayoutmanager/textlayoutorientation.md)
  Constants that describe the text layout orientation.
### Deprecated
- [Deprecated symbols](nslayoutmanager-deprecated-symbols.md)
  Review unsupported symbols and their replacements.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class NSTextStorage](nstextstorage.md)
  The fundamental storage mechanism of TextKit that contains the text managed by the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager)*