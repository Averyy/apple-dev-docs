# moving

**Framework**: Audio Toolbox  
**Kind**: property  
**Role**: Type Property

Indicates that the audio transport is moving.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
static var moving: AUHostTransportStateFlags { get }
```

```c
AUHostTransportStateMoving
```

## See Also

### Constants
- [static var changed: AUHostTransportStateFlags](./changed.md)
  Indicates such state changes as start, stop, or seeking to another position in the timeline. Can be active if there was a change to the state of, or discontinuities in, the audio transport since the [`AUHostTransportStateBlock`](../auhosttransportstateblock.md) callback was last called.
- [static var cycling: AUHostTransportStateFlags](./cycling.md)
  Indicates that the host is cycling or looping.
- [static var recording: AUHostTransportStateFlags](./recording.md)
  Indicates that the host is recording, or is prepared to record. Can be active with or without a moving state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auhosttransportstateflags/moving)*