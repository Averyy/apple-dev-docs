# inputBias

**Framework**: SceneKit  
**Kind**: property

An offset to add to the input value of the controller’s animation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var inputBias: CGFloat { get set }
```

#### Discussion

Use this property and the [`inputScale`](scnparticlepropertycontroller/inputscale.md) property to pre-process input values to the controller’s animation. For example, if you use the [`SCNParticleInputMode.overDistance`](scnparticleinputmode/overdistance.md) option to animate a particle’s opacity as a function of its distance from a specified point, a bias specifies the minimum distance at which the animation’s [`fromValue`](https://developer.apple.com/documentation/QuartzCore/CABasicAnimation/fromValue) property or first keyframe value takes effect.

The default value is `0.0`, leaving the input value to the animation unchanged. The range of possible values depends on the controller’s animation.

## See Also

- [var animation: CAAnimation](scnparticlepropertycontroller/animation.md)
  The Core Animation object defining the behavior of the property animation.
- [var inputMode: SCNParticleInputMode](scnparticlepropertycontroller/inputmode.md)
  The mode that determines input values for the property controller’s animation.
- [var inputScale: CGFloat](scnparticlepropertycontroller/inputscale.md)
  A factor for multiplying the input value of the controller’s animation.
- [var inputOrigin: SCNNode?](scnparticlepropertycontroller/inputorigin.md)
  A node whose distance to each particle provides input values for the controller’s animation.
- [var inputProperty: SCNParticleSystem.ParticleProperty?](scnparticlepropertycontroller/inputproperty.md)
  A particle property that provides input values for this property controller’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/inputbias)*