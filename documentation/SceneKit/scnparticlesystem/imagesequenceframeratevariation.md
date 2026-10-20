# imageSequenceFrameRateVariation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The range, in frames per second, of randomized frame rates for particle image animation. Animatable.

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
var imageSequenceFrameRateVariation: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat imageSequenceFrameRateVariation;
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`imageSequenceFrameRate`](./imagesequenceframerate.md) property. SceneKit randomly adjusts the animation speed for each particle by up to half the [`imageSequenceFrameRateVariation`](./imagesequenceframeratevariation.md) value. For example, if the [`imageSequenceFrameRate`](./imagesequenceframerate.md) value is `10.0` frames per second and the [`imageSequenceFrameRateVariation`](./imagesequenceframeratevariation.md) value is `10.0` seconds, each particle animates at a random rate between `5.0` and `15.0` frames per second.

The default value is `0.0` frames per second, specifying no randomization.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Animating Particle Images
- [var imageSequenceRowCount: Int](./imagesequencerowcount.md)
  The number of rows for treating the particle image as a grid of animation frames.
- [var imageSequenceColumnCount: Int](./imagesequencecolumncount.md)
  The number of columns for treating the particle image as a grid of animation frames.
- [var imageSequenceInitialFrame: CGFloat](./imagesequenceinitialframe.md)
  The index of the first frame in a particle image animation. Animatable.
- [var imageSequenceInitialFrameVariation: CGFloat](./imagesequenceinitialframevariation.md)
  The range of randomized initial frames for particle image animation. Animatable.
- [var imageSequenceFrameRate: CGFloat](./imagesequenceframerate.md)
  The rate, in frames per second, of particle image animation. Animatable.
- [var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode](./imagesequenceanimationmode.md)
  The animation mode for particle image animation.
- [enum SCNParticleImageSequenceAnimationMode](../scnparticleimagesequenceanimationmode.md)
  Options for animating each particle with a sequence of images, used by the [`imageSequenceAnimationMode`](./imagesequenceanimationmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/imagesequenceframeratevariation)*