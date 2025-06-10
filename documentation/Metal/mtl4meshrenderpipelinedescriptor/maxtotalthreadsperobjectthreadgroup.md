# maxTotalThreadsPerObjectThreadgroup

**Framework**: Metal  
**Kind**: property

Controls the largest number of threads the pipeline state can execute in a single object shader threadgroup dispatch.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var maxTotalThreadsPerObjectThreadgroup: Int { get set }
```

#### Discussion

This number represents the maximum size of the product of the components of parameter `threadsPerObjectThreadgroup` that Metal can use when drawing with this pipeline in mesh shader dispatch methods, such as [`drawMeshThreadgroups(threadgroupsPerGrid:threadsPerObjectThreadgroup:threadsPerMeshThreadgroup:)`](mtl4rendercommandencoder/drawmeshthreadgroups(threadgroupspergrid:threadsperobjectthreadgroup:threadspermeshthreadgroup:).md).

The compiler’s optimizer can use the value of this property to generate more efficient code, specifically when the value doesn’t exceed the thread execution width of the underlying GPU.

The default value of this property is `0`, which indicates that the number you pass to attribute `[[max_total_threads_per_threadgroup(N)]]` of the pipeline’s object function determines the maximum total threads per threadgroup.

When you specify both the `[[max_total_threads_per_threadgroup(N)]]` attribute and this property, you are responsible for making sure these values match.

Additionally, you are responsible for ensuring this value doesn’t exceed the “maximum threads per threadgroup” device limit documented in the “Metal Feature Set Tables” PDF: [`https://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Feature-Set-Tables.pdf).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4meshrenderpipelinedescriptor/maxtotalthreadsperobjectthreadgroup)*