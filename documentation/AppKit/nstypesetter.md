# NSTypesetter

**Framework**: Appkit  
**Kind**: class

An abstract class that performs various type layout tasks.

**Availability**:
- macOS ?+

## Declaration

```swift
class NSTypesetter
```

#### Overview

[`NSLayoutManager`](nslayoutmanager.md) uses concrete subclasses of [`NSTypesetter`](nstypesetter.md) to perform line layout, which includes word wrapping, hyphenation, and line breaking in either vertical or horizontal rectangles. By default, the text system uses the concrete subclass [`NSATSTypesetter`](nsatstypesetter.md).

> **Note**:  Use this class with [`NSLayoutManager`](nslayoutmanager.md) in macOS11 and earlier. In macOS12 and later, consider using [`NSLayoutManager`](nslayoutmanager.md) which provides improved support for international scripts.

##### Subclassing Notes

`NSTypesetter` provides concrete subclasses with default implementation interfacing with the Cocoa text system. By subclassing `NSTypesetter`, an application can override the [`layoutParagraph(at:)`](nstypesetter/layoutparagraph(at:).md) method to integrate a custom typesetting engine into the Cocoa text system. On the other hand, an application can subclass [`NSATSTypesetter`](nsatstypesetter.md) and override the glyph storage interface to integrate the concrete subclass into its own custom layout system.

`NSTypesetter` methods belong to three categories: glyph storage interface methods, layout phase interface methods, and core typesetter methods. The glyph storage interface methods map to [`NSLayoutManager`](nslayoutmanager.md) methods. The typesetter itself calls these methods, and their default implementations call the Cocoa layout manager. An `NSTypesetter` subclass can override these methods to call its own glyph storage facility, in which case it should override all of them. (This doesn’t preclude the overridden method calling its superclass implementation if appropriate).

The layout phase interface provides control points similar to delegate methods; if implemented, the system invokes these methods to notify an `NSTypesetter` subclass of events in the layout process so it can intervene as needed.

The remainder of the `NSTypesetter` methods are primitive, core typesetter methods. The core typesetter methods correlate with typesetting state attributes; the layout manager calls these methods to store its values before starting the layout process. If you subclass `NSTypesetter` and override the glyph storage interface methods, you can call the core methods to control the typesetter directly.

###### Glyph Storage Interface

Override these methods to use `NSTypesetter`’s built-in concrete subclass, [`NSATSTypesetter`](nsatstypesetter.md), with a custom glyph storage and layout system other than the Cocoa layout manager and text container mechanism.

- [`characterRange(forGlyphRange:actualGlyphRange:)`](nstypesetter/characterrange(forglyphrange:actualglyphrange:).md)
- [`glyphRange(forCharacterRange:actualCharacterRange:)`](nstypesetter/glyphrange(forcharacterrange:actualcharacterrange:).md)
- [`getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:)`](nstypesetter/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:bidilevels:).md)
- [`getLineFragmentRect(_:usedRect:remaining:forStartingGlyphAt:proposedRect:lineSpacing:paragraphSpacingBefore:paragraphSpacingAfter:)`](nstypesetter/getlinefragmentrect(_:usedrect:remaining:forstartingglyphat:proposedrect:linespacing:paragraphspacingbefore:paragraphspacingafter:).md)
- [`setLineFragmentRect(_:forGlyphRange:usedRect:baselineOffset:)`](nstypesetter/setlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
- [`substituteGlyphs(in:withGlyphs:)`](nstypesetter/substituteglyphs(in:withglyphs:).md)
- [`insertGlyph(_:atGlyphIndex:characterIndex:)`](nstypesetter/insertglyph(_:atglyphindex:characterindex:).md)
- [`deleteGlyphs(in:)`](nstypesetter/deleteglyphs(in:).md)
- [`setNotShownAttribute(_:forGlyphRange:)`](nstypesetter/setnotshownattribute(_:forglyphrange:).md)
- [`setDrawsOutsideLineFragment(_:forGlyphRange:)`](nstypesetter/setdrawsoutsidelinefragment(_:forglyphrange:).md)
- [`setLocation(_:withAdvancements:forStartOfGlyphRange:)`](nstypesetter/setlocation(_:withadvancements:forstartofglyphrange:).md)
- [`setAttachmentSize(_:forGlyphRange:)`](nstypesetter/setattachmentsize(_:forglyphrange:).md)
- [`setBidiLevels(_:forGlyphRange:)`](nstypesetter/setbidilevels(_:forglyphrange:).md)

###### Layout Phase Interface

Override these methods to customize the text layout process, including modifying line fragments, controlling line breaking and hyphenation, and controlling the behavior of tabs and other control glyphs.

- [`willSetLineFragmentRect(_:forGlyphRange:usedRect:baselineOffset:)`](nstypesetter/willsetlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
- [`shouldBreakLine(byWordBeforeCharacterAt:)`](nstypesetter/shouldbreakline(bywordbeforecharacterat:).md)
- [`shouldBreakLine(byHyphenatingBeforeCharacterAt:)`](nstypesetter/shouldbreakline(byhyphenatingbeforecharacterat:).md)
- [`hyphenationFactor(forGlyphAt:)`](nstypesetter/hyphenationfactor(forglyphat:).md)
- [`hyphenCharacter(forGlyphAt:)`](nstypesetter/hyphencharacter(forglyphat:).md)
- [`boundingBox(forControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)`](nstypesetter/boundingbox(forcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md)

## Topics

### Getting a typesetter
- [class var sharedSystemTypesetter: NSTypesetter](nstypesetter/sharedsystemtypesetter.md)
  Returns a shared instance of a reentrant typesetter.
- [class func sharedSystemTypesetter(for: NSLayoutManager.TypesetterBehavior) -> Any](nstypesetter/sharedsystemtypesetter(for:).md)
  Returns a shared instance of a reentrant typesetter that implements typesetting with the specified behavior.
### Getting information about a typesetter
- [class var defaultTypesetterBehavior: NSLayoutManager.TypesetterBehavior](nstypesetter/defaulttypesetterbehavior.md)
  Returns the default typesetter behavior.
### Getting information about glyphs
- [class func printingAdjustment(in: NSLayoutManager, forNominallySpacedGlyphRange: NSRange, packedGlyphs: UnsafePointer<UInt8>, count: Int) -> NSSize](nstypesetter/printingadjustment(in:fornominallyspacedglyphrange:packedglyphs:count:).md)
  Returns the interglyph spacing in the specified range when sent to a printer.
- [func baselineOffset(in: NSLayoutManager, glyphIndex: Int) -> CGFloat](nstypesetter/baselineoffset(in:glyphindex:).md)
  Returns the distance from the bottom of the line fragment rectangle in which the glyph resides to the glyph baseline.
### Accessing the layout manager
- [var layoutManager: NSLayoutManager?](nstypesetter/layoutmanager.md)
  Returns the layout manager for the text being typeset.
- [var usesFontLeading: Bool](nstypesetter/usesfontleading.md)
  Returns whether the typesetter uses the leading (or line gap) value specified in the font metric information of the current font.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](nstypesetter/typesetterbehavior.md)
  Returns the current typesetter behavior.
- [var hyphenationFactor: Float](nstypesetter/hyphenationfactor.md)
  Returns the current hyphenation factor.
### Managing text containers
- [var currentTextContainer: NSTextContainer?](nstypesetter/currenttextcontainer.md)
  Returns the text container for the text being typeset.
- [var textContainers: NSArray?](nstypesetter/textcontainers.md)
  Returns an array containing the text containers belonging to the current layout manager.
- [var lineFragmentPadding: CGFloat](nstypesetter/linefragmentpadding.md)
  Returns the current line fragment padding, in points.
### Performing font substitution
- [func substituteFont(for: NSFont) -> NSFont](nstypesetter/substitutefont(for:).md)
  Returns a screen font suitable for use in place of a given font.
### Getting the location of text tabs
- [func textTab(forGlyphLocation: CGFloat, writingDirection: NSWritingDirection, maxLocation: CGFloat) -> NSTextTab?](nstypesetter/texttab(forglyphlocation:writingdirection:maxlocation:).md)
  Returns the text tab next closest to a given glyph location within the given parameters.
### Bidirectional text processing
- [var bidiProcessingEnabled: Bool](nstypesetter/bidiprocessingenabled.md)
  Returns whether bidirectional text processing is enabled.
### Accessing paragraph typesetting information
- [var currentParagraphStyle: NSParagraphStyle?](nstypesetter/currentparagraphstyle.md)
  Returns the paragraph style object for the text being typeset.
- [var attributedString: NSAttributedString?](nstypesetter/attributedstring.md)
  Returns the text backing store, usually an instance of `NSTextStorage`.
- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](nstypesetter/setparagraphglyphrange(_:separatorglyphrange:).md)
  Sets the current glyph range being processed.
- [var paragraphGlyphRange: NSRange](nstypesetter/paragraphglyphrange.md)
  Returns the glyph range currently being processed.
- [var paragraphSeparatorGlyphRange: NSRange](nstypesetter/paragraphseparatorglyphrange.md)
  Returns the current paragraph separator range.
- [var paragraphCharacterRange: NSRange](nstypesetter/paragraphcharacterrange.md)
  Returns the character range currently being processed.
- [var paragraphSeparatorCharacterRange: NSRange](nstypesetter/paragraphseparatorcharacterrange.md)
  Returns the current paragraph separator character range.
- [var attributesForExtraLineFragment: [NSAttributedString.Key : Any]](nstypesetter/attributesforextralinefragment.md)
  Returns the attributes used to lay out the extra line fragment.
### Getting spacing information
- [func lineSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nstypesetter/linespacing(afterglyphat:withproposedlinefragmentrect:).md)
  Returns the line spacing in effect following the specified glyph.
- [func paragraphSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nstypesetter/paragraphspacing(afterglyphat:withproposedlinefragmentrect:).md)
  Returns the paragraph spacing that is in effect after the specified glyph.
- [func paragraphSpacing(beforeGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](nstypesetter/paragraphspacing(beforeglyphat:withproposedlinefragmentrect:).md)
  Returns the number of points of space—added before a paragraph—that is in effect before the specified glyph.
### Laying out a paragraph
- [func layoutParagraph(at: NSPointPointer) -> Int](nstypesetter/layoutparagraph(at:).md)
  Lays out glyphs in the current glyph range until the next paragraph separator is reached.
- [func beginParagraph()](nstypesetter/beginparagraph.md)
  Sets up layout parameters at the beginning of a paragraph.
- [func endParagraph()](nstypesetter/endparagraph.md)
  Sets up layout parameters at the end of a paragraph.
- [func beginLine(withGlyphAt: Int)](nstypesetter/beginline(withglyphat:).md)
  Sets up layout parameters at the beginning of a line during typesetting.
- [func endLine(withGlyphRange: NSRange)](nstypesetter/endline(withglyphrange:).md)
  Sets up layout parameters at the end of a line during typesetting.
### Laying out characters
- [func layoutCharacters(in: NSRange, for: NSLayoutManager, maximumNumberOfLineFragments: Int) -> NSRange](nstypesetter/layoutcharacters(in:for:maximumnumberoflinefragments:).md)
  Lays out characters in the given character range for the specified layout manager.
### Laying out glyphs
- [func layoutGlyphs(in: NSLayoutManager, startingAtGlyphIndex: Int, maxNumberOfLineFragments: Int, nextGlyphIndex: UnsafeMutablePointer<Int>)](nstypesetter/layoutglyphs(in:startingatglyphindex:maxnumberoflinefragments:nextglyphindex:).md)
  Lays out glyphs in the specified layout manager starting at a specified glyph.
- [func boundingBox(forControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](nstypesetter/boundingbox(forcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md)
  Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [func getLineFragmentRect(NSRectPointer, usedRect: NSRectPointer, forParagraphSeparatorGlyphRange: NSRange, atProposedOrigin: NSPoint)](nstypesetter/getlinefragmentrect(_:usedrect:forparagraphseparatorglyphrange:atproposedorigin:).md)
  Calculates the line fragment rectangle and line fragment used rectangle for blank lines.
- [func getLineFragmentRect(NSRectPointer!, usedRect: NSRectPointer!, remaining: NSRectPointer!, forStartingGlyphAt: Int, proposedRect: NSRect, lineSpacing: CGFloat, paragraphSpacingBefore: CGFloat, paragraphSpacingAfter: CGFloat)](nstypesetter/getlinefragmentrect(_:usedrect:remaining:forstartingglyphat:proposedrect:linespacing:paragraphspacingbefore:paragraphspacingafter:).md)
  Calculates line fragment rectangle, line fragment used rectangle, and remaining rectangle for a line fragment.
- [func hyphenCharacter(forGlyphAt: Int) -> UTF32Char](nstypesetter/hyphencharacter(forglyphat:).md)
  Returns the hyphen character to be inserted after the specified glyph.
- [func hyphenationFactor(forGlyphAt: Int) -> Float](nstypesetter/hyphenationfactor(forglyphat:).md)
  Returns the hyphenation factor in effect at a specified location.
- [func shouldBreakLine(byHyphenatingBeforeCharacterAt: Int) -> Bool](nstypesetter/shouldbreakline(byhyphenatingbeforecharacterat:).md)
  Returns whether the line being laid out should be broken by hyphenating at the specified character.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](nstypesetter/shouldbreakline(bywordbeforecharacterat:).md)
  Returns whether the line being laid out should be broken by a word break at the specified character.
- [func willSetLineFragmentRect(NSRectPointer, forGlyphRange: NSRange, usedRect: NSRectPointer, baselineOffset: UnsafeMutablePointer<CGFloat>)](nstypesetter/willsetlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
  Called by the typesetter just prior to storing the actual line fragment rectangle location in the layout manager.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](nstypesetter/sethardinvalidation(_:forglyphrange:).md)
  Sets whether to force the layout manager to invalidate the specified portion of the glyph cache when invalidating layout.
### Interfacing with Glyph Storage
- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](nstypesetter/characterrange(forglyphrange:actualglyphrange:).md)
  Returns the range for the characters in the receiver’s text store that are mapped to the specified glyphs.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](nstypesetter/glyphrange(forcharacterrange:actualcharacterrange:).md)
  Returns the range for the glyphs mapped to the characters of the text store in the specified range.
- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](nstypesetter/setattachmentsize(_:forglyphrange:).md)
  Sets the size the specified glyphs (assumed to be attachments) will be asked to draw themselves at.
- [func setBidiLevels(UnsafePointer<UInt8>!, forGlyphRange: NSRange)](nstypesetter/setbidilevels(_:forglyphrange:).md)
  Sets the direction of the specified glyphs for bidirectional text.
- [func setDrawsOutsideLineFragment(Bool, forGlyphRange: NSRange)](nstypesetter/setdrawsoutsidelinefragment(_:forglyphrange:).md)
  Sets whether the specified glyphs exceed the bounds of the line fragment in which they are laid out.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect, baselineOffset: CGFloat)](nstypesetter/setlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
  Sets the line fragment rectangle where the specified glyphs are laid out.
- [func setLocation(NSPoint, withAdvancements: UnsafePointer<CGFloat>!, forStartOfGlyphRange: NSRange)](nstypesetter/setlocation(_:withadvancements:forstartofglyphrange:).md)
  Sets the location where the specified glyphs are laid out.
- [func setNotShownAttribute(Bool, forGlyphRange: NSRange)](nstypesetter/setnotshownattribute(_:forglyphrange:).md)
  Sets whether the specified glyphs are not shown.
### Deprecated
- [func actionForControlCharacter(at: Int) -> NSTypesetterControlCharacterAction](nstypesetter/actionforcontrolcharacter(at:).md)
  Returns the action associated with a control character.
- [func deleteGlyphs(in: NSRange)](nstypesetter/deleteglyphs(in:).md)
  Deletes the specified glyphs from the glyph cache maintained by the layout manager.
- [func substituteGlyphs(in: NSRange, withGlyphs: UnsafeMutablePointer<NSGlyph>!)](nstypesetter/substituteglyphs(in:withglyphs:).md)
  Replaces the specified glyphs with specified replacement glyphs.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>!, characterIndexes: UnsafeMutablePointer<Int>!, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits: UnsafeMutablePointer<ObjCBool>!, bidiLevels: UnsafeMutablePointer<UInt8>!) -> Int](nstypesetter/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:bidilevels:).md)
  Extracts the information needed to lay out the provided glyphs from the provided range.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](nstypesetter/insertglyph(_:atglyphindex:characterindex:).md)
  Enables the typesetter to insert a new glyph into the stream.
- [struct NSTypesetterControlCharacterAction](nstypesettercontrolcharacteraction.md)
  The following constants are possible values returned by the [`actionForControlCharacter(at:)`](nstypesetter/actionforcontrolcharacter(at:).md) method to determine the action associated with a control character.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSATSTypesetter](nsatstypesetter.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class NSTextStorage](nstextstorage.md)
  The fundamental storage mechanism of TextKit that contains the text managed by the system.
- [class NSLayoutManager](nslayoutmanager.md)
  An object that coordinates the layout and display of text characters.
- [class NSATSTypesetter](nsatstypesetter.md)
  A concrete typesetter object that places glyphs during the text layout process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/AppKit/nstypesetter)*