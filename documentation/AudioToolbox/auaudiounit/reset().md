# reset()

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

Resets transitory rendering state to its initial state.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func reset()
```

```objc
- (void) reset;
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](../migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Discussion

Hosts should call this at the point of a discontinuity in the input stream being provided to an audio unit—for example, when seeking forward or backward within a track. In response, audio units should clear delay lines, filters, etc. Subclasses should call the superclass implementation.

This version 3 method is bridged to the version 2 [`AudioUnitReset(_:_:_:)`](../audiounitreset%28_,_,_%29.md) API, in the global scope.

## See Also

### Managing the Render Cycle
- [func allocateRenderResources() throws](./allocaterenderresources%28%29.md)
  Allocates resources required to render audio.
- [func deallocateRenderResources()](./deallocaterenderresources%28%29.md)
  Deallocates resources required to render audio.
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
- [typealias AURenderObserver](../aurenderobserver.md)
  A block called when an audio unit renders audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/reset())*