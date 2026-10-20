# NSATSTypesetter

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A concrete typesetter object that places glyphs during the text layout process.

**Availability**:
- macOS

## Declaration

```swift
class NSATSTypesetter
```

```objc
@interface NSATSTypesetter : NSTypesetter
```

#### Overview

An [`NSATSTypesetter`](./nsatstypesetter.md) object creates line fragment rectangles, positions glyphs within the line fragments, determines line breaks by word wrapping and hyphenation, and handles tab positioning. This object encapsulates the advanced typesetting capabilities of Core Text. [`NSATSTypesetter`](./nsatstypesetter.md) provides line and character spacing accuracy and supports many languages, including bidirectional languages.

> **Note**:  Use this class with [`NSLayoutManager`](./nslayoutmanager.md) in macOS11 and earlier. In macOS12 and later, consider using [`NSTextLayoutManager`](./nstextlayoutmanager.md) which provides improved support for international scripts.

## Topics

### Getting the shared typesetter object
- [class var shared: NSATSTypesetter](./nsatstypesetter/shared.md)
  Returns a shared instance of the typesetter.
### Accessing the layout manager
- [var layoutManager: NSLayoutManager?](./nsatstypesetter/layoutmanager.md)
  The layout manager for the text being typeset.
- [var usesFontLeading: Bool](./nsatstypesetter/usesfontleading.md)
  A Boolean value controlling whether the typesetter uses the leading (or line gap) value specified in the font metric information.
- [var typesetterBehavior: NSLayoutManager.TypesetterBehavior](./nsatstypesetter/typesetterbehavior.md)
  The current typesetter behavior value.
- [var hyphenationFactor: Float](./nsatstypesetter/hyphenationfactor.md)
  The threshold controlling when hyphenation is attempted.
- [var bidiProcessingEnabled: Bool](./nsatstypesetter/bidiprocessingenabled.md)
  A Boolean value controlling whether the typesetter performs bidirectional text processing.
### Getting the text container
- [var currentTextContainer: NSTextContainer?](./nsatstypesetter/currenttextcontainer.md)
  The text container for the text being typeset.
- [var lineFragmentPadding: CGFloat](./nsatstypesetter/linefragmentpadding.md)
  The amount (in points) by which text is inset within line fragment rectangles.
### Performing font substitution
- [func substituteFont(for: NSFont) -> NSFont](./nsatstypesetter/substitutefont%28for%29.md)
  Returns a screen font suitable for use in place of the specified original font,.
### Getting the location of text tabs
- [func textTab(forGlyphLocation: CGFloat, writingDirection: NSWritingDirection, maxLocation: CGFloat) -> NSTextTab?](./nsatstypesetter/texttab%28forglyphlocation,writingdirection,maxlocation%29.md)
  Returns the text tab closest to the specified glyph location and not beyond a maximum position.
### Accessing paragraph information
- [var attributedString: NSAttributedString?](./nsatstypesetter/attributedstring.md)
  The backing store that contains the text on which this typesetter operates.
- [func setParagraphGlyphRange(NSRange, separatorGlyphRange: NSRange)](./nsatstypesetter/setparagraphglyphrange%28_,separatorglyphrange%29.md)
  Sets the glyph range being processed and the paragraph separator glyph range (the range of the paragraph separator character or characters).
- [var paragraphGlyphRange: NSRange](./nsatstypesetter/paragraphglyphrange.md)
  The current glyph range being processed.
- [var paragraphSeparatorGlyphRange: NSRange](./nsatstypesetter/paragraphseparatorglyphrange.md)
  The current paragraph separator range that contains the current glyph range and extends from one paragraph separator character to the next.
### Laying out a paragraph
- [func layoutParagraph(at: UnsafeMutablePointer<NSPoint>) -> Int](./nsatstypesetter/layoutparagraph%28at%29.md)
  Lays out glyphs in the current glyph range until the next paragraph separator is reached.
### Getting Spacing Information
- [func lineSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./nsatstypesetter/linespacing%28afterglyphat,withproposedlinefragmentrect%29.md)
  Returns the line spacing in effect following the specified glyph.
- [func paragraphSpacing(afterGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./nsatstypesetter/paragraphspacing%28afterglyphat,withproposedlinefragmentrect%29.md)
  Returns the number of points of space added following a paragraph, in effect after the specified glyph.
- [func paragraphSpacing(beforeGlyphAt: Int, withProposedLineFragmentRect: NSRect) -> CGFloat](./nsatstypesetter/paragraphspacing%28beforeglyphat,withproposedlinefragmentrect%29.md)
  Returns the number of points of space added before a paragraph, which is in effect before the specified glyph.
### Laying Out Glyphs
- [func boundingBox(forControlGlyphAt: Int, for: NSTextContainer, proposedLineFragment: NSRect, glyphPosition: NSPoint, characterIndex: Int) -> NSRect](./nsatstypesetter/boundingbox%28forcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md)
  Returns the bounding rectangle for a control glyph, at the specified glyph position and character index in the text container.
- [func getLineFragmentRect(UnsafeMutablePointer<NSRect>, usedRect: UnsafeMutablePointer<NSRect>, forParagraphSeparatorGlyphRange: NSRange, atProposedOrigin: NSPoint)](./nsatstypesetter/getlinefragmentrect%28_,usedrect,forparagraphseparatorglyphrange,atproposedorigin%29.md)
  Calculates the line fragment rectangle and the portion of the rectangle that contains marks.
- [func hyphenCharacter(forGlyphAt: Int) -> UTF32Char](./nsatstypesetter/hyphencharacter%28forglyphat%29.md)
  Returns the hyphen character to be inserted after the specified glyph when hyphenation is enabled in the layout manager.
- [func hyphenationFactor(forGlyphAt: Int) -> Float](./nsatstypesetter/hyphenationfactor%28forglyphat%29.md)
  Returns the hyphenation factor in effect at the specified glyph index.
- [func shouldBreakLine(byHyphenatingBeforeCharacterAt: Int) -> Bool](./nsatstypesetter/shouldbreakline%28byhyphenatingbeforecharacterat%29.md)
  Breaks a line by hyphenating before the character at the specified index.
- [func shouldBreakLine(byWordBeforeCharacterAt: Int) -> Bool](./nsatstypesetter/shouldbreakline%28bywordbeforecharacterat%29.md)
  Breaks a line by word-wrapping before the character at the specified index.
- [func willSetLineFragmentRect(UnsafeMutablePointer<NSRect>, forGlyphRange: NSRange, usedRect: UnsafeMutablePointer<NSRect>, baselineOffset: UnsafeMutablePointer<CGFloat>)](./nsatstypesetter/willsetlinefragmentrect%28_,forglyphrange,usedrect,baselineoffset%29.md)
  Notifies subclasses that the typesetter is about to set a new line fragment.
- [func setHardInvalidation(Bool, forGlyphRange: NSRange)](./nsatstypesetter/sethardinvalidation%28_,forglyphrange%29.md)
  Sets a Boolean value that determines whether the layout manager invalidates the specified portion of the glyph cache.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>!, characterIndexes: UnsafeMutablePointer<Int>!, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>!, elasticBits: UnsafeMutablePointer<ObjCBool>!) -> Int](./nsatstypesetter/getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits%29.md)
  Extracts the information needed to lay out the glyphs in the given glyph buffer from the given glyph range.

## Relationships

### Inherits From
- [NSTypesetter](./nstypesetter.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### TextKit 1
- [class NSTextStorage](./nstextstorage.md)
  The fundamental storage mechanism of TextKit that contains the text managed by the system.
- [class NSLayoutManager](./nslayoutmanager.md)
  An object that coordinates the layout and display of text characters.
- [class NSTypesetter](./nstypesetter.md)
  An abstract class that performs various type layout tasks.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsatstypesetter)*