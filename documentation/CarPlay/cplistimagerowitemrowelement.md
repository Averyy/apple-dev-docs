# CPListImageRowItemRowElement

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
class CPListImageRowItemRowElement
```

```objc
@interface CPListImageRowItemRowElement : CPListImageRowItemElement
```

## Topics

### Initializers
- [init(image: UIImage, title: String?, subtitle: String?)](./cplistimagerowitemrowelement/init%28image,title,subtitle%29.md)
  Initialize an element that is constituted of an image, title and subtitle. Only image is required while the two others can be omitted.
### Instance Properties
- [var subtitle: String?](./cplistimagerowitemrowelement/subtitle.md)
  The subtitle associated with this element.
- [var title: String?](./cplistimagerowitemrowelement/title.md)
  The title associated with this element.

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

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemrowelement)*