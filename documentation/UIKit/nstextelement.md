# NSTextElement

**Framework**: UIKit  
**Kind**: class

An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
class NSTextElement
```

## Topics

### Creating a text element
- [init(textContentManager: NSTextContentManager?)](nstextelement/init(textcontentmanager:).md)
  Creates a new text element with the content manager you provide.
### Accessing the content manager
- [var textContentManager: NSTextContentManager?](nstextelement/textcontentmanager.md)
  The value that represents the current content manager.
### Accessing the text element range
- [var elementRange: NSTextRange?](nstextelement/elementrange.md)
  A range value that represents the range of the element inside the document.
### Accessing text elements
- [var isRepresentedElement: Bool](nstextelement/isrepresentedelement.md)
  A Boolean value that indicates whether this element is in the text layout.
- [var parent: NSTextElement?](nstextelement/parent.md)
  A value that represents the parent element if this text element is a child of an enclosing element.
- [var childElements: [NSTextElement]](nstextelement/childelements.md)
  An array of zero or more child text elements.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [NSTextParagraph](nstextparagraph.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Enriching your text in text views](enriching-your-text-in-text-views.md)
  Add exclusion paths, text attachments, and text lists to your text, and render it with text views.
- [class NSTextParagraph](nstextparagraph.md)
  A class that represents a single paragraph backed by an attributed string as the contents.
- [class NSTextListElement](nstextlistelement.md)
  A class that represents a text list node.
- [protocol NSTextElementProvider](nstextelementprovider.md)
  A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextelement)*