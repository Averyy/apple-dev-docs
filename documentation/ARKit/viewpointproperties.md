# ViewpointProperties

**Framework**: ARKit  
**Kind**: struct

The ViewpointProperties is a record of render camera transforms at some particular time.

**Availability**:
- visionOS 2.4+

## Declaration

```swift
struct ViewpointProperties
```

## Topics

### Instance Properties
- [var description: String](viewpointproperties/description.md)
  Textual representation of the viewpoint properties.
- [var deviceFromLeftViewpointTransform: simd_float4x4](viewpointproperties/devicefromleftviewpointtransform.md)
  The transformation matrix that converts from the left viewpoint to the device’s coordinate space.
- [var deviceFromRightViewpointTransform: simd_float4x4](viewpointproperties/devicefromrightviewpointtransform.md)
  The transformation matrix that converts from the left viewpoint to the device’s coordinate space.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/viewpointproperties)*