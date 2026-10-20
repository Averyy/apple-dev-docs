# textHighlightStyle

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

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

The value of this attribute is an [`NSAttributedString.TextHighlightStyle`](../texthighlightstyle.md) structure. The default value of this attribute is `nil`, which does not add a highlight to the text.

A highlight adds a background color behind the text, and adjusts the color of the text itself to contrast appropriately. The [`default`](../texthighlightstyle/default.md) highlight style applies the system highlight color to your text. To apply a different color, add the [`textHighlightColorScheme`](./texthighlightcolorscheme.md) attribute to your text in addition to this one. Use the [`textHighlightColorScheme`](./texthighlightcolorscheme.md) key to specify which highlight color you want.

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
- [static let textHighlightColorScheme: NSAttributedString.Key](./texthighlightcolorscheme.md)
  The custom highlight color to apply to the text.
- [static let textItemTag: NSAttributedString.Key](./textitemtag.md)
  The name of a custom tag associated with a text item.
- [static let toolTip: NSAttributedString.Key](./tooltip.md)
  The tooltip text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/texthighlightstyle)*