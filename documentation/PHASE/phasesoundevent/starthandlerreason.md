# PHASESoundEvent.StartHandlerReason

**Framework**: PHASE  
**Kind**: enum

Indicates the status after starting a sound event.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum StartHandlerReason
```

#### Overview

When your app starts a sound event by calling [`start(completion:)`](phasesoundevent/start(completion:).md), the framework invokes the argument closure when starting succeeds or fails. PHASE passes an instance of this enumeration to the closure to describe the results of the call.

## Topics

### Reasons
- [PHASESoundEvent.StartHandlerReason.finishedPlaying](phasesoundevent/starthandlerreason/finishedplaying.md)
  Indicates the framework successfully started the sound event.
- [PHASESoundEvent.StartHandlerReason.terminated](phasesoundevent/starthandlerreason/terminated.md)
  Indicates the framework terminated the sound event abruptly.
- [PHASESoundEvent.StartHandlerReason.failure](phasesoundevent/starthandlerreason/failure.md)
  Indicates an error occurred while starting the sound event.
### Initializers
- [init?(rawValue: Int)](phasesoundevent/starthandlerreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func start(completion: ((PHASESoundEvent.StartHandlerReason) -> Void)?)](phasesoundevent/start(completion:).md)
  Invokes the sound event and runs the specified code on completion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/starthandlerreason)*