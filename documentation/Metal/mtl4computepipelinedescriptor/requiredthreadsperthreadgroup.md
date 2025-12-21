# requiredThreadsPerThreadgroup

**Framework**: Metal  
**Kind**: property

The required number of threads per threadgroup for compute dispatches.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

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