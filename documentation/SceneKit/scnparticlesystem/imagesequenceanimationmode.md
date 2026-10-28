# imageSequenceAnimationMode

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The animation mode for particle image animation.

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
var imageSequenceAnimationMode: SCNParticleImageSequenceAnimationMode { get set }
```

```objc
@property (nonatomic) SCNParticleImageSequenceAnimationMode imageSequenceAnimationMode;
```

## Discussion

The default value is [`SCNParticleImageSequenceAnimationMode.repeat`](../scnparticleimagesequenceanimationmode/repeat.md), indicating that the image sequence loops continuously. For details on other values, see [`SCNParticleImageSequenceAnimationMode`](../scnparticleimagesequenceanimationmode.md).

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
- [var imageSequenceFrameRateVariation: CGFloat](./imagesequenceframeratevariation.md)
  The range, in frames per second, of randomized frame rates for particle image animation. Animatable.
- [enum SCNParticleImageSequenceAnimationMode](../scnparticleimagesequenceanimationmode.md)
  Options for animating each particle with a sequence of images, used by the [`imageSequenceAnimationMode`](./imagesequenceanimationmode.md) property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticlesystem/imagesequenceanimationmode)*