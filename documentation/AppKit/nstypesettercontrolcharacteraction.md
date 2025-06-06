# NSTypesetterControlCharacterAction

**Framework**: AppKit  
**Kind**: struct

The following constants are possible values returned by the [`actionForControlCharacter(at:)`](nstypesetter/actionforcontrolcharacter(at:).md) method to determine the action associated with a control character.

**Availability**:
- macOS ?+

## Declaration

```swift
struct NSTypesetterControlCharacterAction
```

## Topics

### Constants
- [static var zeroAdvancementAction: NSTypesetterControlCharacterAction](nstypesettercontrolcharacteraction/zeroadvancementaction.md)
  Glyphs with this action are filtered out from layout `(notShownAttribute == YES)`.
- [static var whitespaceAction: NSTypesetterControlCharacterAction](nstypesettercontrolcharacteraction/whitespaceaction.md)
  The width for glyphs with this action are determined by [`boundingBox(forControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)`](nstypesetter/boundingbox(forcontrolglyphat:for:proposedlinefragment:glyphposition:characterindex:).md), if the method is implemented; otherwise, same as `NSTypesetterZeroAdvancementAction`.
- [static var horizontalTabAction: NSTypesetterControlCharacterAction](nstypesettercontrolcharacteraction/horizontaltabaction.md)
  Treated as tab character.
- [static var lineBreakAction: NSTypesetterControlCharacterAction](nstypesettercontrolcharacteraction/linebreakaction.md)
  Causes line break.
- [static var paragraphBreakAction: NSTypesetterControlCharacterAction](nstypesettercontrolcharacteraction/paragraphbreakaction.md)
  Causes paragraph break; the value returned by [`firstLineHeadIndent`](nsparagraphstyle/firstlineheadindent.md) is the advancement used for the following glyph.
- [static var containerBreakAction: NSTypesetterControlCharacterAction](nstypesettercontrolcharacteraction/containerbreakaction.md)
  Causes container break.
### Initializers
- [init(rawValue: UInt)](nstypesettercontrolcharacteraction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesettercontrolcharacteraction)*