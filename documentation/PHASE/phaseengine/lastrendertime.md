# lastRenderTime

**Framework**: PHASE  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly, nullable) AVAudioTime * lastRenderTime;
```

#### Discussion

Obtain the time for which the engine most recently rendered.

Will return nil if the engine is not running

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
- [var renderingState: PHASESoundEvent.RenderingState](./renderingstate.md)
  The status of the engine’s audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/lastrendertime)*