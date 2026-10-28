# renderBlock

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Instance Property

The block that hosts use to ask the audio unit to render audio.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var renderBlock: AURenderBlock { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@property (nonatomic, readonly) AURenderBlock renderBlock;
```

*macOS*

```objc
@property (atomic, readonly) AURenderBlock renderBlock;
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](../migrating-your-audio-unit-host-to-the-auv3-api.md)

## Discussion

Before invoking an audio unit’s rendering functionality, a host should fetch this block and cache the result. The block can then be called from a realtime context without the possibility of blocking and causing an overload at the Core Audio HAL level.

This block will call a subclass’s [`internalRenderBlock`](./internalrenderblock.md) implementation, providing all realtime events scheduled for the current render time interval, bracketed by calls to any render observers. Subclasses should override their [`internalRenderBlock`](./internalrenderblock.md) implementation, not this property.

This version 3 property is bridged to the version 2 [`AudioUnitRender(_:_:_:_:_:_:)`](../audiounitrender%28_,_,_,_,_,_%29.md) API.

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
- [renderContextObserver](./rendercontextobserver.md)
  The block that the system calls when the rendering context changes.
- [AURenderContextObserver](../aurendercontextobserver.md)
  A custom block that tells the audio unit which thread context to use for the next render cycle.
- [AudioUnitRenderContext](../audiounitrendercontext.md)
  A structure that contains thread context information for a real-time rendering operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/renderblock)*