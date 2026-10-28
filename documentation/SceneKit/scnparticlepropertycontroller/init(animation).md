# init(animation:)

**Framework**: SceneKit  
**Kind**: init  
**Role**: Initializer

Creates a particle property controller with the specified Core Animation animation.

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
convenience init(animation: CAAnimation)
```

```objc
+ (instancetype) controllerWithAnimation:(CAAnimation *) animation;
```

## Return Value

A new particle property controller.

## Discussion

To set up a particle property animation:

1. Create a [`CAAnimation`](../../QuartzCore/caanimation.md) object defining how a property of each particle in the system changes over time.
2. Create a particle property controller using the [`init(animation:)`](./init%28animation%29.md) method.
3. Attach the property controller to a particle system using the [`propertyControllers`](../scnparticlesystem/propertycontrollers.md) dictionary, choosing a key listed in Particle Property Keys to identify the particle property it animates.

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

- `animation`: A Core Animation object specifying the behavior of the property animation. Must not be nil.

  You can use different [`CAAnimation`](../../QuartzCore/caanimation.md) subclasses to animate effects in different ways. For example, a [`CABasicAnimation`](../../QuartzCore/cabasicanimation.md) instance transitions a property from one value to another, and a [`CAKeyframeAnimation`](../../QuartzCore/cakeyframeanimation.md) instance transitions a property through a series of values. You use properties of the animation object to define its timing curve, repeat mode, and other options.

  SceneKit ignores the [`keyPath`](../../QuartzCore/capropertyanimation/keypath.md), [`duration`](../../QuartzCore/camediatiming/duration.md), and [`repeatCount`](../../QuartzCore/camediatiming/repeatcount.md) properties of this animation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/init(animation:))*