# renderResourcesAllocated

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

Determines whether the audio unit has allocated render resources.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var renderResourcesAllocated: Bool { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) BOOL renderResourcesAllocated;
```

*macOS*

```objc
@property (atomic, readonly) BOOL renderResourcesAllocated;
```

## See Also

### Managing the Render Cycle
- [func allocateRenderResources() throws](./allocaterenderresources%28%29.md)
  Allocates resources required to render audio.
- [func deallocateRenderResources()](./deallocaterenderresources%28%29.md)
  Deallocates resources required to render audio.
- [func reset()](./reset%28%29.md)
  Resets transitory rendering state to its initial state.
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
- [typealias AURenderObserver](../aurenderobserver.md)
  A block called when an audio unit renders audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/renderresourcesallocated)*