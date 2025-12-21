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
- [var image: UIImage](cplistimagerowitemelement/image.md)
  The image associated with this element.
- [var isEnabled: Bool](cplistimagerowitemelement/isenabled.md)
  A Boolean value indicating whether the list element is enabled.
### Type Properties
- [class var maximumImageSize: CGSize](cplistimagerowitemelement/maximumimagesize.md)
  The expected image size for the image in your @c CPListImageRowItemElement. Images provided will be resized to this size.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [CPListImageRowItemCardElement](cplistimagerowitemcardelement.md)
- [CPListImageRowItemCondensedElement](cplistimagerowitemcondensedelement.md)
- [CPListImageRowItemGridElement](cplistimagerowitemgridelement.md)
- [CPListImageRowItemImageGridElement](cplistimagerowitemimagegridelement.md)
- [CPListImageRowItemRowElement](cplistimagerowitemrowelement.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemelement)*