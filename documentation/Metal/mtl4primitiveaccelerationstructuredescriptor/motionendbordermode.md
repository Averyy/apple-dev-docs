# motionEndBorderMode

**Framework**: Metal  
**Kind**: property  
**Role**: Instance Property

Configures the motion border mode.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var motionEndBorderMode: MTLMotionBorderMode { get set }
```

```objc
@property (nonatomic) MTLMotionBorderMode motionEndBorderMode;
```

## Discussion

This property controls what happens if Metal samples the acceleration structure after [`motionEndTime`](./motionendtime.md).

Its default value is `MTLMotionBorderModeClamp`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4primitiveaccelerationstructuredescriptor/motionendbordermode)*