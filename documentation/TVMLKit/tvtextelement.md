# TVTextElement

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

The textual content for the DOM element.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class TVTextElement
```

```objc
@interface TVTextElement : TVViewElement
```

## Topics

### Creating Attributed Strings
- [func makeAttributedString(font: UIFont) -> NSAttributedString](./tvtextelement/makeattributedstring%28font%29.md)
  Provides an attributed string for a given font.
- [func makeAttributedString(font: UIFont, foregroundColor: UIColor?, textAlignment: NSTextAlignment) -> NSAttributedString](./tvtextelement/makeattributedstring%28font,foregroundcolor,textalignment%29.md)
  Convenience method for configuring an attributed string given the specified attributes.
### Inspecting Text Elements
- [var attributedString: NSAttributedString?](./tvtextelement/attributedstring.md)
  The text for an element.
- [var textStyle: TVTextElementStyle](./tvtextelement/textstyle.md)
  The style applied to the text of the element.
- [enum TVTextElementStyle](./tvtextelementstyle.md)
  The style applied to the text inside of an element.

## Relationships

### Inherits From
- [TVViewElement](./tvviewelement.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Custom Elements
- [class TVElementFactory](./tvelementfactory.md)
  An object used to register new elements to extend the Apple TV Markup Language (TVML).
- [class TVImageElement](./tvimageelement.md)
  A representation of a read-only DOM node containing the attributes that describe an image element.
- [Creating TVML Elements](./creating-tvml-elements.md)
  Avoid rewriting complex and often used elements by creating a simplified custom element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvtextelement)*