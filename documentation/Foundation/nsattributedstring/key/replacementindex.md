# replacementIndex

**Framework**: Foundation  
**Kind**: property

The replacement position associated with a format string specifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
static let replacementIndex: NSAttributedString.Key
```

#### Discussion

When creating an attributed string from a format string and one or more replacement values, this attribute indicates the ordinal index of each replacement. You must specify the [`NSAttributedStringFormattingApplyReplacementIndexAttribute`](nsattributedstringformattingoptions/nsattributedstringformattingapplyreplacementindexattribute.md) option at creation time to add this attribute to the substituted text. The value of this key is an `NSNumber` with the replacement position of the substitute text.

## See Also

- [static let cursor: NSAttributedString.Key](nsattributedstring/key/cursor.md)
  The cursor object.
- [static let link: NSAttributedString.Key](nsattributedstring/key/link.md)
  The link for the text.
- [static let markedClauseSegment: NSAttributedString.Key](nsattributedstring/key/markedclausesegment.md)
  The index of the marked clause segment.
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
- [static let textHighlightStyle: NSAttributedString.Key](nsattributedstring/key/texthighlightstyle.md)
  An attribute that adds a highlight color to the text to emphasize it.
- [static let textItemTag: NSAttributedString.Key](nsattributedstring/key/textitemtag.md)
  The name of a custom tag associated with a text item.
- [static let toolTip: NSAttributedString.Key](nsattributedstring/key/tooltip.md)
  The tooltip text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/replacementindex)*