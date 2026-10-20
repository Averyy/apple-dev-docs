# removeRenderObserver(_:)

**Framework**: Audio Toolbox  
**Kind**: method

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

#### Discussion

This version 3 property is bridged to the version 2 [`AudioUnitRemoveRenderNotify(_:_:_:)`](audiounitremoverendernotify(_:_:_:).md) API.

## Parameters

- `token`: The token associated with the block.

## See Also

- [func allocateRenderResources() throws](auaudiounit/allocaterenderresources.md)
  Allocates resources required to render audio.
- [func deallocateRenderResources()](auaudiounit/deallocaterenderresources.md)
  Deallocates resources required to render audio.
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
- [typealias AURenderObserver](aurenderobserver.md)
  A block called when an audio unit renders audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/removerenderobserver(_:))*