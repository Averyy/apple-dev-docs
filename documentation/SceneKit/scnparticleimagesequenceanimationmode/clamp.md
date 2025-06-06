# SCNParticleImageSequenceAnimationMode.clamp

**Framework**: SceneKit  
**Kind**: case

The animation stops after displaying all of its images.

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
case clamp
```

#### Discussion

After animation ends, the particle continues to display the last image of the sequence. (Or the first, if the animation is playing in reverse.)

## See Also

- [SCNParticleImageSequenceAnimationMode.repeat](scnparticleimagesequenceanimationmode/repeat.md)
  The animation loops after displaying all of its images.
- [SCNParticleImageSequenceAnimationMode.autoReverse](scnparticleimagesequenceanimationmode/autoreverse.md)
  After the animation displays all of its images, it plays again in reverse order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnparticleimagesequenceanimationmode/clamp)*