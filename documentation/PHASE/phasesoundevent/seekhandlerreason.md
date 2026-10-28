# PHASESoundEvent.SeekHandlerReason

**Framework**: PHASE  
**Kind**: enum  
**Role**: Enumeration

Indicates the status after a sound event changes its playback position.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
enum SeekHandlerReason
```

```c
enum PHASESoundEventSeekHandlerReason : NSInteger;
```

## Overview

When your app changes the playback position of a sound event by calling [`seek(to:completion:)`](./seek%28to,completion%29.md), the framework invokes the argument closure when the seek succeeds or fails. PHASE passes an instance of this enumeration to the closure to describe the results of the call.

## Topics

### Reasons
- [PHASESoundEvent.SeekHandlerReason.seekSuccessful](./seekhandlerreason/seeksuccessful.md)
  Indicates the sound event successfully updated its playback position.
- [PHASESoundEvent.SeekHandlerReason.failureSeekAlreadyInProgress](./seekhandlerreason/failureseekalreadyinprogress.md)
  Indicates the sound event is still updating its playback position.
- [PHASESoundEvent.SeekHandlerReason.failure](./seekhandlerreason/failure.md)
  Indicates the sound event fails to update its playback position.
### Initializers
- [init?(rawValue: Int)](./seekhandlerreason/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Seeking a Time
- [func seek(to: Double, completion: ((PHASESoundEvent.SeekHandlerReason) -> Void)?)](./seek%28to,completion%29.md)
  Advances the sound event’s playback position to a specific time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/seekhandlerreason)*