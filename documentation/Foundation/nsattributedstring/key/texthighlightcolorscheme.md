# textHighlightColorScheme

**Framework**: Foundation  
**Kind**: property

The custom highlight color to apply to the text.

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
static let textHighlightColorScheme: NSAttributedString.Key
```

#### Discussion

The value of this attribute is an [`NSAttributedString.TextHighlightColorScheme`](nsattributedstring/texthighlightcolorscheme.md) structure. The default value of this attribute is `nil`, which applies the default system highlight color to the text when the [`textHighlightStyle`](nsattributedstring/key/texthighlightstyle.md) attribute is present.

A highlight adds a background color behind the text, and applies a contrasting foreground color to the text itself. Set the value of this attribute to [`default`](nsattributedstring/texthighlightcolorscheme/default.md), or don’t specify the attribute at all, to apply a highlight with the default system color. Specify a different value for this attribute to apply that highlight color instead.

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
- [static let textHighlightStyle: NSAttributedString.Key](nsattributedstring/key/texthighlightstyle.md)
  An attribute that adds a highlight color to the text to emphasize it.
- [static let textItemTag: NSAttributedString.Key](nsattributedstring/key/textitemtag.md)
  The name of a custom tag associated with a text item.
- [static let toolTip: NSAttributedString.Key](nsattributedstring/key/tooltip.md)
  The tooltip text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/texthighlightcolorscheme)*