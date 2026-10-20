# imageURL

**Framework**: Foundation  
**Kind**: property  
**Role**: Type Property

The URL for an image in Markdown text.

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
static let imageURL: NSAttributedString.Key
```

```c
extern NSAttributedStringKey const NSImageURLAttributeName;
```

#### Discussion

The value of this key is an [`NSURL`](../../nsurl.md) with the link to the image.

## See Also

### Getting Markdown attribute keys
- [static let inlinePresentationIntent: NSAttributedString.Key](./inlinepresentationintent.md)
  An attribute that provides details for an inline Markdown element.
- [static let presentationIntentAttributeName: NSAttributedString.Key](./presentationintentattributename.md)
  An attribute that provides details for a block-level Markdown element.
- [static let markdownSourcePosition: NSAttributedString.Key](./markdownsourceposition.md)
  The position in a Markdown source string corresponding to some attributed text.
- [static let alternateDescription: NSAttributedString.Key](./alternatedescription.md)
  An alternate description for a URL or image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsattributedstring/key/imageurl)*