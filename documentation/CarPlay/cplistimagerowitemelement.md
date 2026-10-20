# CPListImageRowItemElement

**Framework**: CarPlay  
**Kind**: class  
**Role**: Class

Abstract superclass for a a row item element object.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class CPListImageRowItemElement
```

```objc
@interface CPListImageRowItemElement : NSObject
```

## Topics

### Instance Properties
- [var accessibilityLabel: String?](./cplistimagerowitemelement/accessibilitylabel.md)
- [var image: UIImage](./cplistimagerowitemelement/image.md)
  The image associated with this element.
- [var isEnabled: Bool](./cplistimagerowitemelement/isenabled.md)
  A Boolean value indicating whether the list element is enabled.
### Type Properties
- [class var maximumImageSize: CGSize](./cplistimagerowitemelement/maximumimagesize.md)
  The expected image size for the image in your @c CPListImageRowItemElement. Images provided will be resized to this size.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [CPListImageRowItemCardElement](./cplistimagerowitemcardelement.md)
- [CPListImageRowItemCondensedElement](./cplistimagerowitemcondensedelement.md)
- [CPListImageRowItemGridElement](./cplistimagerowitemgridelement.md)
- [CPListImageRowItemImageGridElement](./cplistimagerowitemimagegridelement.md)
- [CPListImageRowItemRowElement](./cplistimagerowitemrowelement.md)
### Conforms To
- [CPPlayableItem](./cpplayableitem.md)
- [CVarArg](../Swift/cvararg.md)
- [Copyable](../Swift/copyable.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemelement)*