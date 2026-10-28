# imageSequenceFrameRate

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The rate, in frames per second, of particle image animation. Animatable.

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
var imageSequenceFrameRate: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat imageSequenceFrameRate;
```

## Discussion

To specify a sequence of frames for animating each particle, arrange the frames as a grid in a single image, as shown in [Figure 1](./particleimage.md#1965925). Then use the [`imageSequenceRowCount`](./imagesequencerowcount.md) and [`imageSequenceColumnCount`](./imagesequencecolumncount.md) properties to specify the arrangement of frames in the images, and this property to define animation speed.

The default value is `0.0` frames per second, specifying no animation.

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
- [var imageSequenceFrameRateVariation: CGFloat](./imagesequenceframeratevariation.md)
  The range, in frames per second, of randomized frame rates for particle image animation. Animatable.
- [var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode](./imagesequenceanimationmode.md)
  The animation mode for particle image animation.
- [enum SCNParticleImageSequenceAnimationMode](../scnparticleimagesequenceanimationmode.md)
  Options for animating each particle with a sequence of images, used by the [`imageSequenceAnimationMode`](./imagesequenceanimationmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/imagesequenceframerate)*