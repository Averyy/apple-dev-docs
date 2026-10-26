# NSTextHighlightColorSchemeAttributeName

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The custom highlight color to apply to the text.

**Availability**:
- macOS 15.0+

## Declaration

```c
extern NSAttributedStringKey const NSTextHighlightColorSchemeAttributeName;
```

#### Discussion

The value of this attribute is an [`NSTextHighlightColorScheme`](./nstexthighlightcolorscheme.md) structure. The default value of this attribute is `nil`, which applies the default system highlight color to the text when the [`NSTextHighlightStyleAttributeName`](./nstexthighlightstyleattributename.md) attribute is present.

A highlight adds a background color behind the text, and applies a contrasting foreground color to the text itself. Set the value of this attribute to [`NSTextHighlightColorSchemeDefault`](./nstexthighlightcolorschemedefault.md), or don’t specify the attribute at all, to apply a highlight with the default system color. Specify a different value for this attribute to apply that highlight color instead.

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
- [NSTextHighlightStyleAttributeName](./nstexthighlightstyleattributename.md)
  An attribute that adds a highlight color to the text to emphasize it.
- [NSToolTipAttributeName](./nstooltipattributename.md)
  The tooltip text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstexthighlightcolorschemeattributename)*