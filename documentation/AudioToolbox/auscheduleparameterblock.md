# AUScheduleParameterBlock

**Framework**: Audio Toolbox  
**Kind**: typealias

A block to schedule parameter changes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUScheduleParameterBlock = (AUEventSampleTime, AUAudioFrameCount, AUParameterAddress, AUValue) -> Void
```

#### Discussion

Check the parameter’s flags to determine whether the parameter is rampable. If a parameter isn’t rampable, a ramp duration of `0` changes it immediately to the target value, and a nonzero ramp duration leaves it unchanged.

The block takes the following parameters:

- **eventSampleTime**: The sample time at which the parameter begins changing. When you schedule parameters during the render cycle, such as from a render observer you add with [`token(byAddingRenderObserver:)`](auaudiounit/token(byaddingrenderobserver:).md), pass the `AUEventSampleTimeImmediate` value plus an optional buffer offset of fewer than 4096 sample frames to schedule the event at that position in the current render cycle.
- **rampDurationSampleFrames**: The number of sample frames over which the parameter’s return value is to ramp, or `0` if the parameter change should take effect immediately.
- **parameterAddress**: The parameter’s address.
- **value**: The parameter’s new value if the ramp duration is `0`; otherwise, the value at the end of the scheduled ramp.

## See Also

- [struct ScheduledAudioFileRegion](scheduledaudiofileregion.md)
- [struct ScheduledAudioSlice](scheduledaudioslice.md)
- [typealias ScheduledAudioFileRegionCompletionProc](scheduledaudiofileregioncompletionproc.md)
- [typealias ScheduledAudioSliceCompletionProc](scheduledaudioslicecompletionproc.md)
- [typealias MIDIChannelNumber](midichannelnumber.md)
  MIDI Channel, 0~15 (channels 1 through 16, respectively).
- [typealias AUAudioObjectID](auaudioobjectid.md)
- [typealias AUMIDICIProfileChangedBlock](aumidiciprofilechangedblock.md)
- [typealias AUAudioChannelCount](auaudiochannelcount.md)
  A number of audio channels.
- [typealias AUAudioFrameCount](auaudioframecount.md)
  A number of audio sample frames.
- [typealias AUAudioUnitStatus](auaudiounitstatus.md)
  A result code returned from an audio unit’s render function.
- [typealias AUEventListenerProc](aueventlistenerproc.md)
- [typealias AUEventListenerRef](aueventlistenerref.md)
- [typealias AUEventSampleTime](aueventsampletime.md)
  Expresses time as a sample count.
- [typealias AUImplementorValueObserver](auimplementorvalueobserver.md)
  A block called to notify the audio unit implementation of changes to a parameter value.
- [typealias AUImplementorValueProvider](auimplementorvalueprovider.md)
  A block called to fetch a parameter’s current value from the audio unit implementation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auscheduleparameterblock)*