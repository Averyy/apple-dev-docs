# objectThreadExecutionWidth

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The number of threads the render pass applies to a SIMD group for an object shader.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var objectThreadExecutionWidth: Int { get }
```

#### Discussion

You can access the value of this property in your shader code by adding an integer parameter with the `[[threads_per_simdgroup]]` attribute. For more information about this attribute, see the [`Metal Shading Language Specification (PDF)`](https://developer.apple.comhttps://developer.apple.com/metal/Metal-Shading-Language-Specification.pdf).

## See Also

- [var maxTotalThreadsPerObjectThreadgroup: Int](mtlrenderpipelinestate/maxtotalthreadsperobjectthreadgroup.md)
  The largest number of threads the pipeline state can have in a single object shader threadgroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/objectthreadexecutionwidth)*