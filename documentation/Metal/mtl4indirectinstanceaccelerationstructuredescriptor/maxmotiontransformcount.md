# maxMotionTransformCount

**Framework**: Metal  
**Kind**: property

Controls the maximum number of motion transforms in the motion transform buffer.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var maxMotionTransformCount: Int { get set }
```

#### Discussion

You are responsible for ensuring that final number of motion transforms at build time that the buffer [`motionTransformCountBuffer`](mtl4indirectinstanceaccelerationstructuredescriptor/motiontransformcountbuffer.md) references is less than or equal to this number.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4indirectinstanceaccelerationstructuredescriptor/maxmotiontransformcount)*