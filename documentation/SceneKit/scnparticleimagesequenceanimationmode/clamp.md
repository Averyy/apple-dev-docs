# SCNParticleImageSequenceAnimationMode.clamp

**Framework**: SceneKit  
**Kind**: case  
**Role**: Case

The animation stops after displaying all of its images.

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
case clamp
```

```c
SCNParticleImageSequenceAnimationModeClamp
```

#### Discussion

After animation ends, the particle continues to display the last image of the sequence. (Or the first, if the animation is playing in reverse.)

## See Also

### Constants
- [SCNParticleImageSequenceAnimationMode.repeat](./repeat.md)
  The animation loops after displaying all of its images.
- [SCNParticleImageSequenceAnimationMode.autoReverse](./autoreverse.md)
  After the animation displays all of its images, it plays again in reverse order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleimagesequenceanimationmode/clamp)*