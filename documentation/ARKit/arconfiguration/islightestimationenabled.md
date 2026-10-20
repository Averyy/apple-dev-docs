# isLightEstimationEnabled

**Framework**: ARKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value specifying whether ARKit analyzes scene lighting in captured camera images.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+

## Declaration

```swift
var isLightEstimationEnabled: Bool { get set }
```

```objc
@property (nonatomic, assign, getter=isLightEstimationEnabled) BOOL lightEstimationEnabled;
```

#### Discussion

When this value is [`true`](../../Swift/true.md) (the default), a running AR session provides scene lighting information in the [`lightEstimate`](../arframe/lightestimate.md) property of each [`ARFrame`](../arframe.md) object it captures.

If you render your own overlay graphics for the AR scene, you can use this information in shading algorithms to help make those graphics match the real-world lighting conditions of the scene captured by the camera. (A [`RealityView`](../../RealityKit/realityview.md) or [`ARView`](../../RealityKit/arview.md) automatically uses this information to configure RealityKit lighting.)

## See Also

### Configuring the AR session
- [var worldAlignment: ARConfiguration.WorldAlignment](./worldalignment-swift.property.md)
  A value specifying how the session maps real-world device motion into a 3D scene coordinate system.
- [ARConfiguration.WorldAlignment](./worldalignment-swift.enum.md)
  Options for how ARKit constructs a scene coordinate system based on real-world device motion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/arconfiguration/islightestimationenabled)*