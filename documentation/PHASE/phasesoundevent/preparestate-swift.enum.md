# PHASESoundEvent.PrepareState

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Indicates the state of sound-event preparation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum PrepareState
```

```c
enum PHASESoundEventPrepareState : NSInteger;
```

## Topics

### States
- [PHASESoundEvent.PrepareState.prepareInProgress](./preparestate-swift.enum/prepareinprogress.md)
  Indicates that the sound event prepares for playback.
- [PHASESoundEvent.PrepareState.prepareNotStarted](./preparestate-swift.enum/preparenotstarted.md)
  Indicates that the sound event awaits preparation.
- [PHASESoundEvent.PrepareState.prepared](./preparestate-swift.enum/prepared.md)
  Indicates that the sound event preparation is complete.
### Initializers
- [init?(rawValue: Int)](./preparestate-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Preparing Playback
- [func prepare(completion: ((PHASESoundEvent.PrepareHandlerReason) -> Void)?)](./prepare%28completion%29.md)
  Enables a sound event to play and runs the argument code when the sound event plays back.
- [PHASESoundEvent.PrepareHandlerReason](./preparehandlerreason.md)
  Indicates the results of sound-event preparation.
- [var prepareState: PHASESoundEvent.PrepareState](./preparestate-swift.property.md)
  The status of sound-event preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/preparestate-swift.enum)*