# imageSequenceFrameRateVariation

**Framework**: SceneKit  
**Kind**: property

The range, in frames per second, of randomized frame rates for particle image animation. Animatable.

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
var imageSequenceFrameRateVariation: CGFloat { get set }
```

#### Discussion

Setting a nonzero value for this property randomizes the effect of the [`imageSequenceFrameRate`](scnparticlesystem/imagesequenceframerate.md) property. SceneKit randomly adjusts the animation speed for each particle by up to half the [`imageSequenceFrameRateVariation`](scnparticlesystem/imagesequenceframeratevariation.md) value. For example, if the [`imageSequenceFrameRate`](scnparticlesystem/imagesequenceframerate.md) value is `10.0` frames per second and the [`imageSequenceFrameRateVariation`](scnparticlesystem/imagesequenceframeratevariation.md) value is `10.0` seconds, each particle animates at a random rate between `5.0` and `15.0` frames per second.

The default value is `0.0` frames per second, specifying no randomization.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var imageSequenceRowCount: Int](scnparticlesystem/imagesequencerowcount.md)
  The number of rows for treating the particle image as a grid of animation frames.
- [var imageSequenceColumnCount: Int](scnparticlesystem/imagesequencecolumncount.md)
  The number of columns for treating the particle image as a grid of animation frames.
- [var imageSequenceInitialFrame: CGFloat](scnparticlesystem/imagesequenceinitialframe.md)
  The index of the first frame in a particle image animation. Animatable.
- [var imageSequenceInitialFrameVariation: CGFloat](scnparticlesystem/imagesequenceinitialframevariation.md)
  The range of randomized initial frames for particle image animation. Animatable.
- [var imageSequenceFrameRate: CGFloat](scnparticlesystem/imagesequenceframerate.md)
  The rate, in frames per second, of particle image animation. Animatable.
- [var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode](scnparticlesystem/imagesequenceanimationmode.md)
  The animation mode for particle image animation.
- [enum SCNParticleImageSequenceAnimationMode](scnparticleimagesequenceanimationmode.md)
  Options for animating each particle with a sequence of images, used by the [`imageSequenceAnimationMode`](scnparticlesystem/imagesequenceanimationmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/imagesequenceframeratevariation)*