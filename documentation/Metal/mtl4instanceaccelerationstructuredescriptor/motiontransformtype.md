# motionTransformType

**Framework**: Metal  
**Kind**: property

Controls the type of motion transforms, either as a matrix or individual components.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var motionTransformType: MTLTransformType { get set }
```

#### Discussion

Defaults to `MTLTransformTypePackedFloat4x3`. Using a `MTLTransformTypeComponent` allows you to represent the rotation by a quaternion (instead as of part of the matrix), allowing for correct motion interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metal/mtl4instanceaccelerationstructuredescriptor/motiontransformtype)*