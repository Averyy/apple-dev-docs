# HostCallback_GetTransportState

**Framework**: Audio Toolbox  
**Kind**: typealias

When called by the system, provides audio transport state and timeline information to an audio unit from a host application.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias HostCallback_GetTransportState = (UnsafeMutableRawPointer?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<Float64>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<Float64>?, UnsafeMutablePointer<Float64>?) -> OSStatus
```

#### Discussion

If you named your callback function `MyHostCallback_GetTransportState`, you would declare it like this:

## Parameters

- `inHostUserData`: Custom data that you provided when registering your callback with the audio unit.
- `outIsPlaying`: On output,   if audio is playing, or   otherwise.
- `outTransportStateChanged`: On output,   if the transport state changed since the last time the callback was invoked, or   otherwise.
- `outCurrentSampleInTimeLine`: On output, the sample number, indexed from zero from the beginning of the timeline.
- `outIsCycling`: On output,   if cycling, or   otherwise.
- `outCycleStartBeat`: 
- `outCycleEndBeat`: 

## See Also

- [typealias HostCallback_GetBeatAndTempo](hostcallback_getbeatandtempo.md)
  When called by the system, provides beat and tempo information to an audio unit from a host application.
- [typealias HostCallback_GetMusicalTimeLocation](hostcallback_getmusicaltimelocation.md)
  When called by the system, provides musical timing information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState2](hostcallback_gettransportstate2.md)
- [typealias AUInputSamplesInOutputCallback](auinputsamplesinoutputcallback.md)
  Called by the system when an audio unit has provided a buffer of output samples.
- [typealias AUMIDIOutputCallback](aumidioutputcallback.md)
  When called by a host application, gets MIDI data from an audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/hostcallback_gettransportstate)*