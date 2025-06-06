# makeAccelerationStructure(size:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Creates a new acceleration structure with a specific size.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func makeAccelerationStructure(size: Int) -> (any MTLAccelerationStructure)?
```

#### Return Value

A new [`MTLAccelerationStructure`](mtlaccelerationstructure.md) instance if the method completed successfully; otherwise `nil`.

## Parameters

- `size`: The size of the new acceleration structure, in bytes.

## See Also

- [func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor) -> (any MTLAccelerationStructure)?](mtldevice/makeaccelerationstructure(descriptor:).md)
  Creates a new ray-tracing acceleration structure from a descriptor.
- [func accelerationStructureSizes(descriptor: MTLAccelerationStructureDescriptor) -> MTLAccelerationStructureSizes](mtldevice/accelerationstructuresizes(descriptor:).md)
  Returns the buffer sizes the GPU device needs to build, refit, and store an acceleration structure.
- [struct MTLAccelerationStructureSizes](mtlaccelerationstructuresizes.md)
  The expected sizes for a ray-tracing acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/makeaccelerationstructure(size:))*