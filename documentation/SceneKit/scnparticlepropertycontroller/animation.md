# animation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The Core Animation object defining the behavior of the property animation.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var animation: CAAnimation { get set }
```

```objc
@property (nonatomic, retain) CAAnimation * animation;
```

## Discussion

You can use different [`CAAnimation`](../../QuartzCore/caanimation.md) subclasses to animate effects in different ways. For example, a [`CABasicAnimation`](../../QuartzCore/cabasicanimation.md) transitions a property from one value to another, and a [`CAKeyframeAnimation`](../../QuartzCore/cakeyframeanimation.md) transitions a property through a series of values. You use properties of the animation object to define its timing curve, repeat mode, and other options.

SceneKit ignores the [`keyPath`](../../QuartzCore/capropertyanimation/keypath.md) property of this animation object. Instead, when you attach a property controller to a particle system’s [`propertyControllers`](../scnparticlesystem/propertycontrollers.md) dictionary, use one of the keys listed in Particle Property Keys to specify which particle property it animates. SceneKit also ignores the animation’s [`duration`](../../QuartzCore/camediatiming/duration.md) and [`repeatCount`](../../QuartzCore/camediatiming/repeatcount.md) properties. Instead, the controller defines the behavior of the animation’s input value.

## See Also

### Managing the Controller’s Animation
- [var inputMode: SCNParticleInputMode](./inputmode.md)
  The mode that determines input values for the property controller’s animation.
- [var inputBias: CGFloat](./inputbias.md)
  An offset to add to the input value of the controller’s animation.
- [var inputScale: CGFloat](./inputscale.md)
  A factor for multiplying the input value of the controller’s animation.
- [var inputOrigin: SCNNode?](./inputorigin.md)
  A node whose distance to each particle provides input values for the controller’s animation.
- [var inputProperty: SCNParticleSystem.ParticleProperty?](./inputproperty.md)
  A particle property that provides input values for this property controller’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/animation)*