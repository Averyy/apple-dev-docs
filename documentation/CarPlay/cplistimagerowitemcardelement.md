# CPListImageRowItemCardElement

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)

## Declaration

```swift
@MainActor
class CPListImageRowItemCardElement
```

## Topics

### Initializers
- [init(image: UIImage, showImageFullHeight: Bool, title: String?, subtitle: String?, tintColor: UIColor?)](cplistimagerowitemcardelement/init(image:showimagefullheight:title:subtitle:tintcolor:).md)
  Initialize an element that is constituted of an image, boolean to entierely cover the element with the image, title, subtitle and a tint color.
### Instance Properties
- [var showImageFullHeight: Bool](cplistimagerowitemcardelement/showimagefullheight.md)
  A Boolean value indicating whether the element should be fill with the image.
- [var subtitle: String?](cplistimagerowitemcardelement/subtitle.md)
  The subtitle associated with this element.
- [var tintColor: UIColor?](cplistimagerowitemcardelement/tintcolor.md)
  A UIColor used to tint the element. When @c showImageFullHeight is true, the tint color is applied behind the labels at the bottom of the card. Otherwise, this color is part of the gradient color at the bottom of the card.
- [var title: String?](cplistimagerowitemcardelement/title.md)
  The title associated with this element.
### Type Properties
- [class var maximumFullHeightImageSize: CGSize](cplistimagerowitemcardelement/maximumfullheightimagesize.md)
  The expected image size for the image in your @c CPListImageRowItemCardElement when @c showImageFullHeight is  true. Images provided will be resized to this size.
- [class var maximumImageSize: CGSize](cplistimagerowitemcardelement/maximumimagesize.md)
  The expected image size for the image in your @c CPListImageRowItemCardElement when @c showImageFullHeight is false. Images provided will be resized to this size.

## Relationships

### Inherits From
- [CPListImageRowItemElement](cplistimagerowitemelement.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement)*