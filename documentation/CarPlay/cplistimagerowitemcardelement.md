# CPListImageRowItemCardElement

**Framework**: CarPlay  
**Kind**: class

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
@MainActor
class CPListImageRowItemCardElement
```

## Topics

### Initializers
- [init?(coder: NSCoder)](cplistimagerowitemcardelement/init(coder:).md)
- [init(image: UIImage, showsImageFullHeight: Bool, title: String?, subtitle: String?, tintColor: UIColor?)](cplistimagerowitemcardelement/init(image:showsimagefullheight:title:subtitle:tintcolor:).md)
  Initialize a card element with an image.
- [init(thumbnail: CPThumbnailImage, title: String?, subtitle: String?, tintColor: UIColor?)](cplistimagerowitemcardelement/init(thumbnail:title:subtitle:tintcolor:).md)
  Initialize an element with a thumbnail, title, subtitle, and tint color.
### Instance Properties
- [var showsImageFullHeight: Bool](cplistimagerowitemcardelement/showsimagefullheight.md)
  A Boolean value indicating whether the element should be fill with the image.
- [var subtitle: String?](cplistimagerowitemcardelement/subtitle.md)
  The subtitle associated with this element.
- [var thumbnail: CPThumbnailImage?](cplistimagerowitemcardelement/thumbnail.md)
  The thumbnail associated with this element.
- [var tintColor: UIColor?](cplistimagerowitemcardelement/tintcolor.md)
  A UIColor used to tint the element. When @c showsImageFullHeight is true, the tint color is applied behind the labels at the bottom of the card. Otherwise, this color is part of the gradient color at the bottom of the card.
- [var title: String](cplistimagerowitemcardelement/title.md)
  The title associated with this element.
### Type Properties
- [class var maximumFullHeightImageSize: CGSize](cplistimagerowitemcardelement/maximumfullheightimagesize.md)
  The expected image size for the image in your @c CPListImageRowItemCardElement when @c showsImageFullHeight is  true. Images provided will be resized to this size.
- [class var maximumImageSize: CGSize](cplistimagerowitemcardelement/maximumimagesize.md)
  The expected image size for the image in your @c CPListImageRowItemCardElement when @c showsImageFullHeight is false. Images provided will be resized to this size.

## Relationships

### Inherits From
- [CPListImageRowItemElement](cplistimagerowitemelement.md)
### Conforms To
- [CPPlayableItem](cpplayableitem.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cplistimagerowitemcardelement)*