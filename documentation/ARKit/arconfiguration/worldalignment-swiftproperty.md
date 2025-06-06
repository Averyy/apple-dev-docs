# worldAlignment

**Framework**: ARKit  
**Kind**: property

A value specifying how the session maps real-world device motion into a 3D scene coordinate system.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+

## Declaration

```swift
var worldAlignment: ARConfiguration.WorldAlignment { get set }
```

## Mentions

- [Understanding World Tracking](understanding-world-tracking.md)

#### Discussion

Creating an AR experience depends on being able to construct a coordinate system for placing objects in a virtual 3D world that maps to the real-world position and motion of the device. When you run a session configuration, ARKit creates a scene coordinate system based on the position and orientation of the device; any [`ARAnchor`](aranchor.md) objects you create or that the AR session detects are positioned relative to that coordinate system.

See [`ARConfiguration.WorldAlignment`](arconfiguration/worldalignment-swift.enum.md) for possible values.

## See Also

- [var isLightEstimationEnabled: Bool](arconfiguration/islightestimationenabled.md)
  A Boolean value specifying whether ARKit analyzes scene lighting in captured camera images.
- [ARConfiguration.WorldAlignment](arconfiguration/worldalignment-swift.enum.md)
  Options for how ARKit constructs a scene coordinate system based on real-world device motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/worldalignment-swift.property)*