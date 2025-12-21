# MTLAllocation

**Framework**: Metal  
**Kind**: protocol

A memory allocation from a Metal GPU device, such as a memory heap, texture, or data buffer.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
protocol MTLAllocation : NSObjectProtocol
```

## Mentions

- [Simplifying GPU resource management with residency sets](simplifying-gpu-resource-management-with-residency-sets.md)

#### Overview

Types that conform to [`MTLAllocation`](mtlallocation.md), including [`MTLBuffer`](mtlbuffer.md), [`MTLTexture`](mtltexture.md), and [`MTLHeap`](mtlheap.md), have underlying memory. You make their memory , or GPU-accessible, by adding an allocation to an [`MTLResidencySet`](mtlresidencyset.md) or calling the appropriate method of a command encoder.

See [`Simplifying GPU resource management with residency sets`](simplifying-gpu-resource-management-with-residency-sets.md) for more information.

## Topics

### Inspecting an allocation
- [var allocatedSize: Int](mtlallocation/allocatedsize.md)
  The amount of memory, in byes, a resource consumes, such as for a buffer, texture, or heap.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
### Inherited By
- [MTL4MachineLearningPipelineState](mtl4machinelearningpipelinestate.md)
- [MTLAccelerationStructure](mtlaccelerationstructure.md)
- [MTLBuffer](mtlbuffer.md)
- [MTLComputePipelineState](mtlcomputepipelinestate.md)
- [MTLHeap](mtlheap.md)
- [MTLIndirectCommandBuffer](mtlindirectcommandbuffer.md)
- [MTLIntersectionFunctionTable](mtlintersectionfunctiontable.md)
- [MTLRenderPipelineState](mtlrenderpipelinestate.md)
- [MTLResource](mtlresource.md)
- [MTLTensor](mtltensor.md)
- [MTLTexture](mtltexture.md)
- [MTLVisibleFunctionTable](mtlvisiblefunctiontable.md)

## See Also

- [typealias MTLGPUAddress](mtlgpuaddress.md)
  A 64-bit unsigned integer type appropriate for storing GPU addresses.
- [protocol MTLResource](mtlresource.md)
  An allocation of memory accessible to a GPU.
- [struct MTLResourceOptions](mtlresourceoptions.md)
  Optional arguments used to set the behavior of a resource.
- [struct MTLResourceUsage](mtlresourceusage.md)
  Options that describe how a graphics or compute function uses an argument buffer’s resource.
- [struct MTLResourceID](mtlresourceid.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlallocation)*