# requiredThreadsPerObjectThreadgroup

**Framework**: Metal  
**Kind**: property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var requiredThreadsPerObjectThreadgroup: MTLSize { get set }
```

#### Discussion

Sets the required object threads-per-threadgroup during mesh draws. The `threadsPerObjectThreadgroup` argument of any draw must match to this value if it is set. Optional, unless the pipeline is going to use CooperativeTensors in which case this must be set. Setting this to a size of 0 in every dimension disables this property


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtlmeshrenderpipelinedescriptor/requiredthreadsperobjectthreadgroup)*