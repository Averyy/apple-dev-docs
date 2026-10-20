# ARConfiguration.WorldAlignment

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

Options for how ARKit constructs a scene coordinate system based on real-world device motion.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
enum WorldAlignment
```

```c
enum ARWorldAlignment : NSInteger;
```

## Topics

### Alignments
- [ARConfiguration.WorldAlignment.gravity](./worldalignment-swift.enum/gravity.md)
  The coordinate system’s y-axis is parallel to gravity, and its origin is the initial position of the device.
- [ARConfiguration.WorldAlignment.gravityAndHeading](./worldalignment-swift.enum/gravityandheading.md)
  The coordinate system’s y-axis is parallel to gravity, its x- and z-axes are oriented to compass heading, and its origin is the initial position of the device.
- [ARConfiguration.WorldAlignment.camera](./worldalignment-swift.enum/camera.md)
  The scene coordinate system is locked to match the orientation of the camera.
### Initializers
- [init?(rawValue: Int)](./worldalignment-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Configuring the AR session
- [var isLightEstimationEnabled: Bool](./islightestimationenabled.md)
  A Boolean value specifying whether ARKit analyzes scene lighting in captured camera images.
- [var worldAlignment: ARConfiguration.WorldAlignment](./worldalignment-swift.property.md)
  A value specifying how the session maps real-world device motion into a 3D scene coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/worldalignment-swift.enum)*