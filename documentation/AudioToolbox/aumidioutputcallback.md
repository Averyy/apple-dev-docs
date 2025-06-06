# AUMIDIOutputCallback

**Framework**: Audio Toolbox  
**Kind**: typealias

When called by a host application, gets MIDI data from an audio unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AUMIDIOutputCallback = (UnsafeMutableRawPointer?, UnsafePointer<AudioTimeStamp>, UInt32, UnsafePointer<MIDIPacketList>) -> OSStatus
```

#### Discussion

If you named your callback function `MyAUMIDIOutputCallback`, you would declare it like this:

## Parameters

- `userData`: Custom data.
- `timeStamp`: 
- `midiOutNum`: 
- `pktlist`: 

## See Also

- [typealias HostCallback_GetBeatAndTempo](hostcallback_getbeatandtempo.md)
  When called by the system, provides beat and tempo information to an audio unit from a host application.
- [typealias HostCallback_GetMusicalTimeLocation](hostcallback_getmusicaltimelocation.md)
  When called by the system, provides musical timing information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState](hostcallback_gettransportstate.md)
  When called by the system, provides audio transport state and timeline information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState2](hostcallback_gettransportstate2.md)
- [typealias AUInputSamplesInOutputCallback](auinputsamplesinoutputcallback.md)
  Called by the system when an audio unit has provided a buffer of output samples.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/aumidioutputcallback)*