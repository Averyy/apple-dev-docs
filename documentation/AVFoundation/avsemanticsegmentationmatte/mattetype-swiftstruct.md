# AVSemanticSegmentationMatte.MatteType

**Framework**: AVFoundation  
**Kind**: struct

A structure that defines the types of segmentation matte images that you can capture along with the primary image.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct MatteType
```

## Topics

### Matte Types
- [static let hair: AVSemanticSegmentationMatte.MatteType](avsemanticsegmentationmatte/mattetype-swift.struct/hair.md)
  A matting image that segments the hair from all people in the visible field of view of an image.
- [static let skin: AVSemanticSegmentationMatte.MatteType](avsemanticsegmentationmatte/mattetype-swift.struct/skin.md)
  A matting image that segments the skin from all people in the visible field of view of an image.
- [static let teeth: AVSemanticSegmentationMatte.MatteType](avsemanticsegmentationmatte/mattetype-swift.struct/teeth.md)
  A matting image that segments the teeth from all people in the visible field of view of an image.
- [static let glasses: AVSemanticSegmentationMatte.MatteType](avsemanticsegmentationmatte/mattetype-swift.struct/glasses.md)
  A matting image that segments eyeglasses and sunglasses from all people in the visible field of view of an image.
### Initializers
- [init(rawValue: String)](avsemanticsegmentationmatte/mattetype-swift.struct/init(rawvalue:).md)
  Creates a matte type with a string.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var matteType: AVSemanticSegmentationMatte.MatteType](avsemanticsegmentationmatte/mattetype-swift.property.md)
  The semantic segmentation matte image type.
- [var mattingImage: CVPixelBuffer](avsemanticsegmentationmatte/mattingimage.md)
  The semantic segmentation matte’s internal image.
- [var pixelFormatType: OSType](avsemanticsegmentationmatte/pixelformattype.md)
  The pixel format type for this object’s internal matting image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/mattetype-swift.struct)*