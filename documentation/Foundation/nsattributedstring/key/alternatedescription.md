# alternateDescription

**Framework**: Foundation  
**Kind**: property

An alternate description for a URL or image.

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
static let alternateDescription: NSAttributedString.Key
```

#### Discussion

The value of this key is an [`NSString`](nsstring.md) with the alternate description of the URL or image.

When a Markdown link contains a title string, the system adds this key to the link text and sets the value to the title. For example, in the Markdown tect `[Visit the Apple Store](https://store.apple.com “The Apple Store website”)`, the system sets the value of this key to `The Apple Store website`.

## See Also

- [static let inlinePresentationIntent: NSAttributedString.Key](nsattributedstring/key/inlinepresentationintent.md)
  An attribute that provides details for an inline Markdown element.
- [static let presentationIntentAttributeName: NSAttributedString.Key](nsattributedstring/key/presentationintentattributename.md)
  An attribute that provides details for a block-level Markdown element.
- [static let markdownSourcePosition: NSAttributedString.Key](nsattributedstring/key/markdownsourceposition.md)
  The position in a Markdown source string corresponding to some attributed text.
- [static let imageURL: NSAttributedString.Key](nsattributedstring/key/imageurl.md)
  The URL for an image in Markdown text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/alternatedescription)*