# HostCallback_GetBeatAndTempo

**Framework**: Audio Toolbox  
**Kind**: typealias

When called by the system, provides beat and tempo information to an audio unit from a host application.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias HostCallback_GetBeatAndTempo = (UnsafeMutableRawPointer?, UnsafeMutablePointer<Float64>?, UnsafeMutablePointer<Float64>?) -> OSStatus
```

#### Discussion

If you named your callback function `MyHostCallback_GetBeatAndTempo`, you would declare it like this:

## Parameters

- `inHostUserData`: Custom data that you provided when registering your callback with the audio unit.
- `outCurrentBeat`: On output, the current beat of the music that is playing.
- `outCurrentTempo`: On output, the current tempo of the music that is playing.

## See Also

- [typealias HostCallback_GetMusicalTimeLocation](hostcallback_getmusicaltimelocation.md)
  When called by the system, provides musical timing information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState](hostcallback_gettransportstate.md)
  When called by the system, provides audio transport state and timeline information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState2](hostcallback_gettransportstate2.md)
- [typealias AUInputSamplesInOutputCallback](auinputsamplesinoutputcallback.md)
  Called by the system when an audio unit has provided a buffer of output samples.
- [typealias AUMIDIOutputCallback](aumidioutputcallback.md)
  When called by a host application, gets MIDI data from an audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/hostcallback_getbeatandtempo)*