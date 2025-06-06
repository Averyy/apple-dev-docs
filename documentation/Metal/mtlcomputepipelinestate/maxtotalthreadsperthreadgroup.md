# maxTotalThreadsPerThreadgroup

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The maximum number of threads in a threadgroup that you can dispatch to the pipeline.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var maxTotalThreadsPerThreadgroup: Int { get }
```

## Mentions

- [Calculating Threadgroup and Grid Sizes](calculating-threadgroup-and-grid-sizes.md)

#### Discussion

When you create a compute pipeline state, it calculates the maximum number of threads available on the device. This value never changes, but may be different for different pipeline objects.

See [`Creating Threads and Threadgroups`](creating-threads-and-threadgroups.md) and [`Calculating Threadgroup and Grid Sizes`](calculating-threadgroup-and-grid-sizes.md) for more information on aligning data, thread width, and threadgroup size.

## See Also

- [var threadExecutionWidth: Int](mtlcomputepipelinestate/threadexecutionwidth.md)
  The number of threads that the GPU executes simultaneously.
- [var staticThreadgroupMemoryLength: Int](mtlcomputepipelinestate/staticthreadgroupmemorylength.md)
  The length, in bytes, of statically allocated threadgroup memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/maxtotalthreadsperthreadgroup)*