# inputProperty

**Framework**: SceneKit  
**Kind**: property

A particle property that provides input values for this property controller’s animation.

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
var inputProperty: SCNParticleSystem.ParticleProperty? { get set }
```

#### Discussion

This property applies only when the controller’s [`inputMode`](scnparticlepropertycontroller/inputmode.md) value is [`SCNParticleInputMode.overOtherProperty`](scnparticleinputmode/overotherproperty.md).

Use this option to animate one property in response to changes in one of each particle’s other properties. For example, the following code animates particles’ size as a function of their velocity, causing particles to become larger when they move faster:

```objc
CABasicAnimation *animation = [CABasicAnimation animation];
animation.fromValue = @0.1;
animation.toValue = @10.0;
 
SCNParticlePropertyController *sizeController =
    [SCNParticlePropertyController controllerWithAnimation:animation];
sizeController.inputMode = SCNParticleInputModeOverOtherProperty;
sizeController.inputProperty = SCNParticlePropertyVelocity;
sizeController.inputScale = 0.1;
 
particleSystem.propertyControllers = @{ SCNParticlePropertySize : sizeController };
```

To refine the relationship between a range of property values and a range of input values for the controller’s animation, use the [`inputBias`](scnparticlepropertycontroller/inputbias.md) and [`inputScale`](scnparticlepropertycontroller/inputscale.md) properties.

If you specify a vector property (such as acceleration) as the input property, SceneKit uses that vector’s length for the input value.

## See Also

- [var animation: CAAnimation](scnparticlepropertycontroller/animation.md)
  The Core Animation object defining the behavior of the property animation.
- [var inputMode: SCNParticleInputMode](scnparticlepropertycontroller/inputmode.md)
  The mode that determines input values for the property controller’s animation.
- [var inputBias: CGFloat](scnparticlepropertycontroller/inputbias.md)
  An offset to add to the input value of the controller’s animation.
- [var inputScale: CGFloat](scnparticlepropertycontroller/inputscale.md)
  A factor for multiplying the input value of the controller’s animation.
- [var inputOrigin: SCNNode?](scnparticlepropertycontroller/inputorigin.md)
  A node whose distance to each particle provides input values for the controller’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/inputproperty)*