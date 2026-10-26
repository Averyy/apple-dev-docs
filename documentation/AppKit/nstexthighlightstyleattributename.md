# NSTextHighlightStyleAttributeName

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

An attribute that adds a highlight color to the text to emphasize it.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern NSAttributedStringKey const NSTextHighlightStyleAttributeName;
```

#### Discussion

The value of this attribute is an [`NSTextHighlightStyle`](./nstexthighlightstyle.md) structure. The default value of this attribute is `nil`, which does not add a highlight to the text.

A highlight adds a background color behind the text, and adjusts the color of the text itself to contrast appropriately. The [`NSTextHighlightStyleDefault`](./nstexthighlightstyledefault.md) highlight style applies the system highlight color to your text. To apply a different color, add the [`NSTextHighlightColorSchemeAttributeName`](./nstexthighlightcolorschemeattributename.md) attribute to your text in addition to this one. Use the [`NSTextHighlightColorSchemeAttributeName`](./nstexthighlightcolorschemeattributename.md) key to specify which highlight color you want.

## See Also

### Getting text attribute keys
- [NSCursorAttributeName](./nscursorattributename.md)
  The cursor object.
- [NSLinkAttributeName](./nslinkattributename.md)
  The link for the text.
- [NSMarkedClauseSegmentAttributeName](./nsmarkedclausesegmentattributename.md)
  The index of the marked clause segment.
- [NSShadowAttributeName](./nsshadowattributename.md)
  The shadow of the text.
- [NSSpellingStateAttributeName](./nsspellingstateattributename.md)
  The spelling state of the text.
- [NSTextAlternativesAttributeName](./nstextalternativesattributename.md)
  The alternatives for the text.
- [NSTextEffectAttributeName](./nstexteffectattributename.md)
  An attribute that applies a text effect to the text.
- [NSTextHighlightColorSchemeAttributeName](./nstexthighlightcolorschemeattributename.md)
  The custom highlight color to apply to the text.
- [NSToolTipAttributeName](./nstooltipattributename.md)
  The tooltip text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexthighlightstyleattributename)*