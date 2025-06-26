# requiredThreadsPerThreadgroup

**Framework**: Metal  
**Kind**: property

The required number of threads per threadgroup for compute dispatches.

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

#### Discussion

When you set this value, you are responsible for ensuring that the `threadsPerThreadgroup` argument of any compute dispatch matches it.

Setting this property is optional, except in cases where the pipeline uses .

This property’s default value is `0`, which disables its effect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4computepipelinedescriptor/requiredthreadsperthreadgroup)*