# cycling

**Framework**: Audio Toolbox  
**Kind**: property

Indicates that the host is cycling or looping.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
static var cycling: AUHostTransportStateFlags { get }
```

## See Also

- [static var changed: AUHostTransportStateFlags](auhosttransportstateflags/changed.md)
  Indicates such state changes as start, stop, or seeking to another position in the timeline. Can be active if there was a change to the state of, or discontinuities in, the audio transport since the [`AUHostTransportStateBlock`](auhosttransportstateblock.md) callback was last called.
- [static var moving: AUHostTransportStateFlags](auhosttransportstateflags/moving.md)
  Indicates that the audio transport is moving.
- [static var recording: AUHostTransportStateFlags](auhosttransportstateflags/recording.md)
  Indicates that the host is recording, or is prepared to record. Can be active with or without a moving state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/cycling)*