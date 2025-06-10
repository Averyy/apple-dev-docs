# SCNParticleImageSequenceAnimationMode

**Framework**: SceneKit  
**Kind**: enum

Options for animating each particle with a sequence of images, used by the [`imageSequenceAnimationMode`](scnparticlesystem/imagesequenceanimationmode.md) property.

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
enum SCNParticleImageSequenceAnimationMode
```

## Topics

### Constants
- [SCNParticleImageSequenceAnimationMode.repeat](scnparticleimagesequenceanimationmode/repeat.md)
  The animation loops after displaying all of its images.
- [SCNParticleImageSequenceAnimationMode.clamp](scnparticleimagesequenceanimationmode/clamp.md)
  The animation stops after displaying all of its images.
- [SCNParticleImageSequenceAnimationMode.autoReverse](scnparticleimagesequenceanimationmode/autoreverse.md)
  After the animation displays all of its images, it plays again in reverse order.
### Initializers
- [init?(rawValue: Int)](scnparticleimagesequenceanimationmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var imageSequenceFrameRateVariation: CGFloat](scnparticlesystem/imagesequenceframeratevariation.md)
  The range, in frames per second, of randomized frame rates for particle image animation. Animatable.
- [var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode](scnparticlesystem/imagesequenceanimationmode.md)
  The animation mode for particle image animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleimagesequenceanimationmode)*