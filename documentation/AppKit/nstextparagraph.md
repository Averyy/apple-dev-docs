# NSTextParagraph

**Framework**: AppKit  
**Kind**: class  
**Role**: Class

A class that represents a single paragraph backed by an attributed string as the contents.

**Availability**:
- macOS 12.0+

## Declaration

```swift
class NSTextParagraph
```

```objc
@interface NSTextParagraph : NSTextElement
```

## Topics

### Creating a paragraph
- [init(attributedString: NSAttributedString?)](./nstextparagraph/init%28attributedstring%29.md)
  Creates a new paragraph with the attributed string you provide.
### Getting paragraph characteristics
- [var attributedString: NSAttributedString](./nstextparagraph/attributedstring.md)
  Returns the source attributed string.
- [var paragraphContentRange: NSTextRange?](./nstextparagraph/paragraphcontentrange.md)
  Returns the range of the paragraph in the containing text’s attributed string.
- [var paragraphSeparatorRange: NSTextRange?](./nstextparagraph/paragraphseparatorrange.md)
  Returns the range of the paragraph separator in the containing text’s attributed string.

## Relationships

### Inherits From
- [NSTextElement](./nstextelement.md)
### Inherited By
- [NSTextListElement](./nstextlistelement.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Content elements
- [Enriching your text in text views](../UIKit/enriching-your-text-in-text-views.md)
  Support line numbering, section collapsing, inline attachment caching, exclusion paths, text attachments, and text lists in a text view.
- [class NSTextListElement](./nstextlistelement.md)
  A class that represents a text list node.
- [class NSTextElement](./nstextelement.md)
  An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.
- [protocol NSTextElementProvider](./nstextelementprovider.md)
  A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextparagraph)*