# lastRenderTime

**Framework**: PHASE  
**Kind**: property

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
var lastRenderTime: AVAudioTime? { get }
```

#### Discussion

Obtain the time for which the engine most recently rendered.

Will return nil if the engine is not running

## See Also

- [func pause()](phaseengine/pause.md)
  Pauses all audio playback.
- [func start() throws](phaseengine/start.md)
  Starts or resumes all audio playback.
- [func stop()](phaseengine/stop.md)
  Stops all audio playback.
- [func update()](phaseengine/update.md)
  Processes app commands and increments framework processing.
- [var renderingState: PHASESoundEvent.RenderingState](phaseengine/renderingstate.md)
  The status of the engine’s audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/lastrendertime)*