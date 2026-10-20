# LowLevelDeformation.Error

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

The error type thrown by every throwing method and initializer.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Error
```

## Relationships

### Conforms To
- [Error](../../Swift/error.md)
- [LocalizedError](../../Foundation/localizederror.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Encoding deformation work
- [func encode(into: any MTLComputeCommandEncoder) throws](./encode%28into%29.md)
  Encodes the configured deformation passes into the given command encoder.
- [LowLevelDeformation.Pipeline](./pipeline.md)
  A compiled compute pipeline for a specific combination of mesh layouts and deformer stages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformation/error)*