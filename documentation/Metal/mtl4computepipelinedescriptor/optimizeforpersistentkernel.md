# optimizeForPersistentKernel

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether Metal tunes the pipeline for persistent threads.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
var optimizeForPersistentKernel: Bool { get set }
```

```objc
@property (nonatomic, readwrite) BOOL optimizeForPersistentKernel;
```

## Discussion

Set to `true` to tune the pipeline for long-lived kernels with non-specific grid sizes, such as producer-consumer models. When `true`, call the resulting [`MTLComputePipelineState`](../mtlcomputepipelinestate.md) instance’s [`recommendedPersistentThreadgroupsPerGrid(forThreadsPerThreadgroup:)`](../mtlcomputepipelinestate/recommendedpersistentthreadgroupspergrid%28forthreadsperthreadgroup%29.md) method to get the optimal dispatch size.

This property can’t be `true` when [`forwardProgressUsage`](./forwardprogressusage.md) is [`MTLForwardProgressUsage.weak`](../mtlforwardprogressusage/weak.md) because it’s an invalid configuration which may trigger unpredictable behavior or an error.

The default value is `false`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computepipelinedescriptor/optimizeforpersistentkernel)*