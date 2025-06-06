# MIDITransformType.mapValue

**Framework**: Core MIDI  
**Kind**: case

A transform that maps one value to another.

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
case mapValue
```

#### Discussion

The value you specify is the index of the map in the connection’s array of maps.

## See Also

- [MIDITransformType.none](miditransformtype/none.md)
  No transformation.
- [MIDITransformType.filterOut](miditransformtype/filterout.md)
  A transformation that filters out an event type.
- [MIDITransformType.mapControl](miditransformtype/mapcontrol.md)
  A transformation that changes a specified control number to a supplied parameter value.
- [MIDITransformType.add](miditransformtype/add.md)
  A transform that adds a parameter value.
- [MIDITransformType.scale](miditransformtype/scale.md)
  A transform that multiplies by the specified parameter value.
- [MIDITransformType.minValue](miditransformtype/minvalue.md)
  A transform that sets the minimum value to the specified parameter value.
- [MIDITransformType.maxValue](miditransformtype/maxvalue.md)
  A transform that sets the maximum value to the specified parameter value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/miditransformtype/mapvalue)*