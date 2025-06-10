# threadExecutionWidth

**Framework**: Metal  
**Kind**: property  
**Required**: Yes

The number of threads that the GPU executes simultaneously.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
var threadExecutionWidth: Int { get }
```

## Mentions

- [Creating Threads and Threadgroups](creating-threads-and-threadgroups.md)
- [Calculating Threadgroup and Grid Sizes](calculating-threadgroup-and-grid-sizes.md)

#### Discussion

For better performance, when dispatching a compute command, make the number of threads in the threadgroup a multiple of `threadExecutionWidth`.

See [`Creating Threads and Threadgroups`](creating-threads-and-threadgroups.md) and [`Calculating Threadgroup and Grid Sizes`](calculating-threadgroup-and-grid-sizes.md) for more information on aligning data, thread width, and threadgroup size.

## See Also

- [var maxTotalThreadsPerThreadgroup: Int](mtlcomputepipelinestate/maxtotalthreadsperthreadgroup.md)
  The maximum number of threads in a threadgroup that you can dispatch to the pipeline.
- [var staticThreadgroupMemoryLength: Int](mtlcomputepipelinestate/staticthreadgroupmemorylength.md)
  The length, in bytes, of statically allocated threadgroup memory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/threadexecutionwidth)*