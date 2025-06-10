# motionTransformBuffer

**Framework**: Metal  
**Kind**: property

A buffer containing transformation information for instance motion keyframes, formatted according to the motion transform type.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var motionTransformBuffer: MTL4BufferRange { get set }
```

#### Discussion

Each instance can have a different number of keyframes that you configure via individual instance descriptors.

You are responsible for ensuring the buffer address the range references is not zero when using motion instance descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformbuffer)*