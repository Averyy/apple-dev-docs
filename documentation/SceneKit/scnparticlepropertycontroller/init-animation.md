# init(animation:)

**Framework**: SceneKit  
**Kind**: init

Creates a particle property controller with the specified Core Animation animation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+

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

- `animation`: SceneKit ignores the  ,  , and   properties of this animation object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/init(animation:))*