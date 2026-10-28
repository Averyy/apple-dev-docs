# textHighlightColorScheme

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

## Discussion

The value of this attribute is an [`NSAttributedString.TextHighlightColorScheme`](../texthighlightcolorscheme.md) structure. The default value of this attribute is `nil`, which applies the default system highlight color to the text when the [`textHighlightStyle`](./texthighlightstyle.md) attribute is present.

A highlight adds a background color behind the text, and applies a contrasting foreground color to the text itself. Set the value of this attribute to [`default`](../texthighlightcolorscheme/default.md), or don’t specify the attribute at all, to apply a highlight with the default system color. Specify a different value for this attribute to apply that highlight color instead.

## See Also

### Getting text attribute keys
- [static let cursor: NSAttributedString.Key](./cursor.md)
  The cursor object.
- [static let link: NSAttributedString.Key](./link.md)
  The link for the text.
- [static let markedClauseSegment: NSAttributedString.Key](./markedclausesegment.md)
  The index of the marked clause segment.
- [static let replacementIndex: NSAttributedString.Key](./replacementindex.md)
  The replacement position associated with a format string specifier.
- [static let shadow: NSAttributedString.Key](./shadow.md)
  The shadow of the text.
- [static let spellingState: NSAttributedString.Key](./spellingstate.md)
  The spelling state of the text.
- [static let suggestionHighlight: NSAttributedString.Key](./suggestionhighlight.md)
  A highlight associated with a Spotlight suggestion.
- [static let textAlternatives: NSAttributedString.Key](./textalternatives.md)
  The alternatives for the text.
- [static let textEffect: NSAttributedString.Key](./texteffect.md)
  An attribute that applies a text effect to the text.
- [static let textHighlightStyle: NSAttributedString.Key](./texthighlightstyle.md)
  An attribute that adds a highlight color to the text to emphasize it.
- [static let textItemTag: NSAttributedString.Key](./textitemtag.md)
  The name of a custom tag associated with a text item.
- [static let toolTip: NSAttributedString.Key](./tooltip.md)
  The tooltip text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/texthighlightcolorscheme)*