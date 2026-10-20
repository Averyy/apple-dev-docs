# MTLAccelerationStructureSizes

**Framework**: Metal  
**Kind**: struct  
**Role**: Structure

The expected sizes for a ray-tracing acceleration structure.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct MTLAccelerationStructureSizes
```

```c
typedef struct { ... } MTLAccelerationStructureSizes;
```

## Topics

### Retrieving the sizes
- [var accelerationStructureSize: Int](./mtlaccelerationstructuresizes/accelerationstructuresize.md)
  The size of the acceleration structure, in bytes.
- [var buildScratchBufferSize: Int](./mtlaccelerationstructuresizes/buildscratchbuffersize.md)
  The amount of scratch memory, in bytes, the GPU devices needs to build the acceleration structure.
- [var refitScratchBufferSize: Int](./mtlaccelerationstructuresizes/refitscratchbuffersize.md)
  The amount of scratch memory, in bytes, the GPU device needs to refit the acceleration structure.
### Creating an acceleration size structure
- [init()](./mtlaccelerationstructuresizes/init%28%29.md)
  Creates an acceleration sizes instance with default values.
- [init(accelerationStructureSize: Int, buildScratchBufferSize: Int, refitScratchBufferSize: Int)](./mtlaccelerationstructuresizes/init%28accelerationstructuresize,buildscratchbuffersize,refitscratchbuffersize%29.md)
  Creates an acceleration sizes instance with specific values.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Creating acceleration structures for ray tracing
- [func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor) -> (any MTLAccelerationStructure)?](./mtldevice/makeaccelerationstructure%28descriptor%29.md)
  Creates a new ray-tracing acceleration structure from a descriptor.
- [func makeAccelerationStructure(size: Int) -> (any MTLAccelerationStructure)?](./mtldevice/makeaccelerationstructure%28size%29.md)
  Creates a new acceleration structure with a specific size.
- [func accelerationStructureSizes(descriptor: MTLAccelerationStructureDescriptor) -> MTLAccelerationStructureSizes](./mtldevice/accelerationstructuresizes%28descriptor%29.md)
  Returns the buffer sizes the GPU device needs to build, refit, and store an acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlaccelerationstructuresizes)*