# NSTypesetter

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

An abstract class that performs various type layout tasks.

**Availability**:
- macOS

## Declaration

```swift
class NSTypesetter
```

```objc
@interface NSTypesetter : NSObject
```

#### Overview

[`NSLayoutManager`](./nslayoutmanager.md) uses concrete subclasses of [`NSTypesetter`](./nstypesetter.md) to perform line layout, which includes word wrapping, hyphenation, and line breaking in either vertical or horizontal rectangles. By default, the text system uses the concrete subclass [`NSATSTypesetter`](./nsatstypesetter.md).

> **Note**:  Use this class with [`NSLayoutManager`](./nslayoutmanager.md) in macOS11 and earlier. In macOS12 and later, consider using [`NSLayoutManager`](./nslayoutmanager.md) which provides improved support for international scripts.

##### Subclassing Notes

`NSTypesetter` provides concrete subclasses with default implementation interfacing with the Cocoa text system. By subclassing `NSTypesetter`, an application can override the [`layoutParagraph(at:)`](./nstypesetter/layoutparagraph%28at%29.md) method to integrate a custom typesetting engine into the Cocoa text system. On the other hand, an application can subclass [`NSATSTypesetter`](./nsatstypesetter.md) and override the glyph storage interface to integrate the concrete subclass into its own custom layout system.

`NSTypesetter` methods belong to three categories: glyph storage interface methods, layout phase interface methods, and core typesetter methods. The glyph storage interface methods map to [`NSLayoutManager`](./nslayoutmanager.md) methods. The typesetter itself calls these methods, and their default implementations call the Cocoa layout manager. An `NSTypesetter` subclass can override these methods to call its own glyph storage facility, in which case it should override all of them. (This doesn’t preclude the overridden method calling its superclass implementation if appropriate).

The layout phase interface provides control points similar to delegate methods; if implemented, the system invokes these methods to notify an `NSTypesetter` subclass of events in the layout process so it can intervene as needed.

The remainder of the `NSTypesetter` methods are primitive, core typesetter methods. The core typesetter methods correlate with typesetting state attributes; the layout manager calls these methods to store its values before starting the layout process. If you subclass `NSTypesetter` and override the glyph storage interface methods, you can call the core methods to control the typesetter directly.

###### Glyph Storage Interface

Override these methods to use `NSTypesetter`’s built-in concrete subclass, [`NSATSTypesetter`](./nsatstypesetter.md), with a custom glyph storage and layout system other than the Cocoa layout manager and text container mechanism.

- [`characterRange(forGlyphRange:actualGlyphRange:)`](./nstypesetter/characterrange%28forglyphrange,actualglyphrange%29.md)
- [`glyphRange(forCharacterRange:actualCharacterRange:)`](./nstypesetter/glyphrange%28forcharacterrange,actualcharacterrange%29.md)
- [`getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:)`](./nstypesetter/getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits,bidilevels%29.md)
- [`getLineFragmentRect(_:usedRect:remaining:forStartingGlyphAt:proposedRect:lineSpacing:paragraphSpacingBefore:paragraphSpacingAfter:)`](./nstypesetter/getlinefragmentrect%28_,usedrect,remaining,forstartingglyphat,proposedrect,linespacing,paragraphspacingbefore,paragraphspacingafter%29.md)
- [`setLineFragmentRect(_:forGlyphRange:usedRect:baselineOffset:)`](./nstypesetter/setlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
- [`substituteGlyphs(in:withGlyphs:)`](./nstypesetter/substituteglyphs%28in,withglyphs%29.md)
- [`insertGlyph(_:atGlyphIndex:characterIndex:)`](./nstypesetter/insertglyph%28_,atglyphindex,characterindex%29.md)
- [`deleteGlyphs(in:)`](./nstypesetter/deleteglyphs%28in%29.md)
- [`setNotShownAttribute(_:forGlyphRange:)`](./nstypesetter/setnotshownattribute%28_,forglyphrange%29.md)
- [`setDrawsOutsideLineFragment(_:forGlyphRange:)`](./nstypesetter/setdrawsoutsidelinefragment%28_,forglyphrange%29.md)
- [`setLocation(_:withAdvancements:forStartOfGlyphRange:)`](./nstypesetter/setlocation%28_,withadvancements,forstartofglyphrange%29.md)
- [`setAttachmentSize(_:forGlyphRange:)`](./nstypesetter/setattachmentsize%28_,forglyphrange%29.md)
- [`setBidiLevels(_:forGlyphRange:)`](./nstypesetter/setbidilevels%28_,forglyphrange%29.md)

###### Layout Phase Interface

Override these methods to customize the text layout process, including modifying line fragments, controlling line breaking and hyphenation, and controlling the behavior of tabs and other control glyphs.

- [`willSetLineFragmentRect(_:forGlyphRange:usedRect:baselineOffset:)`](./nstypesetter/willsetlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
- [`shouldBreakLine(byWordBeforeCharacterAt:)`](./nstypesetter/shouldbreakline%28bywordbeforecharacterat%29.md)
- [`shouldBreakLine(byHyphenatingBeforeCharacterAt:)`](./nstypesetter/shouldbreakline%28byhyphenatingbeforecharacterat%29.md)
- [`hyphenationFactor(forGlyphAt:)`](./nstypesetter/hyphenationfactor%28forglyphat%29.md)
- [`hyphenCharacter(forGlyphAt:)`](./nstypesetter/hyphencharacter%28forglyphat%29.md)
- [`boundingBox(forControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)`](./nstypesetter/boundingbox%28forcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md)

## Topics

### Getting a typesetter
- [class var sharedSystemTypesetter: NSTypesetter](./nstypesetter/sharedsystemtypesetter.md)
  Returns a shared instance of a reentrant typesetter.
- [class func sharedSystemTypesetter(for: NSLayoutManager.TypesetterBehavior) -> Any](./nstypesetter/sharedsystemtypesetter%28for%29.md)
  Returns a shared instance of a reentrant typesetter that implements typesetting with the specified behavior.
### Getting information about a typesetter
- [class var defaultTypesetterBehavior: NSLayoutManager.TypesetterBehavior](./nstypesetter/defaulttypesetterbehavior.md)
  Returns the default typesetter behavior.
### Getting information about glyphs
- [class func printingAdjustment(in: NSLayoutManager, forNominallySpacedGlyphRange: NSRange, packedGlyphs: UnsafePointer<UInt8>, count: Int) -> NSSize](./nstypesetter/printingadjustment%28in,fornominallyspacedglyphrange,packedglyphs,count%29.md)
  Returns the interglyph spacing in the specified range when sent to a printer.
- [func baselineOffset(in: NSLayoutManager, glyphIndex: Int) -> CGFloat](./nstypesetter/baselineoffset%28in,glyphindex%29.md)
  Returns the distance from the bottom of the line fragment rectangle in which the glyph resides to the glyph baseline.
### Accessing the layout manager
- [var layoutManager: NSLayoutManager?](./nstypesetter/layoutmanager.md)
  Returns the layout manager for the text being typeset.
- [var usesFontLeading: Bool](./nstypesetter/usesfontleading.md)
  Returns whether the typesetter uses the leading (or line gap) value specified in the font metric information of the current font.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](./nstypesetter/typesetterbehavior.md)
  Returns the current typesetter behavior.
- [var hyphenationFactor: Float](./nstypesetter/hyphenationfactor.md)
  Returns the current hyphenation factor.
### Managing text containers
- [var currentTextContainer: NSTextContainer?](./nstypesetter/currenttextcontainer.md)
  Returns the text container for the text being typeset.
- [var textContainers: NSArray?](./nstypesetter/textcontainers.md)
  Returns an array containing the text containers belonging to the current layout manager.
- [var lineFragmentPadding: CGFloat](./nstypesetter/linefragmentpadding.md)
  Returns the current line fragment padding, in points.
### Performing font substitution
- [func substituteFont(for: NSFont) -> NSFont](./nstypesetter/substitutefont%28for%29.md)
  Returns a screen font suitable for use in place of a given font.
### Getting the location of text tabs
- [func textTab(forGlyphLocation: CGFloat, writingDirection: NSWritingDirection, maxLocation: CGFloat) -> NSTextTab?](./nstypesetter/texttab%28forglyphlocation,writingdirection,maxlocation%29.md)
  Returns the text tab next closest to a given glyph location within the given parameters.
### Bidirectional text processing
- [var bidiProcessingEnabled: Bool](./nstypesetter/bidiprocessingenabled.md)
  Returns whether bidirectional text processing is enabled.
### Accessing paragraph typesetting information
- [var currentParagraphStyle: NSParagraphStyle?](./nstypesetter/currentparagraphstyle.md)
  Returns the paragraph style object for the text being typeset.
- [var attributedString: NSAttributedString?](./nstypesetter/attributedstring.md)
  Returns the text backing store, usually an instance of `NSTextStorage`.
- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](./nstypesetter/setparagraphglyphrange%28_,separatorglyphrange%29.md)
  Sets the current glyph range being processed.
- [var paragraphGlyphRange: NSRange](./nstypesetter/paragraphglyphrange.md)
  Returns the glyph range currently being processed.
- [var paragraphSeparatorGlyphRange: NSRange](./nstypesetter/paragraphseparatorglyphrange.md)
  Returns the current paragraph separator range.
- [var paragraphCharacterRange: NSRange](./nstypesetter/paragraphcharacterrange.md)
  Returns the character range currently being processed.
- [var paragraphSeparatorCharacterRange: NSRange](./nstypesetter/paragraphseparatorcharacterrange.md)
  Returns the current paragraph separator character range.
- [var attributesForExtraLineFragment: [NSAttributedString.Key : Any]](./nstypesetter/attributesforextralinefragment.md)
  Returns the attributes used to lay out the extra line fragment.
### Getting spacing information
- [func lineSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./nstypesetter/linespacing%28afterglyphat,withproposedlinefragmentrect%29.md)
  Returns the line spacing in effect following the specified glyph.
- [func paragraphSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./nstypesetter/paragraphspacing%28afterglyphat,withproposedlinefragmentrect%29.md)
  Returns the paragraph spacing that is in effect after the specified glyph.
- [func paragraphSpacing(beforeGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./nstypesetter/paragraphspacing%28beforeglyphat,withproposedlinefragmentrect%29.md)
  Returns the number of points of space—added before a paragraph—that is in effect before the specified glyph.
### Laying out a paragraph
- [func layoutParagraph(at: NSPointPointer) -> Int](./nstypesetter/layoutparagraph%28at%29.md)
  Lays out glyphs in the current glyph range until the next paragraph separator is reached.
- [func beginParagraph()](./nstypesetter/beginparagraph%28%29.md)
  Sets up layout parameters at the beginning of a paragraph.
- [func endParagraph()](./nstypesetter/endparagraph%28%29.md)
  Sets up layout parameters at the end of a paragraph.
- [func beginLine(withGlyphAt: Int)](./nstypesetter/beginline%28withglyphat%29.md)
  Sets up layout parameters at the beginning of a line during typesetting.
- [func endLine(withGlyphRange: NSRange)](./nstypesetter/endline%28withglyphrange%29.md)
  Sets up layout parameters at the end of a line during typesetting.
### Laying out characters
- [func layoutCharacters(in: NSRange, for: NSLayoutManager, maximumNumberOfLineFragments: Int) -> NSRange](./nstypesetter/layoutcharacters%28in,for,maximumnumberoflinefragments%29.md)
  Lays out characters in the given character range for the specified layout manager.
### Laying out glyphs
- [func layoutGlyphs(in: NSLayoutManager, startingAtGlyphIndex: Int, maxNumberOfLineFragments: Int, nextGlyphIndex: UnsafeMutablePointer<Int>)](./nstypesetter/layoutglyphs%28in,startingatglyphindex,maxnumberoflinefragments,nextglyphindex%29.md)
  Lays out glyphs in the specified layout manager starting at a specified glyph.
- [func boundingBox(forControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](./nstypesetter/boundingbox%28forcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md)
  Returns the bounding rectangle for the specified control glyph with the specified parameters.
- [func getLineFragmentRect(NSRectPointer, usedRect: NSRectPointer, forParagraphSeparatorGlyphRange: NSRange, atProposedOrigin: NSPoint)](./nstypesetter/getlinefragmentrect%28_,usedrect,forparagraphseparatorglyphrange,atproposedorigin%29.md)
  Calculates the line fragment rectangle and line fragment used rectangle for blank lines.
- [func getLineFragmentRect(NSRectPointer!, usedRect: NSRectPointer!, remaining: NSRectPointer!, forStartingGlyphAt: Int, proposedRect: NSRect, lineSpacing: CGFloat, paragraphSpacingBefore: CGFloat, paragraphSpacingAfter: CGFloat)](./nstypesetter/getlinefragmentrect%28_,usedrect,remaining,forstartingglyphat,proposedrect,linespacing,paragraphspacingbefore,paragraphspacingafter%29.md)
  Calculates line fragment rectangle, line fragment used rectangle, and remaining rectangle for a line fragment.
- [func hyphenCharacter(forGlyphAt: Int) -> UTF32Char](./nstypesetter/hyphencharacter%28forglyphat%29.md)
  Returns the hyphen character to be inserted after the specified glyph.
- [func hyphenationFactor(forGlyphAt: Int) -> Float](./nstypesetter/hyphenationfactor%28forglyphat%29.md)
  Returns the hyphenation factor in effect at a specified location.
- [func shouldBreakLine(byHyphenatingBeforeCharacterAt: Int) -> Bool](./nstypesetter/shouldbreakline%28byhyphenatingbeforecharacterat%29.md)
  Returns whether the line being laid out should be broken by hyphenating at the specified character.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](./nstypesetter/shouldbreakline%28bywordbeforecharacterat%29.md)
  Returns whether the line being laid out should be broken by a word break at the specified character.
- [func willSetLineFragmentRect(NSRectPointer, forGlyphRange: NSRange, usedRect: NSRectPointer, baselineOffset: UnsafeMutablePointer<CGFloat>)](./nstypesetter/willsetlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
  Called by the typesetter just prior to storing the actual line fragment rectangle location in the layout manager.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](./nstypesetter/sethardinvalidation%28_,forglyphrange%29.md)
  Sets whether to force the layout manager to invalidate the specified portion of the glyph cache when invalidating layout.
### Interfacing with Glyph Storage
- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](./nstypesetter/characterrange%28forglyphrange,actualglyphrange%29.md)
  Returns the range for the characters in the receiver’s text store that are mapped to the specified glyphs.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](./nstypesetter/glyphrange%28forcharacterrange,actualcharacterrange%29.md)
  Returns the range for the glyphs mapped to the characters of the text store in the specified range.
- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](./nstypesetter/setattachmentsize%28_,forglyphrange%29.md)
  Sets the size the specified glyphs (assumed to be attachments) will be asked to draw themselves at.
- [func setBidiLevels(UnsafePointer<UInt8>!, forGlyphRange: NSRange)](./nstypesetter/setbidilevels%28_,forglyphrange%29.md)
  Sets the direction of the specified glyphs for bidirectional text.
- [func setDrawsOutsideLineFragment(Bool, forGlyphRange: NSRange)](./nstypesetter/setdrawsoutsidelinefragment%28_,forglyphrange%29.md)
  Sets whether the specified glyphs exceed the bounds of the line fragment in which they are laid out.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect, baselineOffset: CGFloat)](./nstypesetter/setlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
  Sets the line fragment rectangle where the specified glyphs are laid out.
- [func setLocation(NSPoint, withAdvancements: UnsafePointer<CGFloat>!, forStartOfGlyphRange: NSRange)](./nstypesetter/setlocation%28_,withadvancements,forstartofglyphrange%29.md)
  Sets the location where the specified glyphs are laid out.
- [func setNotShownAttribute(Bool, forGlyphRange: NSRange)](./nstypesetter/setnotshownattribute%28_,forglyphrange%29.md)
  Sets whether the specified glyphs are not shown.
### Deprecated
- [func actionForControlCharacter(at: Int) -> NSTypesetterControlCharacterAction](./nstypesetter/actionforcontrolcharacter%28at%29.md)
  Returns the action associated with a control character.
- [func deleteGlyphs(in: NSRange)](./nstypesetter/deleteglyphs%28in%29.md)
  Deletes the specified glyphs from the glyph cache maintained by the layout manager.
- [func substituteGlyphs(in: NSRange, withGlyphs: UnsafeMutablePointer<NSGlyph>!)](./nstypesetter/substituteglyphs%28in,withglyphs%29.md)
  Replaces the specified glyphs with specified replacement glyphs.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>!, characterIndexes: UnsafeMutablePointer<Int>!, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits: UnsafeMutablePointer<ObjCBool>!, bidiLevels: UnsafeMutablePointer<UInt8>!) -> Int](./nstypesetter/getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits,bidilevels%29.md)
  Extracts the information needed to lay out the provided glyphs from the provided range.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](./nstypesetter/insertglyph%28_,atglyphindex,characterindex%29.md)
  Enables the typesetter to insert a new glyph into the stream.
- [struct NSTypesetterControlCharacterAction](./nstypesettercontrolcharacteraction.md)
  The following constants are possible values returned by the [`actionForControlCharacter(at:)`](./nstypesetter/actionforcontrolcharacter%28at%29.md) method to determine the action associated with a control character.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [NSATSTypesetter](./nsatstypesetter.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### TextKit 1
- [class NSTextStorage](./nstextstorage.md)
  The fundamental storage mechanism of TextKit that contains the text managed by the system.
- [class NSLayoutManager](./nslayoutmanager.md)
  An object that coordinates the layout and display of text characters.
- [class NSATSTypesetter](./nsatstypesetter.md)
  A concrete typesetter object that places glyphs during the text layout process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter)*