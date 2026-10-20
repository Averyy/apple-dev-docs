# renderingState

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) PHASERenderingState renderingState;
```

#### Discussion

Access this property to check the engine’s playback status. The value reflects the state that you control by calling one of the functions: [`start()`](./start%28%29.md), [`stop()`](./stop%28%29.md), or [`pause()`](./pause%28%29.md).

## See Also

### Controlling and Inspecting Playback State
- [func pause()](./pause%28%29.md)
  Pauses all audio playback.
- [func start() throws](./start%28%29.md)
  Starts or resumes all audio playback.
- [func stop()](./stop%28%29.md)
  Stops all audio playback.
- [func update()](./update%28%29.md)
  Processes app commands and increments framework processing.
- [var lastRenderTime: AVAudioTime?](./lastrendertime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/renderingstate)*