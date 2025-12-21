# ParticleEmitterComponent.ParticleEmitter.ImageSequence

**Framework**: RealityKit  
**Kind**: struct

Structure used to define properties of the sprite sheet, used by imageSequence.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageSequence
```

## Topics

### Initializers
- [init()](particleemittercomponent/particleemitter/imagesequence-swift.struct/init.md)
### Instance Properties
- [var animationMode: ParticleEmitterComponent.ParticleEmitter.ImageSequence.AnimationRepeatMode](particleemittercomponent/particleemitter/imagesequence-swift.struct/animationmode.md)
  How the effect timeline is played.
- [var columnCount: Int](particleemittercomponent/particleemitter/imagesequence-swift.struct/columncount.md)
  Number of columns in the sprite sheet.
- [var frameRate: Float](particleemittercomponent/particleemitter/imagesequence-swift.struct/framerate.md)
  Number of sprite sheet frames to play per second.
- [var frameRateVariation: Float](particleemittercomponent/particleemitter/imagesequence-swift.struct/frameratevariation.md)
  Defines a plus/minus range (in frames per second) from which a value is randomly selected to offset `frameRate`.
- [var initialFrame: Int](particleemittercomponent/particleemitter/imagesequence-swift.struct/initialframe.md)
  First frame of the sprite sheet animation.
- [var initialFrameVariation: Int](particleemittercomponent/particleemitter/imagesequence-swift.struct/initialframevariation.md)
  Defines a plus/minus range (in frames) from which a value is randomly selected to offset `initialFrame`.
- [var rowCount: Int](particleemittercomponent/particleemitter/imagesequence-swift.struct/rowcount.md)
  Number of rows in the sprite sheet.
### Enumerations
- [ParticleEmitterComponent.ParticleEmitter.ImageSequence.AnimationRepeatMode](particleemittercomponent/particleemitter/imagesequence-swift.struct/animationrepeatmode.md)
  Options for how the effect timeline is played, used by the animationMode property.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/particleemittercomponent/particleemitter/imagesequence-swift.struct)*