# MIDIControlTransform

**Framework**: Core MIDI  
**Kind**: struct

A structure that describes the transformation of MIDI control change events.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct MIDIControlTransform
```

#### Overview

A single parameters object may describe any number of transformations to control events. It’s important to order multiple transformations correctly: filter out, remap, and then alter values.

The system performs all transformations internally using 14-bit values, so when you perform an add, min, or max transform on a 7-bit control value, the parameter must be a 14-bit value. For example, to add 10 to a control value, the parameter must be (10 << 7) = 1280.

Based on the MIDI specification, the system interprets several controls specially:

| Control | Function |
| --- | --- |
| 32-63 | The least signifcant bit of 0-31. |
| 6/38 | Data entry. |
| 96, 97 | Data increment and decrement, respectively. |
| 98-101 | NRPN/RPN |

## Topics

### Configuring a Control Transform
- [var controlType: MIDITransformControlType](midicontroltransform/controltype.md)
  The type of control specified by the control number.
- [var remappedControlType: MIDITransformControlType](midicontroltransform/remappedcontroltype.md)
  The remapped control type.
- [var controlNumber: UInt16](midicontroltransform/controlnumber.md)
  The control number to affect.
- [var transform: MIDITransformType](midicontroltransform/transform.md)
  The type of transformation to apply to the event values.
- [var param: Int16](midicontroltransform/param.md)
  An argument to the transformation method.
### Initializers
- [init()](midicontroltransform/init.md)
- [init(controlType: MIDITransformControlType, remappedControlType: MIDITransformControlType, controlNumber: UInt16, transform: MIDITransformType, param: Int16)](midicontroltransform/init(controltype:remappedcontroltype:controlnumber:transform:param:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct MIDIValueMap](midivaluemap.md)
  A custom lookup table to transform MIDI 7-bit values, as contained in note numbers, velocities, control values, and so on.
- [struct MIDITransform](miditransform.md)
  The transformation of a single type of MIDI event.
- [enum MIDITransformType](miditransformtype.md)
  Values that specify the type of MIDI transformation.
- [enum MIDITransformControlType](miditransformcontroltype.md)
  A set of values that indicate how to interpret control numbers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midicontroltransform)*