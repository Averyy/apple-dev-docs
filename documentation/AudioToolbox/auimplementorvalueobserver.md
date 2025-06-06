# AUImplementorValueObserver

**Framework**: Audio Toolbox  
**Kind**: typealias

A block called to notify the audio unit implementation of changes to a parameter value.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUImplementorValueObserver = (AUParameter, AUValue) -> Void
```

#### Discussion

This block is only of interest to audio unit subclasses.

The block takes the following parameters:

## See Also

- [var implementorValueObserver: AUImplementorValueObserver](auparameternode/implementorvalueobserver.md)
  The callback for parameter value changes.
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
- [typealias AUImplementorValueProvider](auimplementorvalueprovider.md)
  A block called to fetch a parameter’s current value from the audio unit implementation.
- [typealias AUInputHandler](auinputhandler.md)
  A block to notify the host of an I/O unit that an input is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auimplementorvalueobserver)*