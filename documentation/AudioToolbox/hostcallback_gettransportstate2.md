# HostCallback_GetTransportState2

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias HostCallback_GetTransportState2 = (UnsafeMutableRawPointer?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<Float64>?, UnsafeMutablePointer<DarwinBoolean>?, UnsafeMutablePointer<Float64>?, UnsafeMutablePointer<Float64>?) -> OSStatus
```

```c
typedef int (*)(void *, unsigned char *, unsigned char *, unsigned char *, double *, unsigned char *, double *, double *) __attribute__((nonblocking)) HostCallback_GetTransportState2;
```

## See Also

### Getting Information from the Host
- [typealias HostCallback_GetBeatAndTempo](./hostcallback_getbeatandtempo.md)
  When called by the system, provides beat and tempo information to an audio unit from a host application.
- [typealias HostCallback_GetMusicalTimeLocation](./hostcallback_getmusicaltimelocation.md)
  When called by the system, provides musical timing information to an audio unit from a host application.
- [typealias HostCallback_GetTransportState](./hostcallback_gettransportstate.md)
  When called by the system, provides audio transport state and timeline information to an audio unit from a host application.
- [typealias AUInputSamplesInOutputCallback](./auinputsamplesinoutputcallback.md)
  Called by the system when an audio unit has provided a buffer of output samples.
- [typealias AUMIDIOutputCallback](./aumidioutputcallback.md)
  When called by a host application, gets MIDI data from an audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/hostcallback_gettransportstate2)*