# MIDIObjectType

**Framework**: Core MIDI  
**Kind**: enum

The MIDI object types that the system supports.

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
enum MIDIObjectType
```

## Topics

### Object Types
- [MIDIObjectType.other](midiobjecttype/other.md)
  A MIDI object with an undefined type.
- [MIDIObjectType.device](midiobjecttype/device.md)
  A MIDI device.
- [MIDIObjectType.entity](midiobjecttype/entity.md)
  A MIDI entity.
- [MIDIObjectType.source](midiobjecttype/source.md)
  A MIDI source.
- [MIDIObjectType.destination](midiobjecttype/destination.md)
  A MIDI destination.
- [MIDIObjectType.externalDevice](midiobjecttype/externaldevice.md)
  An external device.
- [MIDIObjectType.externalEntity](midiobjecttype/externalentity.md)
  An external entity.
- [MIDIObjectType.externalSource](midiobjecttype/externalsource.md)
  An external source.
- [MIDIObjectType.externalDestination](midiobjecttype/externaldestination.md)
  An external destination.
- [let kMIDIObjectType_ExternalMask: MIDIObjectType](kmidiobjecttype_externalmask.md)
  A bit mask indicating that a device is external.
### Initializers
- [init?(rawValue: Int32)](midiobjecttype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [typealias MIDIUniqueID](midiuniqueid.md)
  A MIDI object’s unique identifier.
- [var kMIDIInvalidUniqueID: MIDIUniqueID](kmidiinvaliduniqueid.md)
  An invalid identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjecttype)*