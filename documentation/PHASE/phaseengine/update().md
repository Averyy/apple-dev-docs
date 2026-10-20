# update()

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Processes app commands and increments framework processing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func update()
```

```objc
- (void) update;
```

#### Discussion

This function consumes the app’s API calls since the last [`update()`](./update%28%29.md), adjusts internal systems, objects, increments parameters, and invokes the app’s queued callbacks. An API call may require several [`update()`](./update%28%29.md) invocations before the output device reflects the call’s results.

The framework ignores calls to this function for engines with `updateMode` set to [`PHASEEngine.UpdateMode.automatic`](./updatemode/automatic.md); for more more information, see [`init(updateMode:)`](./init%28updatemode%29.md).

> **Note**:  The frequency that the app calls this function doesn’t change the speed by which PHASE plays audio in real time.

##### Update an Engine Manually

On an engine configured for manual updates ([`PHASEEngine.UpdateMode.manual`](./updatemode/manual.md)), call this function periodically to instruct the framework to process API calls and perform internal updates. Call [`update()`](./update%28%29.md) at a rate that matches your app’s visuals or logic update rate for optimal performance:

- Apps that process graphics at 60 FPS can invoke [`update()`](./update%28%29.md) in their display link callback.
- Rates in the range of 240Hz to 30Hz offer equivalent audio performance, however apps that actively change the parameters of playing audio achieve smoother interpolation at a higher rate.
- If a game skips frames due to long running graphics routines, an app can throttle [`update()`](./update%28%29.md) calls to values less than 30Hz without affecting audio quality as long as the system isn’t overloaded.

This function offers thread safety for apps that intend to call [`update()`](./update%28%29.md) off of the main thread.

## See Also

### Controlling and Inspecting Playback State
- [func pause()](./pause%28%29.md)
  Pauses all audio playback.
- [func start() throws](./start%28%29.md)
  Starts or resumes all audio playback.
- [func stop()](./stop%28%29.md)
  Stops all audio playback.
- [var renderingState: PHASESoundEvent.RenderingState](./renderingstate.md)
  The status of the engine’s audio playback.
- [var lastRenderTime: AVAudioTime?](./lastrendertime.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/update())*