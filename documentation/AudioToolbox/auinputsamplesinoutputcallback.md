# AUInputSamplesInOutputCallback

**Framework**: Audio Toolbox  
**Kind**: typealias

Called by the system when an audio unit has provided a buffer of output samples.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUInputSamplesInOutputCallback = (UnsafeMutableRawPointer, UnsafePointer<AudioTimeStamp>, Float64, Float64) -> Void
```

#### Return Value

A result code.

#### Discussion

If you named your callback function `MyAUInputSamplesInOutputCallback`, you would declare it like this:

##### Discussion

When your application uses a  or pitch-shifting audio unit, it may not be clear which input samples are represented in a buffer of output samples. This callback function addresses this issue by providing the input sample number corresponding to the first sample in an output buffer.

## Parameters

- `inRefCon`: Custom data that you provided when registering your callback with the audio unit.
- `inOutputTimeStamp`: The time stamp that corresponds to the first sample of audio data produced in AudioUnitRender (its output data).
- `inInputSample`: The sample number of the input that is represented in the first sample of that output time stamp.
- `inNumberInputSamples`: The number of input samples that are represented in an output buffer.

## See Also

- [typealias HostCallback_GetBeatAndTempo](hostcallback_getbeatandtempo.md)
  When called by the system, provides beat and tempo information to an audio unit from a host application.
- [typealias HostCallback_GetMusicalTimeLocation](hostcallback_getmusicaltimelocation.md)
  When called by the system, provides musical timing information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState](hostcallback_gettransportstate.md)
  When called by the system, provides audio transport state and timeline information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState2](hostcallback_gettransportstate2.md)
- [typealias AUMIDIOutputCallback](aumidioutputcallback.md)
  When called by a host application, gets MIDI data from an audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auinputsamplesinoutputcallback)*