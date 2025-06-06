# HostCallbackInfo

**Framework**: Audio Toolbox  
**Kind**: struct

The time- and transport-related callback functions for an audio unit.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct HostCallbackInfo
```

## Topics

### Initializers
- [init()](hostcallbackinfo/init.md)
- [init(hostUserData: UnsafeMutableRawPointer?, beatAndTempoProc: HostCallback_GetBeatAndTempo?, musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation?, transportStateProc: HostCallback_GetTransportState?, transportStateProc2: HostCallback_GetTransportState2?)](hostcallbackinfo/init(hostuserdata:beatandtempoproc:musicaltimelocationproc:transportstateproc:transportstateproc2:).md)
### Instance Properties
- [var beatAndTempoProc: HostCallback_GetBeatAndTempo?](hostcallbackinfo/beatandtempoproc.md)
  Your callback function that provides beat and tempo information to an audio unit. May be `NULL`.
- [var hostUserData: UnsafeMutableRawPointer?](hostcallbackinfo/hostuserdata.md)
  Custom data specified by your application. May be `NULL`.
- [var musicalTimeLocationProc: HostCallback_GetMusicalTimeLocation?](hostcallbackinfo/musicaltimelocationproc.md)
  Your callback function that provides musical timeline information to an audio unit. May be `NULL`.
- [var transportStateProc: HostCallback_GetTransportState?](hostcallbackinfo/transportstateproc.md)
  Your callback function that provides audio transport state information (, , and so on) to an audio unit. May be `NULL`.
- [var transportStateProc2: HostCallback_GetTransportState2?](hostcallbackinfo/transportstateproc2.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [Other Plug-In Formats](1534082-other-plug-in-formats.md)
- [RenderQuality](1534177-renderquality.md)
  Render quality settings for audio units.
- [General Audio Unit Properties](general-audio-unit-properties.md)
  Properties that apply to any audio unit.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/hostcallbackinfo)*