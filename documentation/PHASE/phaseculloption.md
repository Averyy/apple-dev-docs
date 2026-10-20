# PHASECullOption

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

The actions the engine takes when it culls sound.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum PHASECullOption
```

```c
enum PHASECullOption : NSInteger;
```

#### Overview

Culling refers to the temporary removal of a sound from the audio output. This enumeration determines the actions a sampler node performs after the engine culls its sound or queues it for culling. To indicate a preference, the app sets a sampler node’s [`cullOption`](./phasesamplernodedefinition/culloption.md) property.

## Topics

### Options
- [PHASECullOption.terminate](./phaseculloption/terminate.md)
  An option that culls sound by stopping playback.
- [PHASECullOption.doNotCull](./phaseculloption/donotcull.md)
  An option that indicates the framework takes no action to cull sound.
- [PHASECullOption.sleepWakeAtRealtimeOffset](./phaseculloption/sleepwakeatrealtimeoffset.md)
  An option that pauses playback and resumes where it left off.
- [PHASECullOption.sleepWakeAtZero](./phaseculloption/sleepwakeatzero.md)
  An option that pauses playback and resumes at the beginning.
- [PHASECullOption.sleepWakeAtRandomOffset](./phaseculloption/sleepwakeatrandomoffset.md)
  An option that pauses playback and resumes at a random position.
### Initializers
- [init?(rawValue: Int)](./phaseculloption/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Defining Cull Behavior
- [var cullOption: PHASECullOption](./phasesamplernodedefinition/culloption.md)
  The action the engine performs after it temporarily removes the node’s sound from the audio output.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseculloption)*