# motionTransformCountBuffer

**Framework**: Metal  
**Kind**: property

Associates a buffer reference containing the number of motion transforms in the motion transform buffer, formatted as a 32-bit unsigned integer.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var motionTransformCountBuffer: MTL4BufferRange { get set }
```

#### Discussion

You are responsible for ensuring that the final number of motion transforms at build time in the buffer this property references is less than or equal to the value of property [`maxMotionTransformCount`](mtl4indirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformcountbuffer)*