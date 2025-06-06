# imageSequenceFrameRate

**Framework**: SceneKit  
**Kind**: property

The rate, in frames per second, of particle image animation. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var imageSequenceFrameRate: CGFloat { get set }
```

#### Discussion

To specify a sequence of frames for animating each particle, arrange the frames as a grid in a single image, as shown in [`Figure 1`](scnparticlesystem/1524153-particleimage#1965925.md). Then use the [`imageSequenceRowCount`](scnparticlesystem/imagesequencerowcount.md) and [`imageSequenceColumnCount`](scnparticlesystem/imagesequencecolumncount.md) properties to specify the arrangement of frames in the images, and this property to define animation speed.

The default value is `0.0` frames per second, specifying no animation.

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
- [var imageSequenceFrameRateVariation: CGFloat](scnparticlesystem/imagesequenceframeratevariation.md)
  The range, in frames per second, of randomized frame rates for particle image animation. Animatable.
- [var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode](scnparticlesystem/imagesequenceanimationmode.md)
  The animation mode for particle image animation.
- [enum SCNParticleImageSequenceAnimationMode](scnparticleimagesequenceanimationmode.md)
  Options for animating each particle with a sequence of images, used by the [`imageSequenceAnimationMode`](scnparticlesystem/imagesequenceanimationmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/imagesequenceframerate)*