# token(byAddingRenderObserver:)

**Framework**: Audio Toolbox  
**Kind**: method

Adds a block to be called on each render cycle.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func token(byAddingRenderObserver observer: @escaping AURenderObserver) -> Int
```

#### Return Value

A token to be used when removing the observer.

#### Discussion

The supplied block is called at the beginning and ending of each render cycle. It should not make any blocking calls.

This method is implemented in the [`AUAudioUnit`](auaudiounit.md) base class and should not be overridden.

This version 3 method is bridged to the version 2 [`AudioUnitAddRenderNotify(_:_:_:)`](audiounitaddrendernotify(_:_:_:).md) API.

## Parameters

- `observer`: The block to call.

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
- [func removeRenderObserver(Int)](auaudiounit/removerenderobserver(_:).md)
  Removes an observer block previously added to the render cycle.
- [typealias AURenderObserver](aurenderobserver.md)
  A block called when an audio unit renders audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/token(byaddingrenderobserver:))*