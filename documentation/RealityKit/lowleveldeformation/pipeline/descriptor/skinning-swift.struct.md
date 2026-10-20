# LowLevelDeformation.Pipeline.Descriptor.Skinning

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The skinning stage configuration for a deformation pipeline.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Skinning
```

## Topics

### Creating a skinning configuration
- [init(jointIndexType: MTLIndexType)](./skinning-swift.struct/init%28jointindextype%29.md)
  Creates a skinning descriptor.
- [var jointIndexType: MTLIndexType](./skinning-swift.struct/jointindextype.md)
  The data type of the joint index buffer.

## Relationships

### Conforms To
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Configuring skinning
- [var skinning: LowLevelDeformation.Pipeline.Descriptor.Skinning?](./skinning-swift.property.md)
  Skinning parameters, or `nil` to omit skinning.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/pipeline/descriptor/skinning-swift.struct)*