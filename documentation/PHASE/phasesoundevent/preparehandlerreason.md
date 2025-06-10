# PHASESoundEvent.PrepareHandlerReason

**Framework**: PHASE  
**Kind**: enum

Indicates the results of sound-event preparation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+

## Declaration

```swift
enum PrepareHandlerReason
```

#### Overview

The sound event [`prepare(completion:)`](phasesoundevent/prepare(completion:).md) function passes an instance of this class to its argument completion closure to communicate the results of the call.

## Topics

### Reasons
- [PHASESoundEvent.PrepareHandlerReason.prepared](phasesoundevent/preparehandlerreason/prepared.md)
  Indicates the completion of sound-event preparation.
- [PHASESoundEvent.PrepareHandlerReason.terminated](phasesoundevent/preparehandlerreason/terminated.md)
  Indicates sound-event preparation stops abruptly.
- [PHASESoundEvent.PrepareHandlerReason.failure](phasesoundevent/preparehandlerreason/failure.md)
  Indicates an error occurs during sound-event preparation.
### Initializers
- [init?(rawValue: Int)](phasesoundevent/preparehandlerreason/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func prepare(completion: ((PHASESoundEvent.PrepareHandlerReason) -> Void)?)](phasesoundevent/prepare(completion:).md)
  Enables a sound event to play and runs the argument code when the sound event plays back.
- [var prepareState: PHASESoundEvent.PrepareState](phasesoundevent/preparestate-swift.property.md)
  The status of sound-event preparation.
- [PHASESoundEvent.PrepareState](phasesoundevent/preparestate-swift.enum.md)
  Indicates the state of sound-event preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/preparehandlerreason)*