# PHASESoundEvent.SeekHandlerReason

**Framework**: PHASE  
**Kind**: enum

Indicates the status after a sound event changes its playback position.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum SeekHandlerReason
```

#### Overview

When your app changes the playback position of a sound event by calling [`seek(to:completion:)`](phasesoundevent/seek(to:completion:).md), the framework invokes the argument closure when the seek succeeds or fails. PHASE passes an instance of this enumeration to the closure to describe the results of the call.

## Topics

### Reasons
- [PHASESoundEvent.SeekHandlerReason.seekSuccessful](phasesoundevent/seekhandlerreason/seeksuccessful.md)
  Indicates the sound event successfully updated its playback position.
- [PHASESoundEvent.SeekHandlerReason.failureSeekAlreadyInProgress](phasesoundevent/seekhandlerreason/failureseekalreadyinprogress.md)
  Indicates the sound event is still updating its playback position.
- [PHASESoundEvent.SeekHandlerReason.failure](phasesoundevent/seekhandlerreason/failure.md)
  Indicates the sound event fails to update its playback position.
### Initializers
- [init?(rawValue: Int)](phasesoundevent/seekhandlerreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func seek(to: Double, completion: ((PHASESoundEvent.SeekHandlerReason) -> Void)?)](phasesoundevent/seek(to:completion:).md)
  Advances the sound event’s playback position to a specific time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/seekhandlerreason)*