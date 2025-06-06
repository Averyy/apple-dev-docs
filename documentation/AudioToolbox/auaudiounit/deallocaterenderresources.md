# deallocateRenderResources()

**Framework**: Audio Toolbox  
**Kind**: method

Deallocates resources required to render audio.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func deallocateRenderResources()
```

## Mentions

- [Migrating Your Audio Unit Host to the AUv3 API](migrating-your-audio-unit-host-to-the-auv3-api.md)

#### Discussion

Hosts should call this after finishing rendering. Subclasses should call the superclass implementation.

This version 3 method is bridged to the version 2 [`AudioUnitUninitialize(_:)`](audiounituninitialize(_:).md) API.

## See Also

- [func allocateRenderResources() throws](auaudiounit/allocaterenderresources.md)
  Allocates resources required to render audio.
- [func reset()](auaudiounit/reset.md)
  Resets transitory rendering state to its initial state.
- [var renderResourcesAllocated: Bool](auaudiounit/renderresourcesallocated.md)
  Determines whether the audio unit has allocated render resources.
- [var renderBlock: AURenderBlock](auaudiounit/renderblock.md)
  The block that hosts use to ask the audio unit to render audio.
- [var scheduleParameterBlock: AUScheduleParameterBlock](auaudiounit/scheduleparameterblock.md)
  The block that hosts use to schedule parameters.
- [var maximumFramesToRender: AUAudioFrameCount](auaudiounit/maximumframestorender.md)
  The maximum number of frames that the audio unit can render at once.
- [func token(byAddingRenderObserver: AURenderObserver) -> Int](auaudiounit/token(byaddingrenderobserver:).md)
  Adds a block to be called on each render cycle.
- [func removeRenderObserver(Int)](auaudiounit/removerenderobserver(_:).md)
  Removes an observer block previously added to the render cycle.
- [typealias AURenderObserver](aurenderobserver.md)
  A block called when an audio unit renders audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/deallocaterenderresources())*