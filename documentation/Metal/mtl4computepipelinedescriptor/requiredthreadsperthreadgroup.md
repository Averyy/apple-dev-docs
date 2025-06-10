# requiredThreadsPerThreadgroup

**Framework**: Metal  
**Kind**: property

Sets the required threads-per-threadgroup during dispatches. The `threadsPerThreadgroup` argument of any dispatch must match this value if it is set. Optional, unless the pipeline is going to use CooperativeTensors in which case this must be set. Setting this to a size of 0 in every dimension disables this property

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var requiredThreadsPerThreadgroup: MTLSize { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computepipelinedescriptor/requiredthreadsperthreadgroup)*