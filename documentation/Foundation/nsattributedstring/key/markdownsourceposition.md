# markdownSourcePosition

**Framework**: Foundation  
**Kind**: property

The position in a Markdown source string corresponding to some attributed text.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
static let markdownSourcePosition: NSAttributedString.Key
```

#### Discussion

This attribute indicates the position in the Markdown source where a run of attributed text begins and ends, omitting markup characters in the source. For example, after parsing the source string `“This is *emphasized*.”`, the text `emphasized` has a Markdown source position that starts at column `10`. This index is the `“e”` character, not the `“*”` formatting character.

An attributed string parsed from Markdown text includes this attribute only if the [`appliesSourcePositionAttributes`](nsattributedstringmarkdownparsingoptions/appliessourcepositionattributes.md) value in the directory of [`NSAttributedString.DocumentReadingOptionKey`](nsattributedstring/documentreadingoptionkey.md) options provided to the [`NSAttributedString`](nsattributedstring.md) initializer is `YES`.

## See Also

- [static let inlinePresentationIntent: NSAttributedString.Key](nsattributedstring/key/inlinepresentationintent.md)
  An attribute that provides details for an inline Markdown element.
- [static let presentationIntentAttributeName: NSAttributedString.Key](nsattributedstring/key/presentationintentattributename.md)
  An attribute that provides details for a block-level Markdown element.
- [static let alternateDescription: NSAttributedString.Key](nsattributedstring/key/alternatedescription.md)
  An alternate description for a URL or image.
- [static let imageURL: NSAttributedString.Key](nsattributedstring/key/imageurl.md)
  The URL for an image in Markdown text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/markdownsourceposition)*