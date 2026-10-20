# token(byAddingRenderObserver:)

**Framework**: Audio Toolbox  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSInteger) tokenByAddingRenderObserver:(AURenderObserver) observer;
```

#### Return Value

A token to be used when removing the observer.

#### Discussion

The supplied block is called at the beginning and ending of each render cycle. It should not make any blocking calls.

This method is implemented in the [`AUAudioUnit`](../auaudiounit.md) base class and should not be overridden.

This version 3 method is bridged to the version 2 [`AudioUnitAddRenderNotify(_:_:_:)`](../audiounitaddrendernotify%28_,_,_%29.md) API.

## Parameters

- `observer`: The block to call.

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
- [func removeRenderObserver(Int)](./removerenderobserver%28_%29.md)
  Removes an observer block previously added to the render cycle.
- [typealias AURenderObserver](../aurenderobserver.md)
  A block called when an audio unit renders audio.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/token(byaddingrenderobserver:))*