# NSTextParagraph

**Framework**: UIKit  
**Kind**: class

A class that represents a single paragraph backed by an attributed string as the contents.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class NSTextParagraph
```

## Topics

### Creating a paragraph
- [init(attributedString: NSAttributedString?)](nstextparagraph/init(attributedstring:).md)
  Creates a new paragraph with the attributed string you provide.
### Getting paragraph characteristics
- [var attributedString: NSAttributedString](nstextparagraph/attributedstring.md)
  Returns the source attributed string.
- [var paragraphContentRange: NSTextRange?](nstextparagraph/paragraphcontentrange.md)
  Returns the range of the paragraph in the containing text’s attributed string.
- [var paragraphSeparatorRange: NSTextRange?](nstextparagraph/paragraphseparatorrange.md)
  Returns the range of the paragraph separator in the containing text’s attributed string.

## Relationships

### Inherits From
- [NSTextElement](nstextelement.md)
### Inherited By
- [NSTextListElement](nstextlistelement.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Enriching your text in text views](enriching-your-text-in-text-views.md)
  Add exclusion paths, text attachments, and text lists to your text, and render it with text views.
- [class NSTextListElement](nstextlistelement.md)
  A class that represents a text list node.
- [class NSTextElement](nstextelement.md)
  An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.
- [protocol NSTextElementProvider](nstextelementprovider.md)
  A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextparagraph)*