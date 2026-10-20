# inputScale

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A factor for multiplying the input value of the controller’s animation.

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
var inputScale: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat inputScale;
```

#### Discussion

Use this property and the [`inputBias`](./inputbias.md) property to pre-process input values to the controller’s animation. For example, you use the [`SCNParticleInputMode.overDistance`](../scnparticleinputmode/overdistance.md) option to animate a particle’s opacity as a function of its distance from a specified point, a scale specifies the range of distances over which the animation takes effect.

The default value is `1.0`, leaving the input value to the animation unchanged. The range of possible values depends on the controller’s animation.

## See Also

### Managing the Controller’s Animation
- [var animation: CAAnimation](./animation.md)
  The Core Animation object defining the behavior of the property animation.
- [var inputMode: SCNParticleInputMode](./inputmode.md)
  The mode that determines input values for the property controller’s animation.
- [var inputBias: CGFloat](./inputbias.md)
  An offset to add to the input value of the controller’s animation.
- [var inputOrigin: SCNNode?](./inputorigin.md)
  A node whose distance to each particle provides input values for the controller’s animation.
- [var inputProperty: SCNParticleSystem.ParticleProperty?](./inputproperty.md)
  A particle property that provides input values for this property controller’s animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlepropertycontroller/inputscale)*