# NSTypesetterControlCharacterAction

**Framework**: AppKit  
**Kind**: struct  
**Role**: Structure

The following constants are possible values returned by the [`actionForControlCharacter(at:)`](./nstypesetter/actionforcontrolcharacter%28at%29.md) method to determine the action associated with a control character.

**Availability**:
- macOS

## Declaration

```swift
struct NSTypesetterControlCharacterAction
```

```c
enum NSTypesetterControlCharacterAction : NSUInteger;
```

## Topics

### Constants
- [static var zeroAdvancementAction: NSTypesetterControlCharacterAction](./nstypesettercontrolcharacteraction/zeroadvancementaction.md)
  Glyphs with this action are filtered out from layout `(notShownAttribute == YES)`.
- [static var whitespaceAction: NSTypesetterControlCharacterAction](./nstypesettercontrolcharacteraction/whitespaceaction.md)
  The width for glyphs with this action are determined by [`boundingBox(forControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)`](./nstypesetter/boundingbox%28forcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md), if the method is implemented; otherwise, same as `NSTypesetterZeroAdvancementAction`.
- [static var horizontalTabAction: NSTypesetterControlCharacterAction](./nstypesettercontrolcharacteraction/horizontaltabaction.md)
  Treated as tab character.
- [static var lineBreakAction: NSTypesetterControlCharacterAction](./nstypesettercontrolcharacteraction/linebreakaction.md)
  Causes line break.
- [static var paragraphBreakAction: NSTypesetterControlCharacterAction](./nstypesettercontrolcharacteraction/paragraphbreakaction.md)
  Causes paragraph break; the value returned by [`firstLineHeadIndent`](./nsparagraphstyle/firstlineheadindent.md) is the advancement used for the following glyph.
- [static var containerBreakAction: NSTypesetterControlCharacterAction](./nstypesettercontrolcharacteraction/containerbreakaction.md)
  Causes container break.
### Initializers
- [init(rawValue: UInt)](./nstypesettercontrolcharacteraction/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesettercontrolcharacteraction)*