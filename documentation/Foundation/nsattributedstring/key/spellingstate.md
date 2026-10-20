# spellingState

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The spelling state of the text.

**Availability**:
- macOS 10.0+

## Declaration

```swift
static let spellingState: NSAttributedString.Key
```

#### Discussion

The value of this attribute is an integer. The default value of this key is 0, which indicates that there are no grammar or spelling errors. Specify a different value to indicate that a spelling or grammar error exists.

This key is available in macOS 10.2 and later, but its interpretation changed in OS X v10.5. Previously, any non-zero value caused the spelling indicator to be displayed. For macOS 10.5 and later, the (integer) value is treated as being composed of the spelling and grammar flags. See `NSSpellingStateAttributeName Flags` for possible values.

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
- [static let suggestionHighlight: NSAttributedString.Key](./suggestionhighlight.md)
  A highlight associated with a Spotlight suggestion.
- [static let textAlternatives: NSAttributedString.Key](./textalternatives.md)
  The alternatives for the text.
- [static let textEffect: NSAttributedString.Key](./texteffect.md)
  An attribute that applies a text effect to the text.
- [static let textHighlightColorScheme: NSAttributedString.Key](./texthighlightcolorscheme.md)
  The custom highlight color to apply to the text.
- [static let textHighlightStyle: NSAttributedString.Key](./texthighlightstyle.md)
  An attribute that adds a highlight color to the text to emphasize it.
- [static let textItemTag: NSAttributedString.Key](./textitemtag.md)
  The name of a custom tag associated with a text item.
- [static let toolTip: NSAttributedString.Key](./tooltip.md)
  The tooltip text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/spellingstate)*