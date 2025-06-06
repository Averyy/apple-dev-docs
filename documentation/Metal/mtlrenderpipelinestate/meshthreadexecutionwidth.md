# meshThreadExecutionWidth

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The number of threads the render pass applies to a SIMD group for a mesh shader.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var meshThreadExecutionWidth: Int { get }
```

#### Discussion

You can access the value of this property in your shader code by adding an integer parameter with the `[[threads_per_simdgroup]]` attribute. For more information about this attribute, see the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## See Also

- [var maxTotalThreadsPerMeshThreadgroup: Int](mtlrenderpipelinestate/maxtotalthreadspermeshthreadgroup.md)
  The largest number of threads the pipeline state can have in a single mesh shader threadgroup.
- [var maxTotalThreadgroupsPerMeshGrid: Int](mtlrenderpipelinestate/maxtotalthreadgroupspermeshgrid.md)
  The largest number of threadgroups the pipeline state can have in a single mesh shader grid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/meshthreadexecutionwidth)*