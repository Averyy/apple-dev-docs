# start()

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Starts or resumes all audio playback.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func start() throws
```

```objc
- (BOOL) startAndReturnError:(NSError **) error;
```

## Discussion

This function throws an error if the framework fails to start the engine.

## See Also

### Controlling and Inspecting Playback State
- [func pause()](./pause%28%29.md)
  Pauses all audio playback.
- [func stop()](./stop%28%29.md)
  Stops all audio playback.
- [func update()](./update%28%29.md)
  Processes app commands and increments framework processing.
- [var renderingState: PHASESoundEvent.RenderingState](./renderingstate.md)
  The status of the engine’s audio playback.
- [var lastRenderTime: AVAudioTime?](./lastrendertime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/start())*