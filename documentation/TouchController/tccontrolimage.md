# TCControlImage

**Framework**: Touch Controller  
**Kind**: class

Represents an image to be rendered using Metal.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
class TCControlImage
```

## Topics

### Creating a control image
- [convenience init?(cgImage: CGImage, size: CGSize, device: any MTLDevice)](tccontrolimage/init(cgimage:size:device:).md)
  Creates a new image from a CGImage.
- [convenience init(texture: any MTLTexture, size: CGSize)](tccontrolimage/init(texture:size:).md)
  Creates a new image with the specified texture and size.
- [init(texture: any MTLTexture, size: CGSize, highlight: (any MTLTexture)?, offset: CGPoint, tintColor: CGColor)](tccontrolimage/init(texture:size:highlight:offset:tintcolor:).md)
  Creates a new image with the specified texture, size, highlight texture, offset, and color tint.
- [convenience init?(uiImage: UIImage, size: CGSize, device: any MTLDevice)](tccontrolimage/init(uiimage:size:device:).md)
  Creates a new image from a UIImage.
### Inspecting the control image
- [var highlightTexture: (any MTLTexture)?](tccontrolimage/highlighttexture.md)
  The Metal texture to use for the image when highlighted. May be `nil`.
- [var offset: CGPoint](tccontrolimage/offset.md)
  The offset from the center of the parent control in points.
- [var size: CGSize](tccontrolimage/size.md)
  The size of the image in points.
- [var texture: any MTLTexture](tccontrolimage/texture.md)
  The Metal texture to use for the image.
- [var tintColor: CGColor](tccontrolimage/tintcolor.md)
  The color tint to apply to the texture. The color ref is retained.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class TCControlContents](tccontrolcontents.md)
  Represents the visual contents of a touch control.
- [protocol TCControlLayout](tccontrollayout.md)
  A protocol defining the controlLayout properties for a control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/touchcontroller/tccontrolimage)*