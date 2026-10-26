# removeRenderObserver(_:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Removes an observer block previously added to the render cycle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeRenderObserver(_ token: Int)
```

```objc
- (void) removeRenderObserver:(NSInteger) token;
```

#### Discussion

This version 3 property is bridged to the version 2 [`AudioUnitRemoveRenderNotify(_:_:_:)`](../audiounitremoverendernotify%28_,_,_%29.md) API.

## Parameters

- `token`: The token associated with the block.

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
- [typealias AURenderObserver](../aurenderobserver.md)
  A block called when an audio unit renders audio.
- [renderContextObserver](./rendercontextobserver.md)
  The block that the system calls when the rendering context changes.
- [AURenderContextObserver](../aurendercontextobserver.md)
  A custom block that tells the audio unit which thread context to use for the next render cycle.
- [AudioUnitRenderContext](../audiounitrendercontext.md)
  A structure that contains thread context information for a real-time rendering operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/removerenderobserver(_:))*