# renderingState

**Framework**: PHASE  
**Kind**: property

The status of the engine’s audio playback.

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

Access this property to check the engine’s playback status. The value reflects the state that you control by calling one of the functions: [`start()`](phaseengine/start().md), [`stop()`](phaseengine/stop().md), or [`pause()`](phaseengine/pause().md).

## See Also

- [func pause()](phaseengine/pause.md)
  Pauses all audio playback.
- [func start() throws](phaseengine/start.md)
  Starts or resumes all audio playback.
- [func stop()](phaseengine/stop.md)
  Stops all audio playback.
- [func update()](phaseengine/update.md)
  Processes app commands and increments framework processing.
- [var lastRenderTime: AVAudioTime?](phaseengine/lastrendertime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/renderingstate)*