# imageSequenceInitialFrame

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The index of the first frame in a particle image animation. Animatable.

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
var imageSequenceInitialFrame: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat imageSequenceInitialFrame;
```

#### Discussion

To specify a sequence of frames for animating each particle, arrange the frames as a grid in a single image, as shown in [Figure 1](./api-1524153-particleimage.md#1965925). The total number of frames in an image sequence is the product of multiplying the [`imageSequenceRowCount`](./imagesequencerowcount.md) and [`imageSequenceColumnCount`](./imagesequencecolumncount.md) properties. Frames are numbered starting at zero, indicating the top left image in the grid.

When you use image sequences for particles, SceneKit interpolates between frames of animation, so a fractional value specifies a partial fade between two animation frames.

The default value is `0.0`, specifying that animation begins with the top left image in the grid.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Animating Particle Images
- [var imageSequenceRowCount: Int](./imagesequencerowcount.md)
  The number of rows for treating the particle image as a grid of animation frames.
- [var imageSequenceColumnCount: Int](./imagesequencecolumncount.md)
  The number of columns for treating the particle image as a grid of animation frames.
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

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/imagesequenceinitialframe)*