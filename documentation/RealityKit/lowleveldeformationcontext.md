# LowLevelDeformationContext

**Framework**: RealityKit  
**Kind**: class

An object that manages shared resources for [`LowLevelDeformation`](lowleveldeformation.md) instances.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class LowLevelDeformationContext
```

## Topics

### Creating deformation pipelines
- [func makeDeformation(pipeline: LowLevelDeformation.Pipeline, descriptor: LowLevelDeformation.Descriptor) throws -> LowLevelDeformation](lowleveldeformationcontext/makedeformation(pipeline:descriptor:).md)
  Creates a deformation bound to a compiled pipeline.
- [func makePipeline(desc: LowLevelDeformation.Pipeline.Descriptor) throws -> LowLevelDeformation.Pipeline](lowleveldeformationcontext/makepipeline(desc:)-9riyx.md)
  Creates a compute pipeline synchronously.
- [func makePipeline(desc: LowLevelDeformation.Pipeline.Descriptor) async throws -> LowLevelDeformation.Pipeline](lowleveldeformationcontext/makepipeline(desc:)-4ybrk.md)
  Creates a compute pipeline asynchronously.
### Accessing the device
- [let device: any MTLDevice](lowleveldeformationcontext/device.md)
  The Metal device this context targets.
### Initializers
- [init(any MTLDevice) throws](lowleveldeformationcontext/init(_:).md)
  Creates a context targeting the specified Metal device.
### Instance Methods
- [func makePipeline(desc:)](lowleveldeformationcontext/makepipeline(desc:).md)
  Creates a compute pipeline asynchronously.

## See Also

- [class LowLevelDeformation](lowleveldeformation.md)
  An object that encodes blend-shape, skinning, and renormalization passes into a Metal compute command encoder.
- [class CanaryDescription](canarydescription.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformationcontext)*