# containerBreakAction

**Framework**: AppKit  
**Kind**: property

Causes container break.

**Availability**:
- macOS ?+

## Declaration

```swift
static var containerBreakAction: NSTypesetterControlCharacterAction { get }
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesettercontrolcharacteraction/containerbreakaction)*