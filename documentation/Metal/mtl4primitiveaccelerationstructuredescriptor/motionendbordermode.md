# motionEndBorderMode

**Framework**: Metal  
**Kind**: property

Configures the motion border mode.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var motionEndBorderMode: MTLMotionBorderMode { get set }
```

#### Discussion

This property controls what happens if Metal samples the acceleration structure after [`motionEndTime`](mtl4primitiveaccelerationstructuredescriptor/motionendtime.md).

Its default value is `MTLMotionBorderModeClamp`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4primitiveaccelerationstructuredescriptor/motionendbordermode)*