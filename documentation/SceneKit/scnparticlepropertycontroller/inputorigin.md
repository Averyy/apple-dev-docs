# inputOrigin

**Framework**: SceneKit  
**Kind**: property

A node whose distance to each particle provides input values for the controller’s animation.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
weak var inputOrigin: SCNNode? { get set }
```

#### Discussion

This property applies only when the controller’s [`inputMode`](scnparticlepropertycontroller/inputmode.md) value is [`SCNParticleInputMode.overDistance`](scnparticleinputmode/overdistance.md). When you select that input mode, this property’s value must be a node in the scene containing the particle system; otherwise, SceneKit ignores this property. The default value is `nil`.

SceneKit calculates the distance between this node’s [`position`](scnnode/position.md) vector (converted to the scene’s world coordinate space) and each particle and then uses the resulting value as the input to the controller’s animation. For example, if you use this option to animate particle opacity from `1.0` to `0.0`, all particles beyond a certain distance from the [`inputOrigin`](scnparticlepropertycontroller/inputorigin.md) node are fully transparent—regardless of any random velocity or direction variations in reaching that distance.

To refine the relationship between a range of distances and a range of input values for the controller’s animation, use the [`inputBias`](scnparticlepropertycontroller/inputbias.md) and [`inputScale`](scnparticlepropertycontroller/inputscale.md) properties.

## See Also

- [var animation: CAAnimation](scnparticlepropertycontroller/animation.md)
  The Core Animation object defining the behavior of the property animation.
- [var inputMode: SCNParticleInputMode](scnparticlepropertycontroller/inputmode.md)
  The mode that determines input values for the property controller’s animation.
- [var inputBias: CGFloat](scnparticlepropertycontroller/inputbias.md)
  An offset to add to the input value of the controller’s animation.
- [var inputScale: CGFloat](scnparticlepropertycontroller/inputscale.md)
  A factor for multiplying the input value of the controller’s animation.
- [var inputProperty: SCNParticleSystem.ParticleProperty?](scnparticlepropertycontroller/inputproperty.md)
  A particle property that provides input values for this property controller’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/inputorigin)*