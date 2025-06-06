# supportsMPE

**Framework**: Audio Toolbox  
**Kind**: property

A Boolean value that indicates whether the audio unit supports multi-dimensional polyphonic expression.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var supportsMPE: Bool { get }
```

## See Also

- [var musicalContextBlock: AUHostMusicalContextBlock?](auaudiounit/musicalcontextblock.md)
  A callback to the host for musical context information.
- [var transportStateBlock: AUHostTransportStateBlock?](auaudiounit/transportstateblock.md)
  A callback to the host for transport state information.
- [var contextName: String?](auaudiounit/contextname.md)
  Information about the host context in which the audio unit is connected, for display in the audio unit’s view.
- [typealias AUHostMusicalContextBlock](auhostmusicalcontextblock.md)
  A block through which hosts provide musical tempo, time signature, and beat position.
- [typealias AUHostTransportStateBlock](auhosttransportstateblock.md)
  A block through which hosts provide information about their transport state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/auaudiounit/supportsmpe)*