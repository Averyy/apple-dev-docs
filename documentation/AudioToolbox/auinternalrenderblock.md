# AUInternalRenderBlock

**Framework**: Audio Toolbox  
**Kind**: typealias

A block to render the audio unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUInternalRenderBlock = (UnsafeMutablePointer<AudioUnitRenderActionFlags>, UnsafePointer<AudioTimeStamp>, AUAudioFrameCount, Int, UnsafeMutablePointer<AudioBufferList>, UnsafePointer<AURenderEvent>?, AURenderPullInputBlock?) -> AUAudioUnitStatus
```

#### Discussion

This block is implemented in subclasses and should not be used by hosts.

The block returns an audio unit status result code. If instead an error is returned, the output data should be assumed to be invalid.

The block takes the following parameters:

- **actionFlags**: The pointer to the action flags.
- **timestamp**: The HAL time at which the input data will be rendered. If there is a sample rate conversion or time compression/expansion downstream, the sample time will not have a defined correlation with the `AudioDevice` sample time.
- **frameCount**: The number of sample frames to render.
- **outputBusNumber**: The index of the output bus to render.
- **outputData**: The output bus’s render buffers and flags. The buffer pointers may be null on entry, in which case the block will render into memory it owns and modify the `mData` pointers to point to that memory. The block is responsible for preserving the validity of that memory until it is next called to render, or until the [`deallocateRenderResources()`](auaudiounit/deallocaterenderresources().md) method is called.
- **realtimeEventListHead**: A time-ordered linked list of the events to be rendered during this cycle. A ramp event will only appear in the render cycle during which it starts; the audio unit is responsible for maintaining continued ramping state for any further render cycles.
- **pullInputBlock**: A block that the audio unit will call in order to pull for input data. This value may be `nil` for instrument and audio generator units (which do not have input busses).

## See Also

- [class func registerSubclass(AnyClass, as: AudioComponentDescription, name: String, version: UInt32)](auaudiounit/registersubclass(_:as:name:version:).md)
  Registers an audio unit subclass.
- [func shouldChange(to: AVAudioFormat, for: AUAudioUnitBus) -> Bool](auaudiounit/shouldchange(to:for:).md)
  This is called when you set the format on a bus.
- [func setRenderResourcesAllocated(Bool)](auaudiounit/setrenderresourcesallocated(_:).md)
  Sets the Boolean value of the [`renderResourcesAllocated`](auaudiounit/renderresourcesallocated.md) property.
- [var internalRenderBlock: AUInternalRenderBlock](auaudiounit/internalrenderblock.md)
  The block which you must provide, via a getter, in order to implement rendering.
- [var midiOutputBufferSizeHint: Int](auaudiounit/midioutputbuffersizehint.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auinternalrenderblock)*