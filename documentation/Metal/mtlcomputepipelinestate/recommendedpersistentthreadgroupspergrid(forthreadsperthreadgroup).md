# recommendedPersistentThreadgroupsPerGrid(forThreadsPerThreadgroup:)

**Framework**: Metal  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the number of threadgroups per grid that achieves the best throughput for a threads-per-threadgroup size.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func recommendedPersistentThreadgroupsPerGrid(forThreadsPerThreadgroup threadsPerThreadgroup: MTLSize) -> Int
```

```objc
- (NSUInteger) recommendedPersistentThreadgroupsPerGridForThreadsPerThreadgroup:(MTLSize) threadsPerThreadgroup;
```

## Return Value

The number of threadgroups to dispatch. Pass a threadgroup count to a dispatch method, such as [`dispatchThreadgroups(_:threadsPerThreadgroup:)`](../mtlcomputecommandencoder/dispatchthreadgroups%28_,threadsperthreadgroup%29.md), whose width, height, and depth product equals this value.

## Discussion

This method applies to pipelines you create with an [`MTLComputePipelineDescriptor`](../mtlcomputepipelinedescriptor.md) with its [`optimizeForPersistentKernel`](../mtlcomputepipelinedescriptor/optimizeforpersistentkernel.md) property equal to `true`.

## Parameters

- `threadsPerThreadgroup`: The number of threads in each threadgroup.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlcomputepipelinestate/recommendedpersistentthreadgroupspergrid(forthreadsperthreadgroup:))*