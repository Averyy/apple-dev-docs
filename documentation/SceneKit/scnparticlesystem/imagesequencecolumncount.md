# imageSequenceColumnCount

**Framework**: SceneKit  
**Kind**: property

The number of columns for treating the particle image as a grid of animation frames.

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
var imageSequenceColumnCount: Int { get set }
```

#### Discussion

To specify a sequence of frames for animating each particle, arrange the frames as a grid in a single image, as shown in [`Figure 1`](scnparticlesystem/1524153-particleimage#1965925.md). Then use this property and the [`imageSequenceRowCount`](scnparticlesystem/imagesequencerowcount.md) property to specify the arrangement of frames in the image, and the [`imageSequenceInitialFrame`](scnparticlesystem/imagesequenceinitialframe.md) and [`imageSequenceFrameRate`](scnparticlesystem/imagesequenceframerate.md) properties to define animation timing.

The default value is `1`. If the [`imageSequenceRowCount`](scnparticlesystem/imagesequencerowcount.md) value is also `1` (the default), this specifies no animation for particle images.

## See Also

- [var imageSequenceRowCount: Int](scnparticlesystem/imagesequencerowcount.md)
  The number of rows for treating the particle image as a grid of animation frames.
- [var imageSequenceInitialFrame: CGFloat](scnparticlesystem/imagesequenceinitialframe.md)
  The index of the first frame in a particle image animation. Animatable.
- [var imageSequenceInitialFrameVariation: CGFloat](scnparticlesystem/imagesequenceinitialframevariation.md)
  The range of randomized initial frames for particle image animation. Animatable.
- [var imageSequenceFrameRate: CGFloat](scnparticlesystem/imagesequenceframerate.md)
  The rate, in frames per second, of particle image animation. Animatable.
- [var imageSequenceFrameRateVariation: CGFloat](scnparticlesystem/imagesequenceframeratevariation.md)
  The range, in frames per second, of randomized frame rates for particle image animation. Animatable.
- [var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode](scnparticlesystem/imagesequenceanimationmode.md)
  The animation mode for particle image animation.
- [enum SCNParticleImageSequenceAnimationMode](scnparticleimagesequenceanimationmode.md)
  Options for animating each particle with a sequence of images, used by the [`imageSequenceAnimationMode`](scnparticlesystem/imagesequenceanimationmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/imagesequencecolumncount)*