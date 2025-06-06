# NSTextListElement

**Framework**: AppKit  
**Kind**: class

A class that represents a text list node.

**Availability**:
- macOS 13.0+

## Declaration

```swift
class NSTextListElement
```

## Topics

### Create a text list element
- [convenience init?(children: [NSTextListElement], textList: NSTextList, nestingLevel: Int)](nstextlistelement/init(children:textlist:nestinglevel:).md)
  Creates a text list element with the list elements and nesting level you provide.
- [convenience init(contents: NSAttributedString, markerAttributes: [NSAttributedString.Key : Any]?, textList: NSTextList, children: [NSTextListElement]?)](nstextlistelement/init(contents:markerattributes:textlist:children:).md)
  Creates a text list element with the list elements, nesting level, and marker attributes you provide.
- [init(parent: NSTextListElement?, textList: NSTextList, contents: NSAttributedString?, markerAttributes: [NSAttributedString.Key : Any]?, children: [NSTextListElement]?)](nstextlistelement/init(parent:textlist:contents:markerattributes:children:).md)
  Creates a text list element with the parent, list elements, nesting level, and marker attributes you provide.
### Accessing the text elements
- [var textList: NSTextList](nstextlistelement/textlist.md)
  The value that represents the text list.
- [var parent: NSTextListElement?](nstextlistelement/parent.md)
  A text list element that refers to the enclosing text list element.
- [var childElements: [NSTextListElement]](nstextlistelement/childelements.md)
  An array that contains child text elements.
### Accessing the text list’s attributes
- [var markerAttributes: [NSAttributedString.Key : Any]?](nstextlistelement/markerattributes.md)
  A dictionary of attributed string keys and IDs that represent the list’s marker attributes.
### Accessing the formatted string data
- [var attributedString: NSAttributedString](nstextlistelement/attributedstring.md)
  An attributed string that represents the string the framework displays for this element taking into account markers and the indentation level of the list element.
- [var contents: NSAttributedString?](nstextlistelement/contents.md)
  The text list element contents without markers and formatting.

## Relationships

### Inherits From
- [NSTextParagraph](nstextparagraph.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Enriching your text in text views](../UIKit/enriching-your-text-in-text-views.md)
  Add exclusion paths, text attachments, and text lists to your text, and render it with text views.
- [class NSTextParagraph](nstextparagraph.md)
  A class that represents a single paragraph backed by an attributed string as the contents.
- [class NSTextElement](nstextelement.md)
  An abstract base class that represents the smallest units of text layout such as paragraphs or attachments.
- [protocol NSTextElementProvider](nstextelementprovider.md)
  A protocol the text content manager and its concrete subclasses conform to, which defines the interface for interacting with custom content types of a text document.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextlistelement)*