# maxTotalThreadgroupsPerMeshGrid

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The largest number of threadgroups the pipeline state can have in a single mesh shader grid.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var maxTotalThreadgroupsPerMeshGrid: Int { get }
```

```objc
@property (readonly) NSUInteger maxTotalThreadgroupsPerMeshGrid;
```

## See Also

### Checking mesh shader memory requirements
- [var maxTotalThreadsPerMeshThreadgroup: Int](./maxtotalthreadspermeshthreadgroup.md)
  The largest number of threads the pipeline state can have in a single mesh shader threadgroup.
- [var meshThreadExecutionWidth: Int](./meshthreadexecutionwidth.md)
  The number of threads the render pass applies to a SIMD group for a mesh shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/maxtotalthreadgroupspermeshgrid)*