# maxTotalThreadsPerObjectThreadgroup

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The largest number of threads the pipeline state can have in a single object shader threadgroup.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
var maxTotalThreadsPerObjectThreadgroup: Int { get }
```

## See Also

- [var objectThreadExecutionWidth: Int](mtlrenderpipelinestate/objectthreadexecutionwidth.md)
  The number of threads the render pass applies to a SIMD group for an object shader.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlrenderpipelinestate/maxtotalthreadsperobjectthreadgroup)*