# maxTotalThreadsPerMeshThreadgroup

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The largest number of threads the pipeline state can have in a single mesh shader threadgroup.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var maxTotalThreadsPerMeshThreadgroup: Int { get }
```

## See Also

- [var maxTotalThreadgroupsPerMeshGrid: Int](mtlrenderpipelinestate/maxtotalthreadgroupspermeshgrid.md)
  The largest number of threadgroups the pipeline state can have in a single mesh shader grid.
- [var meshThreadExecutionWidth: Int](mtlrenderpipelinestate/meshthreadexecutionwidth.md)
  The number of threads the render pass applies to a SIMD group for a mesh shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/maxtotalthreadspermeshthreadgroup)*