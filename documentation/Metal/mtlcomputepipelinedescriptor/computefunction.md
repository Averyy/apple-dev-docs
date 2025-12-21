# computeFunction

**Framework**: Metal  
**Kind**: property

The compute kernel the pipeline calls.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var computeFunction: (any MTLFunction)? { get set }
```

#### Discussion

> ⚠️ **Warning**:  Ensure that this value is non-`nil` before creating a new [`MTLComputePipelineState`](mtlcomputepipelinestate.md) with the associated pipeline descriptor instance.

The default value is `nil`.

## See Also

- [var threadGroupSizeIsMultipleOfThreadExecutionWidth: Bool](mtlcomputepipelinedescriptor/threadgroupsizeismultipleofthreadexecutionwidth.md)
  A Boolean value that indicates whether the threadgroup size is always a multiple of the thread execution width.
- [var maxTotalThreadsPerThreadgroup: Int](mtlcomputepipelinedescriptor/maxtotalthreadsperthreadgroup.md)
  A property that limits the number of threads you can dispatch in a threadgroup for the compute function.
- [var maxCallStackDepth: Int](mtlcomputepipelinedescriptor/maxcallstackdepth.md)
  The maximum call stack depth for indirect function calls in compute shaders.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinedescriptor/computefunction)*