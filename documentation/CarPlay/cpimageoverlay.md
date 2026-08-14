# CPImageOverlay

**Framework**: CarPlay  
**Kind**: class

An overlay that displays information over an image.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
@MainActor
class CPImageOverlay
```

## Topics

### Initializers
- [init?(coder: NSCoder)](cpimageoverlay/init(coder:).md)
- [init(image: UIImage, alignment: CPImageOverlay.Alignment)](cpimageoverlay/init(image:alignment:).md)
  Initialize an overlay with a UIImage.
- [init(text: String, textColor: UIColor, backgroundColor: UIColor, alignment: CPImageOverlay.Alignment)](cpimageoverlay/init(text:textcolor:backgroundcolor:alignment:).md)
  Initialize an overlay with properties that control the overlay’s appearance and text contents.
### Instance Properties
- [var alignment: CPImageOverlay.Alignment](cpimageoverlay/alignment-swift.property.md)
  The alignment for positioning the overlay.
- [var backgroundColor: UIColor?](cpimageoverlay/backgroundcolor.md)
  The background color of the overlay.
- [var image: UIImage?](cpimageoverlay/image.md)
  An optional image to display in the overlay.
- [var text: String?](cpimageoverlay/text.md)
  The text displayed in the overlay.
- [var textColor: UIColor?](cpimageoverlay/textcolor.md)
  The color of the overlay text.
### Enumerations
- [CPImageOverlay.Alignment](cpimageoverlay/alignment-swift.enum.md)
  Alignment options for positioning.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/carplay/cpimageoverlay)*