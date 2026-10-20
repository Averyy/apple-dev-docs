# prepareState

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

The status of sound-event preparation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var prepareState: PHASESoundEvent.PrepareState { get }
```

```objc
@property (readonly) PHASESoundEventPrepareState prepareState;
```

## See Also

### Preparing Playback
- [func prepare(completion: ((PHASESoundEvent.PrepareHandlerReason) -> Void)?)](./prepare%28completion%29.md)
  Enables a sound event to play and runs the argument code when the sound event plays back.
- [PHASESoundEvent.PrepareHandlerReason](./preparehandlerreason.md)
  Indicates the results of sound-event preparation.
- [PHASESoundEvent.PrepareState](./preparestate-swift.enum.md)
  Indicates the state of sound-event preparation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/preparestate-swift.property)*