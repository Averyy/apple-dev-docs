# animation

**Framework**: SceneKit  
**Kind**: property

The Core Animation object defining the behavior of the property animation.

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
var animation: CAAnimation { get set }
```

#### Discussion

You can use different [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation) subclasses to animate effects in different ways. For example, a [`CABasicAnimation`](https://developer.apple.com/documentation/QuartzCore/CABasicAnimation) transitions a property from one value to another, and a [`CAKeyframeAnimation`](https://developer.apple.com/documentation/QuartzCore/CAKeyframeAnimation) transitions a property through a series of values. You use properties of the animation object to define its timing curve, repeat mode, and other options.

SceneKit ignores the [`keyPath`](https://developer.apple.com/documentation/QuartzCore/CAPropertyAnimation/keyPath) property of this animation object. Instead, when you attach a property controller to a particle system’s [`propertyControllers`](scnparticlesystem/propertycontrollers.md) dictionary, use one of the keys listed in Particle Property Keys to specify which particle property it animates. SceneKit also ignores the animation’s [`duration`](https://developer.apple.com/documentation/QuartzCore/CAMediaTiming/duration) and [`repeatCount`](https://developer.apple.com/documentation/QuartzCore/CAMediaTiming/repeatCount) properties. Instead, the controller defines the behavior of the animation’s input value.

## See Also

- [var inputMode: SCNParticleInputMode](scnparticlepropertycontroller/inputmode.md)
  The mode that determines input values for the property controller’s animation.
- [var inputBias: CGFloat](scnparticlepropertycontroller/inputbias.md)
  An offset to add to the input value of the controller’s animation.
- [var inputScale: CGFloat](scnparticlepropertycontroller/inputscale.md)
  A factor for multiplying the input value of the controller’s animation.
- [var inputOrigin: SCNNode?](scnparticlepropertycontroller/inputorigin.md)
  A node whose distance to each particle provides input values for the controller’s animation.
- [var inputProperty: SCNParticleSystem.ParticleProperty?](scnparticlepropertycontroller/inputproperty.md)
  A particle property that provides input values for this property controller’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/animation)*