# remappedControlType

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The remapped control type.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var remappedControlType: MIDITransformControlType
```

```c
MIDITransformControlType remappedControlType;
```

## Discussion

If transform is [`MIDITransformType.mapControl`](../miditransformtype/mapcontrol.md), the output control type.

## See Also

### Configuring a Control Transform
- [var controlType: MIDITransformControlType](./controltype.md)
  The type of control specified by the control number.
- [var controlNumber: UInt16](./controlnumber.md)
  The control number to affect.
- [var transform: MIDITransformType](./transform.md)
  The type of transformation to apply to the event values.
- [var param: Int16](./param.md)
  An argument to the transformation method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicontroltransform/remappedcontroltype)*