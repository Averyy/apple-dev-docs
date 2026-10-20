# containerBreakAction

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Causes container break.

**Availability**:
- macOS

## Declaration

```swift
static var containerBreakAction: NSTypesetterControlCharacterAction { get }
```

```c
NSTypesetterContainerBreakAction
```

## See Also

### Constants
- [static var zeroAdvancementAction: NSTypesetterControlCharacterAction](./zeroadvancementaction.md)
  Glyphs with this action are filtered out from layout `(notShownAttribute == YES)`.
- [static var whitespaceAction: NSTypesetterControlCharacterAction](./whitespaceaction.md)
  The width for glyphs with this action are determined by [`boundingBox(forControlGlyphAt:for:proposedLineFragment:glyphPosition:characterIndex:)`](../nstypesetter/boundingbox%28forcontrolglyphat,for,proposedlinefragment,glyphposition,characterindex%29.md), if the method is implemented; otherwise, same as `NSTypesetterZeroAdvancementAction`.
- [static var horizontalTabAction: NSTypesetterControlCharacterAction](./horizontaltabaction.md)
  Treated as tab character.
- [static var lineBreakAction: NSTypesetterControlCharacterAction](./linebreakaction.md)
  Causes line break.
- [static var paragraphBreakAction: NSTypesetterControlCharacterAction](./paragraphbreakaction.md)
  Causes paragraph break; the value returned by [`firstLineHeadIndent`](../nsparagraphstyle/firstlineheadindent.md) is the advancement used for the following glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesettercontrolcharacteraction/containerbreakaction)*