# MIDITransformType.filterOut

**Framework**: Core MIDI  
**Kind**: case  
**Role**: Case

A transformation that filters out an event type.

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
case filterOut
```

```c
kMIDITransform_FilterOut
```

## See Also

### Transform Types
- [MIDITransformType.none](./none.md)
  No transformation.
- [MIDITransformType.mapControl](./mapcontrol.md)
  A transformation that changes a specified control number to a supplied parameter value.
- [MIDITransformType.add](./add.md)
  A transform that adds a parameter value.
- [MIDITransformType.scale](./scale.md)
  A transform that multiplies by the specified parameter value.
- [MIDITransformType.minValue](./minvalue.md)
  A transform that sets the minimum value to the specified parameter value.
- [MIDITransformType.maxValue](./maxvalue.md)
  A transform that sets the maximum value to the specified parameter value.
- [MIDITransformType.mapValue](./mapvalue.md)
  A transform that maps one value to another.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/miditransformtype/filterout)*