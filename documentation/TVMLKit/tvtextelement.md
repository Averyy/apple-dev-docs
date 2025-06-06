# TVTextElement

**Framework**: TVMLKit  
**Kind**: class

The textual content for the DOM element.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class TVTextElement
```

## Topics

### Creating Attributed Strings
- [func makeAttributedString(font: UIFont) -> NSAttributedString](tvtextelement/makeattributedstring(font:).md)
  Provides an attributed string for a given font.
- [func makeAttributedString(font: UIFont, foregroundColor: UIColor?, textAlignment: NSTextAlignment) -> NSAttributedString](tvtextelement/makeattributedstring(font:foregroundcolor:textalignment:).md)
  Convenience method for configuring an attributed string given the specified attributes.
### Inspecting Text Elements
- [var attributedString: NSAttributedString?](tvtextelement/attributedstring.md)
  The text for an element.
- [var textStyle: TVTextElementStyle](tvtextelement/textstyle.md)
  The style applied to the text of the element.
- [enum TVTextElementStyle](tvtextelementstyle.md)
  The style applied to the text inside of an element.

## Relationships

### Inherits From
- [TVViewElement](tvviewelement.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TVElementFactory](tvelementfactory.md)
  An object used to register new elements to extend the Apple TV Markup Language (TVML).
- [class TVImageElement](tvimageelement.md)
  A representation of a read-only DOM node containing the attributes that describe an image element.
- [Creating TVML Elements](creating-tvml-elements.md)
  Avoid rewriting complex and often used elements by creating a simplified custom element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvtextelement)*