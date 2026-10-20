# renderingState

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) PHASERenderingState renderingState;
```

#### Discussion

Access this property to check the sound event’s playback status. The value reflects the state you control by calling one of the functions: [`start(completion:)`](./start%28completion%29.md), [`stopAndInvalidate()`](./stopandinvalidate%28%29.md), or [`pause()`](./pause%28%29.md).

## See Also

### Checking Playback Status
- [PHASESoundEvent.RenderingState](./renderingstate-swift.enum.md)
  The playback status of audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasesoundevent/renderingstate-swift.property)*