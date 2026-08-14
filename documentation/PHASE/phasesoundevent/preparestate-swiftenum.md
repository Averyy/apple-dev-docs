# PHASESoundEvent.PrepareState

**Framework**: PHASE  
**Kind**: enum

Indicates the state of sound-event preparation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
enum PrepareState
```

## Topics

### States
- [PHASESoundEvent.PrepareState.prepareInProgress](phasesoundevent/preparestate-swift.enum/prepareinprogress.md)
  Indicates that the sound event prepares for playback.
- [PHASESoundEvent.PrepareState.prepareNotStarted](phasesoundevent/preparestate-swift.enum/preparenotstarted.md)
  Indicates that the sound event awaits preparation.
- [PHASESoundEvent.PrepareState.prepared](phasesoundevent/preparestate-swift.enum/prepared.md)
  Indicates that the sound event preparation is complete.
### Initializers
- [init?(rawValue: Int)](phasesoundevent/preparestate-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func prepare(completion: ((PHASESoundEvent.PrepareHandlerReason) -> Void)?)](phasesoundevent/prepare(completion:).md)
  Enables a sound event to play and runs the argument code when the sound event plays back.
- [PHASESoundEvent.PrepareHandlerReason](phasesoundevent/preparehandlerreason.md)
  Indicates the results of sound-event preparation.
- [var prepareState: PHASESoundEvent.PrepareState](phasesoundevent/preparestate-swift.property.md)
  The status of sound-event preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/preparestate-swift.enum)*