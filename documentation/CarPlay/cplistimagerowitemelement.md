# CPListImageRowItemElement

**Framework**: CarPlay  
**Kind**: class

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

## Topics

### Instance Properties
- [var accessibilityLabel: String?](cplistimagerowitemelement/accessibilitylabel.md)
- [var image: UIImage](cplistimagerowitemelement/image.md)
  The image associated with this element.
- [var isEnabled: Bool](cplistimagerowitemelement/isenabled.md)
  A Boolean value indicating whether the list element is enabled.
### Type Properties
- [class var maximumImageSize: CGSize](cplistimagerowitemelement/maximumimagesize.md)
  The expected image size for the image in your @c CPListImageRowItemElement. Images provided will be resized to this size.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Inherited By
- [CPListImageRowItemCardElement](cplistimagerowitemcardelement.md)
- [CPListImageRowItemCondensedElement](cplistimagerowitemcondensedelement.md)
- [CPListImageRowItemGridElement](cplistimagerowitemgridelement.md)
- [CPListImageRowItemImageGridElement](cplistimagerowitemimagegridelement.md)
- [CPListImageRowItemRowElement](cplistimagerowitemrowelement.md)
### Conforms To
- [CPPlayableItem](cpplayableitem.md)
- [CVarArg](../swift/cvararg.md)
- [Copyable](../swift/copyable.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemelement)*