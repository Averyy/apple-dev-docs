# textEffect

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

An attribute that applies a text effect to the text.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
static let textEffect: NSAttributedString.Key
```

## Discussion

The value of this attribute is an [`NSString`](../../nsstring.md) object. Use this attribute to specify a text effect, such as [`letterpressStyle`](../texteffectstyle/letterpressstyle.md). The default value of this property is `nil`, indicating no text effect.

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
- [static let textHighlightColorScheme: NSAttributedString.Key](./texthighlightcolorscheme.md)
  The custom highlight color to apply to the text.
- [static let textHighlightStyle: NSAttributedString.Key](./texthighlightstyle.md)
  An attribute that adds a highlight color to the text to emphasize it.
- [static let textItemTag: NSAttributedString.Key](./textitemtag.md)
  The name of a custom tag associated with a text item.
- [static let toolTip: NSAttributedString.Key](./tooltip.md)
  The tooltip text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/texteffect)*