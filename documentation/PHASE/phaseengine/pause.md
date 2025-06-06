# pause()

**Framework**: PHASE  
**Kind**: method

Pauses all audio playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func pause()
```

#### Discussion

To resume paused playback, call [`start()`](phaseengine/start().md).

## See Also

- [func start() throws](phaseengine/start.md)
  Starts or resumes all audio playback.
- [func stop()](phaseengine/stop.md)
  Stops all audio playback.
- [func update()](phaseengine/update.md)
  Processes app commands and increments framework processing.
- [var renderingState: PHASESoundEvent.RenderingState](phaseengine/renderingstate.md)
  The status of the engine’s audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/pause())*