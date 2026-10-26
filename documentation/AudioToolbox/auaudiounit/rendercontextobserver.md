# renderContextObserver

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The block that the system calls when the rendering context changes.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```objc
@property (nonatomic, readonly) AURenderContextObserver renderContextObserver;
```

#### Discussion

Implement this property if your Audio Unit creates auxilliary realtime rendering threads. Return a block for the system to call when the rendering context changes.

> ❗ **Important**:  The block you provide is for system use only. Audio Unit hosts must not attempt to interact with the audio unit through this block.

## See Also

### Managing the Render Cycle
- [func allocateRenderResources() throws](./allocaterenderresources%28%29.md)
  Allocates resources required to render audio.
- [func deallocateRenderResources()](./deallocaterenderresources%28%29.md)
  Deallocates resources required to render audio.
- [func reset()](./reset%28%29.md)
  Resets transitory rendering state to its initial state.
- [var renderResourcesAllocated: Bool](./renderresourcesallocated.md)
  Determines whether the audio unit has allocated render resources.
- [var renderBlock: AURenderBlock](./renderblock.md)
  The block that hosts use to ask the audio unit to render audio.
- [var scheduleParameterBlock: AUScheduleParameterBlock](./scheduleparameterblock.md)
  The block that hosts use to schedule parameters.
- [var maximumFramesToRender: AUAudioFrameCount](./maximumframestorender.md)
  The maximum number of frames that the audio unit can render at once.
- [func token(byAddingRenderObserver: AURenderObserver) -> Int](./token%28byaddingrenderobserver%29.md)
  Adds a block to be called on each render cycle.
- [func removeRenderObserver(Int)](./removerenderobserver%28_%29.md)
  Removes an observer block previously added to the render cycle.
- [AURenderContextObserver](../aurendercontextobserver.md)
  A custom block that tells the audio unit which thread context to use for the next render cycle.
- [AudioUnitRenderContext](../audiounitrendercontext.md)
  A structure that contains thread context information for a real-time rendering operation.
- [typealias AURenderObserver](../aurenderobserver.md)
  A block called when an audio unit renders audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/rendercontextobserver)*