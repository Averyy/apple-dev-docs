# requiredThreadsPerObjectThreadgroup

**Framework**: Metal  
**Kind**: property

Controls the required number of object threads-per-threadgroup when drawing with a mesh shader pipeline you create from this descriptor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var requiredThreadsPerObjectThreadgroup: MTLSize { get set }
```

#### Discussion

This argument is optional, unless this pipeline uses `CooperativeTensors`, in which case you are responsible for providing it.

When this value is set to non-zero, you are responsible for ensuring the parameter `threadsPerObjectThreadgroup` in any mesh dispatch draw calls that use this mesh render pipeline, such as [`drawMeshThreadgroups(threadgroupsPerGrid:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)`](mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md), match it.

Setting this value to a size of 0 in every dimension disables this property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup)*