# accelerationStructureSizes(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Required**: Yes

Returns the buffer sizes the GPU device needs to build, refit, and store an acceleration structure.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
func accelerationStructureSizes(descriptor: MTLAccelerationStructureDescriptor) -> MTLAccelerationStructureSizes
```

#### Return Value

A new [`MTLAccelerationStructureSizes`](mtlaccelerationstructuresizes.md) instance.

## Parameters

- `descriptor`: An   instance.

## See Also

- [func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor) -> (any MTLAccelerationStructure)?](mtldevice/makeaccelerationstructure(descriptor:).md)
  Creates a new ray-tracing acceleration structure from a descriptor.
- [func makeAccelerationStructure(size: Int) -> (any MTLAccelerationStructure)?](mtldevice/makeaccelerationstructure(size:).md)
  Creates a new acceleration structure with a specific size.
- [struct MTLAccelerationStructureSizes](mtlaccelerationstructuresizes.md)
  The expected sizes for a ray-tracing acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/accelerationstructuresizes(descriptor:))*