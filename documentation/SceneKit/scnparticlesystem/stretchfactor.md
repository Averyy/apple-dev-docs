# stretchFactor

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

A multiplier for stretching particle images along their direction of motion. Animatable.

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
var stretchFactor: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat stretchFactor;
```

#### Discussion

Use this property to create visual effects that show streaks of motion, such as fireworks. If the [`orientationMode`](./orientationmode.md) property value is [`SCNParticleOrientationMode.free`](../scnparticleorientationmode/free.md), a non-default stretch factor stretches particle images in the y-axis direction of each particle’s local coordinate space.

The default value is `0.0`, specifying that particle images maintain their original aspect ratio.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Specifying Particle Appearance
- [var particleSize: CGFloat](./particlesize.md)
  The rendered size, in units of the scene’s world coordinate space, of the particle image. Animatable.
- [var particleSizeVariation: CGFloat](./particlesizevariation.md)
  The range of randomized particle sizes. Animatable.
- [var particleColor: UIColor](./particlecolor.md)
  The color of newly spawned particles. Animatable.
- [var particleColorVariation: SCNVector4](./particlecolorvariation.md)
  The ranges of randomized particle color components. Animatable.
- [var particleImage: Any?](./particleimage.md)
  The texture image SceneKit uses to render each particle.
- [var fresnelExponent: CGFloat](./fresnelexponent.md)
  The reflectivity exponent SceneKit uses when rendering the particle’s image as a cube map. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/stretchfactor)*