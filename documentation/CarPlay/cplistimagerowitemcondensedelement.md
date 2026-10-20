# CPListImageRowItemCondensedElement

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
class CPListImageRowItemCondensedElement
```

```objc
@interface CPListImageRowItemCondensedElement : CPListImageRowItemElement
```

## Topics

### Initializers
- [init(image: UIImage, imageShape: CPListImageRowItemCondensedElement.Shape, title: String, subtitle: String?, accessorySymbolName: String?)](./cplistimagerowitemcondensedelement/init%28image,imageshape,title,subtitle,accessorysymbolname%29.md)
  Initialize a list image row condensed element with an image, an image shape, a title, subtitle and a system symbol name.
### Instance Properties
- [var accessorySymbolName: String?](./cplistimagerowitemcondensedelement/accessorysymbolname.md)
  The name of the system symbol image to use as accessory.
- [var imageShape: CPListImageRowItemCondensedElement.Shape](./cplistimagerowitemcondensedelement/imageshape.md)
  Shape used to draw the image of the element.
- [var subtitle: String?](./cplistimagerowitemcondensedelement/subtitle.md)
  The subtitle associated with this element.
- [var title: String](./cplistimagerowitemcondensedelement/title.md)
  The title associated with this element.
### Enumerations
- [CPListImageRowItemCondensedElement.Shape](./cplistimagerowitemcondensedelement/shape.md)
  Types of shape used to draw a condensed row element.

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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcondensedelement)*