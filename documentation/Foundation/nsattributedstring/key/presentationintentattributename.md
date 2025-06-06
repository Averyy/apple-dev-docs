# presentationIntentAttributeName

**Framework**: Foundation  
**Kind**: property

An attribute that provides details for a block-level Markdown element.

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
static let presentationIntentAttributeName: NSAttributedString.Key
```

#### Discussion

The value of this key is an [`NSPresentationIntent`](nspresentationintent.md) object. Block-level elements include paragraphs, headers, lists, tables, and other structural elements of the Markdown content.

The system provides default visual treatments for ranges of text with this attribute. To replace the default visual treatment, remove this attribute and replace it with the formatting options you want.

## See Also

- [static let inlinePresentationIntent: NSAttributedString.Key](nsattributedstring/key/inlinepresentationintent.md)
  An attribute that provides details for an inline Markdown element.
- [static let markdownSourcePosition: NSAttributedString.Key](nsattributedstring/key/markdownsourceposition.md)
  The position in a Markdown source string corresponding to some attributed text.
- [static let alternateDescription: NSAttributedString.Key](nsattributedstring/key/alternatedescription.md)
  An alternate description for a URL or image.
- [static let imageURL: NSAttributedString.Key](nsattributedstring/key/imageurl.md)
  The URL for an image in Markdown text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/presentationintentattributename)*