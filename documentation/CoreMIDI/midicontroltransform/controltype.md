# controlType

**Framework**: Core MIDI  
**Kind**: property  
**Role**: Instance Property

The type of control specified by the control number.

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
var controlType: MIDITransformControlType
```

```c
MIDITransformControlType controlType;
```

## See Also

### Configuring a Control Transform
- [var remappedControlType: MIDITransformControlType](./remappedcontroltype.md)
  The remapped control type.
- [var controlNumber: UInt16](./controlnumber.md)
  The control number to affect.
- [var transform: MIDITransformType](./transform.md)
  The type of transformation to apply to the event values.
- [var param: Int16](./param.md)
  An argument to the transformation method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicontroltransform/controltype)*