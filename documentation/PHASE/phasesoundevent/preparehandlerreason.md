# PHASESoundEvent.PrepareHandlerReason

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Indicates the results of sound-event preparation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum PrepareHandlerReason
```

```c
enum PHASESoundEventPrepareHandlerReason : NSInteger;
```

## Overview

The sound event [`prepare(completion:)`](./prepare%28completion%29.md) function passes an instance of this class to its argument completion closure to communicate the results of the call.

## Topics

### Reasons
- [PHASESoundEvent.PrepareHandlerReason.prepared](./preparehandlerreason/prepared.md)
  Indicates the completion of sound-event preparation.
- [PHASESoundEvent.PrepareHandlerReason.terminated](./preparehandlerreason/terminated.md)
  Indicates sound-event preparation stops abruptly.
- [PHASESoundEvent.PrepareHandlerReason.failure](./preparehandlerreason/failure.md)
  Indicates an error occurs during sound-event preparation.
### Initializers
- [init?(rawValue: Int)](./preparehandlerreason/init%28rawvalue%29.md)

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
- [var prepareState: PHASESoundEvent.PrepareState](./preparestate-swift.property.md)
  The status of sound-event preparation.
- [PHASESoundEvent.PrepareState](./preparestate-swift.enum.md)
  Indicates the state of sound-event preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/preparehandlerreason)*