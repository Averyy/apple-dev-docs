# staticThreadgroupMemoryLength

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The length, in bytes, of statically allocated threadgroup memory.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var staticThreadgroupMemoryLength: Int { get }
```

## See Also

- [var maxTotalThreadsPerThreadgroup: Int](mtlcomputepipelinestate/maxtotalthreadsperthreadgroup.md)
  The maximum number of threads in a threadgroup that you can dispatch to the pipeline.
- [var threadExecutionWidth: Int](mtlcomputepipelinestate/threadexecutionwidth.md)
  The number of threads that the GPU executes simultaneously.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/staticthreadgroupmemorylength)*