# threadGroupSizeIsMultipleOfThreadExecutionWidth

**Framework**: Metal  
**Kind**: property

A Boolean value that indicates whether the threadgroup size is always a multiple of the thread execution width.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var threadGroupSizeIsMultipleOfThreadExecutionWidth: Bool { get set }
```

#### Discussion

> ⚠️ **Warning**:  When this configuration value is `true` and the threadgroup size isn’t a multiple of thread execution width, the compute pass’s execution results are undefined.

If you can guarantee that the threadgroup size used by all compute commands in this pipeline is a multiple of [`threadExecutionWidth`](mtlcomputepipelinestate/threadexecutionwidth.md), set this property to `true` to take advantage of additional Metal optimizations.

The default value is `false`.

## See Also

- [var computeFunction: (any MTLFunction)?](mtlcomputepipelinedescriptor/computefunction.md)
  The compute kernel the pipeline calls.
- [var maxTotalThreadsPerThreadgroup: Int](mtlcomputepipelinedescriptor/maxtotalthreadsperthreadgroup.md)
  The maximum number of threads in a threadgroup that you can dispatch to the compute function.
- [var maxCallStackDepth: Int](mtlcomputepipelinedescriptor/maxcallstackdepth.md)
  The maximum recursive call depth for dynamic library, visible, and intersection functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/threadgroupsizeismultipleofthreadexecutionwidth)*