# renderingState

**Framework**: PHASE  
**Kind**: property

The sound event’s playback status.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
var renderingState: PHASESoundEvent.RenderingState { get }
```

#### Discussion

Access this property to check the sound event’s playback status. The value reflects the state you control by calling one of the functions: [`start(completion:)`](phasesoundevent/start(completion:).md), [`stopAndInvalidate()`](phasesoundevent/stopandinvalidate().md), or [`pause()`](phasesoundevent/pause().md).

## See Also

- [PHASESoundEvent.RenderingState](phasesoundevent/renderingstate-swift.enum.md)
  The playback status of audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/renderingstate-swift.property)*