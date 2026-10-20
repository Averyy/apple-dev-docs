# pause()

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) pause;
```

#### Discussion

To resume paused playback, call [`start()`](./start%28%29.md).

## See Also

### Controlling and Inspecting Playback State
- [func start() throws](./start%28%29.md)
  Starts or resumes all audio playback.
- [func stop()](./stop%28%29.md)
  Stops all audio playback.
- [func update()](./update%28%29.md)
  Processes app commands and increments framework processing.
- [var renderingState: PHASESoundEvent.RenderingState](./renderingstate.md)
  The status of the engine’s audio playback.
- [var lastRenderTime: AVAudioTime?](./lastrendertime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/pause())*