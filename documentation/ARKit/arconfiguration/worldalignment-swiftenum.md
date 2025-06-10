# ARConfiguration.WorldAlignment

**Framework**: ARKit  
**Kind**: enum

Options for how ARKit constructs a scene coordinate system based on real-world device motion.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
enum WorldAlignment
```

## Topics

### Alignments
- [ARConfiguration.WorldAlignment.gravity](arconfiguration/worldalignment-swift.enum/gravity.md)
  The coordinate system’s y-axis is parallel to gravity, and its origin is the initial position of the device.
- [ARConfiguration.WorldAlignment.gravityAndHeading](arconfiguration/worldalignment-swift.enum/gravityandheading.md)
  The coordinate system’s y-axis is parallel to gravity, its x- and z-axes are oriented to compass heading, and its origin is the initial position of the device.
- [ARConfiguration.WorldAlignment.camera](arconfiguration/worldalignment-swift.enum/camera.md)
  The scene coordinate system is locked to match the orientation of the camera.
### Initializers
- [init?(rawValue: Int)](arconfiguration/worldalignment-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isLightEstimationEnabled: Bool](arconfiguration/islightestimationenabled.md)
  A Boolean value specifying whether ARKit analyzes scene lighting in captured camera images.
- [var worldAlignment: ARConfiguration.WorldAlignment](arconfiguration/worldalignment-swift.property.md)
  A value specifying how the session maps real-world device motion into a 3D scene coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/worldalignment-swift.enum)*