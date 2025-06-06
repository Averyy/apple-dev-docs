# HostCallback_GetMusicalTimeLocation

**Framework**: Audio Toolbox  
**Kind**: typealias

When called by the system, provides musical timing information to an audio unit from a host application.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias HostCallback_GetMusicalTimeLocation = (UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<Float32>?, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<Float64>?) -> OSStatus
```

#### Discussion

If you named your callback function `MyHostCallback_GetMusicalTimeLocation`, you would declare it like this:

## Parameters

- `inHostUserData`: Custom data that you provided when registering your callback with the audio unit.
- `outDeltaSampleOffsetToNextBeat`: On output, the number of samples until the next beat.
- `outTimeSig_Numerator`: On output, the numerator for a musical time signature.
- `outTimeSig_Denominator`: On output, the denominator for a musical time signature.
- `outCurrentMeasureDownBeat`: 

## See Also

- [typealias HostCallback_GetBeatAndTempo](hostcallback_getbeatandtempo.md)
  When called by the system, provides beat and tempo information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState](hostcallback_gettransportstate.md)
  When called by the system, provides audio transport state and timeline information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState2](hostcallback_gettransportstate2.md)
- [typealias AUInputSamplesInOutputCallback](auinputsamplesinoutputcallback.md)
  Called by the system when an audio unit has provided a buffer of output samples.
- [typealias AUMIDIOutputCallback](aumidioutputcallback.md)
  When called by a host application, gets MIDI data from an audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/hostcallback_getmusicaltimelocation)*