# inputDevicePose

**Framework**: TabletopKit  
**Kind**: property

The current pose of the input device.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
var inputDevicePose: Pose3D { get }
```

## See Also

- [var initialInputDevicePose: Pose3D](tabletopinteraction/value-swift.struct/gesture-swift.struct/initialinputdevicepose.md)
  The pose of the input device at the start of the interaction.
- [var kind: TabletopInteraction.Value.Gesture.Kind](tabletopinteraction/value-swift.struct/gesture-swift.struct/kind-swift.property.md)
  The input source or mode which started this gesture.
- [TabletopInteraction.Value.Gesture.Kind](tabletopinteraction/value-swift.struct/gesture-swift.struct/kind-swift.enum.md)
  The possible input sources or modes that can start a gesture interaction.
- [var chirality: TabletopInteraction.Value.Gesture.Chirality?](tabletopinteraction/value-swift.struct/gesture-swift.struct/chirality-swift.property.md)
  The chirality, or handedness, of this gesture, if known.
- [TabletopInteraction.Value.Gesture.Chirality](tabletopinteraction/value-swift.struct/gesture-swift.struct/chirality-swift.enum.md)
  The chirality, or handedness, of a gesture.
- [var phase: TabletopInteraction.Value.Phase](tabletopinteraction/value-swift.struct/gesture-swift.struct/phase.md)
  The current phase of the gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tabletopkit/tabletopinteraction/value-swift.struct/gesture-swift.struct/inputdevicepose)*