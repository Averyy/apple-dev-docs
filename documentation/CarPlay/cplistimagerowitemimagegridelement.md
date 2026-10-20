# CPListImageRowItemImageGridElement

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class CPListImageRowItemImageGridElement
```

```objc
@interface CPListImageRowItemImageGridElement : CPListImageRowItemElement
```

## Topics

### Initializers
- [init(image: UIImage, imageShape: CPListImageRowItemImageGridElement.Shape, title: String, accessorySymbolName: String?)](./cplistimagerowitemimagegridelement/init%28image,imageshape,title,accessorysymbolname%29.md)
  Initialize an element that is constituted of an image and an image shape.
### Instance Properties
- [var accessorySymbolName: String?](./cplistimagerowitemimagegridelement/accessorysymbolname.md)
  The name of the system symbol image to use as accessory.
- [var imageShape: CPListImageRowItemImageGridElement.Shape](./cplistimagerowitemimagegridelement/imageshape.md)
  Shape used to draw the image of the element.
- [var title: String](./cplistimagerowitemimagegridelement/title.md)
  The title associated with this element.
### Enumerations
- [CPListImageRowItemImageGridElement.Shape](./cplistimagerowitemimagegridelement/shape.md)
  Types of shape used to draw a list item.

## Relationships

### Inherits From
- [CPListImageRowItemElement](./cplistimagerowitemelement.md)
### Conforms To
- [CPPlayableItem](./cpplayableitem.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemimagegridelement)*