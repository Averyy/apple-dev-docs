# TVImageElement

**Framework**: TVMLKit  
**Kind**: class

A representation of a read-only DOM node containing the attributes that describe an image element.

**Availability**:
- tvOS 9.0+

## Declaration

```swift
class TVImageElement
```

## Topics

### Identifying an Image
- [var url: URL?](tvimageelement/url.md)
  A URL that points to the location of the image.
- [var imageType: TVImageType](tvimageelement/imagetype.md)
  The type of image.
- [enum TVImageType](tvimagetype.md)
  The type of image.
- [var srcset: [String : URL]?](tvimageelement/srcset.md)
  A dictionary specifying versions of the same image for different resolutions.

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
- [class TVTextElement](tvtextelement.md)
  The textual content for the DOM element.
- [Creating TVML Elements](creating-tvml-elements.md)
  Avoid rewriting complex and often used elements by creating a simplified custom element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvmlkit/tvimageelement)*