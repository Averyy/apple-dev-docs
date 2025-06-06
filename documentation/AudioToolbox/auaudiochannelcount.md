# AUAudioChannelCount

**Framework**: Audio Toolbox  
**Kind**: typealias

A number of audio channels.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUAudioChannelCount = UInt32
```

#### Discussion

This alias is type `uint32_t` for impedance-matching with the pervasive use of `UInt32` in the Audio Toolbox framework and the C Audio Unit framework APIs, as well as the [`AVAudioChannelCount`](https://developer.apple.com/documentation/AVFAudio/AVAudioChannelCount) data type.

## See Also

- [struct ScheduledAudioFileRegion](scheduledaudiofileregion.md)
- [struct ScheduledAudioSlice](scheduledaudioslice.md)
- [typealias ScheduledAudioFileRegionCompletionProc](scheduledaudiofileregioncompletionproc.md)
- [typealias ScheduledAudioSliceCompletionProc](scheduledaudioslicecompletionproc.md)
- [typealias MIDIChannelNumber](midichannelnumber.md)
  MIDI Channel, 0~15 (channels 1 through 16, respectively).
- [typealias AUAudioObjectID](auaudioobjectid.md)
- [typealias AUMIDICIProfileChangedBlock](aumidiciprofilechangedblock.md)
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
- [typealias AUInputHandler](auinputhandler.md)
  A block to notify the host of an I/O unit that an input is available.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiochannelcount)*