# accelerationStructureSizes(descriptor:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
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

```objc
- (MTLAccelerationStructureSizes) accelerationStructureSizesWithDescriptor:(MTLAccelerationStructureDescriptor *) descriptor;
```

## Return Value

A new [`MTLAccelerationStructureSizes`](../mtlaccelerationstructuresizes.md) instance.

## Parameters

- `descriptor`: An [`MTLAccelerationStructureDescriptor`](../mtlaccelerationstructuredescriptor.md) instance.

## See Also

### Creating acceleration structures for ray tracing
- [func makeAccelerationStructure(descriptor: MTLAccelerationStructureDescriptor) -> (any MTLAccelerationStructure)?](./makeaccelerationstructure%28descriptor%29.md)
  Creates a new ray-tracing acceleration structure from a descriptor.
- [func makeAccelerationStructure(size: Int) -> (any MTLAccelerationStructure)?](./makeaccelerationstructure%28size%29.md)
  Creates a new acceleration structure with a specific size.
- [struct MTLAccelerationStructureSizes](../mtlaccelerationstructuresizes.md)
  The expected sizes for a ray-tracing acceleration structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtldevice/accelerationstructuresizes(descriptor:))*