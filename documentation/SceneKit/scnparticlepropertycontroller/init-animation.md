# init(animation:)

**Framework**: SceneKit  
**Kind**: init

Creates a particle property controller with the specified Core Animation animation.

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
convenience init(animation: CAAnimation)
```

#### Return Value

A new particle property controller.

#### Discussion

To set up a particle property animation:

1. Create a [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation) object defining how a property of each particle in the system changes over time.
2. Create a particle property controller using the [`init(animation:)`](scnparticlepropertycontroller/init(animation:).md) method.
3. Attach the property controller to a particle system using the [`propertyControllers`](scnparticlesystem/propertycontrollers.md) dictionary, choosing a key listed in Particle Property Keys to identify the particle property it animates.

For example, the following code sets up a controller to animate particle sizes:

```objc
// 1. Create and configure an animation object.
CAKeyframeAnimation *animation = [CAKeyframeAnimation animation];
animation.values = @[ @0.1, @1.0, @3.0, @0.5 ];
 
// 2. Create a property controller from the animation object.
SCNParticlePropertyController *controller =
    [SCNParticlePropertyController controllerWithAnimation:animation];
 
// 3. Assign the controller to a particle system, associating it with a particle property.
particleSystem.propertyControllers = @{ SCNParticlePropertySize: controller };
```

## Parameters

- `animation`: A Core Animation object specifying the behavior of the property animation. Must not be nil. You can use different [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation) subclasses to animate effects in different ways. For example, a [`CABasicAnimation`](https://developer.apple.com/documentation/QuartzCore/CABasicAnimation) instance transitions a property from one value to another, and a [`CAKeyframeAnimation`](https://developer.apple.com/documentation/QuartzCore/CAKeyframeAnimation) instance transitions a property through a series of values. You use properties of the animation object to define its timing curve, repeat mode, and other options. SceneKit ignores the [`keyPath`](https://developer.apple.com/documentation/QuartzCore/CAPropertyAnimation/keyPath), [`duration`](https://developer.apple.com/documentation/QuartzCore/CAMediaTiming/duration), and [`repeatCount`](https://developer.apple.com/documentation/QuartzCore/CAMediaTiming/repeatCount) properties of this animation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/init(animation:))*