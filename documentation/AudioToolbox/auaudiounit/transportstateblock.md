# transportStateBlock

**Framework**: Audio Toolbox  
**Kind**: property

A callback to the host for transport state information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var transportStateBlock: AUHostTransportStateBlock? { get set }
```

#### Discussion

An audio unit accessing this property should cache it in realtime-safe storage before beginning to render.

This version 3 property is bridged to the version 2 [`HostCallback_GetTransportState`](hostcallback_gettransportstate.md) and `HostCallback_GetTransportState2` callback members in the `kAudioUnitProperty_HostCallbacks` API.

## See Also

- [var musicalContextBlock: AUHostMusicalContextBlock?](auaudiounit/musicalcontextblock.md)
  A callback to the host for musical context information.
- [var contextName: String?](auaudiounit/contextname.md)
  Information about the host context in which the audio unit is connected, for display in the audio unit’s view.
- [var supportsMPE: Bool](auaudiounit/supportsmpe.md)
  A Boolean value that indicates whether the audio unit supports multi-dimensional polyphonic expression.
- [typealias AUHostMusicalContextBlock](auhostmusicalcontextblock.md)
  A block through which hosts provide musical tempo, time signature, and beat position.
- [typealias AUHostTransportStateBlock](auhosttransportstateblock.md)
  A block through which hosts provide information about their transport state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/transportstateblock)*