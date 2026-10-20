# TVImageElement

**Framework**: TVMLKit  
**Kind**: class  
**Role**: Class

A representation of a read-only DOM node containing the attributes that describe an image element.

**Availability**:
- tvOS 9.0+ - Deprecated in 18.0

> **Deprecated**: Please use SwiftUI or UIKit

## Declaration

```swift
class TVImageElement
```

```objc
@interface TVImageElement : TVViewElement
```

## Topics

### Identifying an Image
- [var url: URL?](./tvimageelement/url.md)
  A URL that points to the location of the image.
- [var imageType: TVImageType](./tvimageelement/imagetype.md)
  The type of image.
- [enum TVImageType](./tvimagetype.md)
  The type of image.
- [var srcset: [String : URL]?](./tvimageelement/srcset.md)
  A dictionary specifying versions of the same image for different resolutions.

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
- [class TVTextElement](./tvtextelement.md)
  The textual content for the DOM element.
- [Creating TVML Elements](./creating-tvml-elements.md)
  Avoid rewriting complex and often used elements by creating a simplified custom element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvimageelement)*