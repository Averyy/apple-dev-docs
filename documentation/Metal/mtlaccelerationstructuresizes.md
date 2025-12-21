# MTLAccelerationStructureSizes

**Framework**: Metal  
**Kind**: struct

The expected sizes for a ray-tracing acceleration structure.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct MTLAccelerationStructureSizes
```

## Topics

### Retrieving the sizes
- [var accelerationStructureSize: Int](mtlaccelerationstructuresizes/accelerationstructuresize.md)
  The size of the acceleration structure, in bytes.
- [var buildScratchBufferSize: Int](mtlaccelerationstructuresizes/buildscratchbuffersize.md)
  The amount of scratch memory, in bytes, the GPU devices needs to build the acceleration structure.
- [var refitScratchBufferSize: Int](mtlaccelerationstructuresizes/refitscratchbuffersize.md)
  The amount of scratch memory, in bytes, the GPU device needs to refit the acceleration structure.
### Creating an acceleration size structure
- [init()](mtlaccelerationstructuresizes/init.md)
  Creates an acceleration sizes instance with default values.
- [init(accelerationStructureSize: Int, buildScratchBufferSize: Int, refitScratchBufferSize: Int)](mtlaccelerationstructuresizes/init(accelerationstructuresize:buildscratchbuffersize:refitscratchbuffersize:).md)
  Creates an acceleration sizes instance with specific values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor) -> (any MTLAccelerationStructure)?](mtldevice/makeaccelerationstructure(descriptor:).md)
  Creates a new ray-tracing acceleration structure from a descriptor.
- [func makeAccelerationStructure(size: Int) -> (any MTLAccelerationStructure)?](mtldevice/makeaccelerationstructure(size:).md)
  Creates a new acceleration structure with a specific size.
- [func accelerationStructureSizes(descriptor: MTLAccelerationStructureDescriptor) -> MTLAccelerationStructureSizes](mtldevice/accelerationstructuresizes(descriptor:).md)
  Returns the buffer sizes the GPU device needs to build, refit, and store an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuresizes)*