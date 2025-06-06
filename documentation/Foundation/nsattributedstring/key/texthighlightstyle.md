# textHighlightStyle

**Framework**: Foundation  
**Kind**: property

An attribute that adds a highlight color to the text to emphasize it.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static let textHighlightStyle: NSAttributedString.Key
```

#### Discussion

The value of this attribute is an [`NSAttributedString.TextHighlightStyle`](nsattributedstring/texthighlightstyle.md) structure. The default value of this attribute is `nil`, which does not add a highlight to the text.

A highlight adds a background color behind the text, and adjusts the color of the text itself to contrast appropriately. The [`default`](nsattributedstring/texthighlightstyle/default.md) highlight style applies the system highlight color to your text. To apply a different color, add the [`textHighlightColorScheme`](nsattributedstring/key/texthighlightcolorscheme.md) attribute to your text in addition to this one. Use the [`textHighlightColorScheme`](nsattributedstring/key/texthighlightcolorscheme.md) key to specify which highlight color you want.

## See Also

- [static let cursor: NSAttributedString.Key](nsattributedstring/key/cursor.md)
  The cursor object.
- [static let link: NSAttributedString.Key](nsattributedstring/key/link.md)
  The link for the text.
- [static let markedClauseSegment: NSAttributedString.Key](nsattributedstring/key/markedclausesegment.md)
  The index of the marked clause segment.
- [static let replacementIndex: NSAttributedString.Key](nsattributedstring/key/replacementindex.md)
  The replacement position associated with a format string specifier.
- [static let shadow: NSAttributedString.Key](nsattributedstring/key/shadow.md)
  The shadow of the text.
- [static let spellingState: NSAttributedString.Key](nsattributedstring/key/spellingstate.md)
  The spelling state of the text.
- [static let suggestionHighlight: NSAttributedString.Key](nsattributedstring/key/suggestionhighlight.md)
  A highlight associated with a Spotlight suggestion.
- [static let textAlternatives: NSAttributedString.Key](nsattributedstring/key/textalternatives.md)
  The alternatives for the text.
- [static let textEffect: NSAttributedString.Key](nsattributedstring/key/texteffect.md)
  An attribute that applies a text effect to the text.
- [static let textHighlightColorScheme: NSAttributedString.Key](nsattributedstring/key/texthighlightcolorscheme.md)
  The custom highlight color to apply to the text.
- [static let textItemTag: NSAttributedString.Key](nsattributedstring/key/textitemtag.md)
  The name of a custom tag associated with a text item.
- [static let toolTip: NSAttributedString.Key](nsattributedstring/key/tooltip.md)
  The tooltip text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/texthighlightstyle)*