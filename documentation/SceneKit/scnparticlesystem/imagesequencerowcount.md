# imageSequenceRowCount

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of rows for treating the particle image as a grid of animation frames.

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
var imageSequenceRowCount: Int { get set }
```

```objc
@property (nonatomic) NSUInteger imageSequenceRowCount;
```

#### Discussion

To specify a sequence of frames for animating each particle, arrange the frames as a grid in a single image, as shown in [Figure 1](./api-1524153-particleimage.md#1965925). Then use this property and the [`imageSequenceColumnCount`](./imagesequencecolumncount.md) property to specify the arrangement of frames in the image, and the [`imageSequenceInitialFrame`](./imagesequenceinitialframe.md) and [`imageSequenceFrameRate`](./imagesequenceframerate.md) properties to define animation timing.

The default value is `1`. If the [`imageSequenceColumnCount`](./imagesequencecolumncount.md) value is also `1` (the default), this specifies no animation for particle images.

## See Also

### Animating Particle Images
- [var imageSequenceColumnCount: Int](./imagesequencecolumncount.md)
  The number of columns for treating the particle image as a grid of animation frames.
- [var imageSequenceInitialFrame: CGFloat](./imagesequenceinitialframe.md)
  The index of the first frame in a particle image animation. Animatable.
- [var imageSequenceInitialFrameVariation: CGFloat](./imagesequenceinitialframevariation.md)
  The range of randomized initial frames for particle image animation. Animatable.
- [var imageSequenceFrameRate: CGFloat](./imagesequenceframerate.md)
  The rate, in frames per second, of particle image animation. Animatable.
- [var imageSequenceFrameRateVariation: CGFloat](./imagesequenceframeratevariation.md)
  The range, in frames per second, of randomized frame rates for particle image animation. Animatable.
- [var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode](./imagesequenceanimationmode.md)
  The animation mode for particle image animation.
- [enum SCNParticleImageSequenceAnimationMode](../scnparticleimagesequenceanimationmode.md)
  Options for animating each particle with a sequence of images, used by the [`imageSequenceAnimationMode`](./imagesequenceanimationmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/imagesequencerowcount)*