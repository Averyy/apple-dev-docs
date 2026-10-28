# imageSequenceInitialFrameVariation

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The range of randomized initial frames for particle image animation. Animatable.

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
var imageSequenceInitialFrameVariation: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat imageSequenceInitialFrameVariation;
```

## Discussion

Setting a nonzero value for this property randomizes the effect of the [`imageSequenceInitialFrame`](./imagesequenceinitialframe.md) property. SceneKit randomly adjusts the initial animation frame for each particle by up to half the [`imageSequenceInitialFrameVariation`](./imagesequenceinitialframevariation.md) value. For example, if the [`imageSequenceInitialFrame`](./imagesequenceinitialframe.md) value is `10.0` and the [`imageSequenceInitialFrameVariation`](./imagesequenceinitialframevariation.md) value is `5.0`, each particle randomly begins on a frame between frame 7.5 and frame 12.5 of the image sequence animation.

When you use image sequences for particles, SceneKit interpolates between frames of animation, so a fractional value (either for this property or for either endpoint of the range it determines) results in a partial fade between two animation frames.

The default value is `0.0` seconds, specifying no randomization.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Animating Particle Images
- [var imageSequenceRowCount: Int](./imagesequencerowcount.md)
  The number of rows for treating the particle image as a grid of animation frames.
- [var imageSequenceColumnCount: Int](./imagesequencecolumncount.md)
  The number of columns for treating the particle image as a grid of animation frames.
- [var imageSequenceInitialFrame: CGFloat](./imagesequenceinitialframe.md)
  The index of the first frame in a particle image animation. Animatable.
- [var imageSequenceFrameRate: CGFloat](./imagesequenceframerate.md)
  The rate, in frames per second, of particle image animation. Animatable.
- [var imageSequenceFrameRateVariation: CGFloat](./imagesequenceframeratevariation.md)
  The range, in frames per second, of randomized frame rates for particle image animation. Animatable.
- [var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode](./imagesequenceanimationmode.md)
  The animation mode for particle image animation.
- [enum SCNParticleImageSequenceAnimationMode](../scnparticleimagesequenceanimationmode.md)
  Options for animating each particle with a sequence of images, used by the [`imageSequenceAnimationMode`](./imagesequenceanimationmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/imagesequenceinitialframevariation)*