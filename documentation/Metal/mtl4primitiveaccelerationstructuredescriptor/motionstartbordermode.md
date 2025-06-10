# motionStartBorderMode

**Framework**: Metal  
**Kind**: property

Configures the behavior when the ray-tracing system samples the acceleration structure before the motion start time.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var motionStartBorderMode: MTLMotionBorderMode { get set }
```

#### Discussion

Use this property to control the behavior when the ray-tracing system samples the acceleration structure at a time prior to the one you set for [`motionStartTime`](mtl4primitiveaccelerationstructuredescriptor/motionstarttime.md).

The default value of this property is `MTLMotionBorderModeClamp`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4primitiveaccelerationstructuredescriptor/motionstartbordermode)*