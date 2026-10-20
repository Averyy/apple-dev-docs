# AVSemanticSegmentationMatte.MatteType

**Framework**: AVFoundation  
**Kind**: struct  
**Role**: Structure

A structure that defines the types of segmentation matte images that you can capture along with the primary image.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct MatteType
```

```c
typedef NSString * AVSemanticSegmentationMatteType;
```

## Topics

### Matte types
- [static let hair: AVSemanticSegmentationMatte.MatteType](./mattetype-swift.struct/hair.md)
  A matting image that segments the hair from all people in the visible field of view of an image.
- [static let skin: AVSemanticSegmentationMatte.MatteType](./mattetype-swift.struct/skin.md)
  A matting image that segments the skin from all people in the visible field of view of an image.
- [static let teeth: AVSemanticSegmentationMatte.MatteType](./mattetype-swift.struct/teeth.md)
  A matting image that segments the teeth from all people in the visible field of view of an image.
- [static let glasses: AVSemanticSegmentationMatte.MatteType](./mattetype-swift.struct/glasses.md)
  A matting image that segments eyeglasses and sunglasses from all people in the visible field of view of an image.
### Initializers
- [init(rawValue: String)](./mattetype-swift.struct/init%28rawvalue%29.md)
  Creates a matte type with a string.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting a segmentation matte
- [var matteType: AVSemanticSegmentationMatte.MatteType](./mattetype-swift.property.md)
  The semantic segmentation matte image type.
- [var mattingImage: CVPixelBuffer](./mattingimage.md)
  The semantic segmentation matte’s internal image.
- [var pixelFormatType: OSType](./pixelformattype.md)
  The pixel format type for this object’s internal matting image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avsemanticsegmentationmatte/mattetype-swift.struct)*