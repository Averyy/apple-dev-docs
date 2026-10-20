# PHASESoundEvent.StartHandlerReason

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Indicates the status after starting a sound event.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum StartHandlerReason
```

```c
enum PHASESoundEventStartHandlerReason : NSInteger;
```

#### Overview

When your app starts a sound event by calling [`start(completion:)`](./start%28completion%29.md), the framework invokes the argument closure when starting succeeds or fails. PHASE passes an instance of this enumeration to the closure to describe the results of the call.

## Topics

### Reasons
- [PHASESoundEvent.StartHandlerReason.finishedPlaying](./starthandlerreason/finishedplaying.md)
  Indicates the framework successfully started the sound event.
- [PHASESoundEvent.StartHandlerReason.terminated](./starthandlerreason/terminated.md)
  Indicates the framework terminated the sound event abruptly.
- [PHASESoundEvent.StartHandlerReason.failure](./starthandlerreason/failure.md)
  Indicates an error occurred while starting the sound event.
### Initializers
- [init?(rawValue: Int)](./starthandlerreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Starting Playback
- [func start(completion: ((PHASESoundEvent.StartHandlerReason) -> Void)?)](./start%28completion%29.md)
  Invokes the sound event and runs the specified code on completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/starthandlerreason)*