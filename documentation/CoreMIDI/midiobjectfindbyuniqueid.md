# MIDIObjectFindByUniqueID(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Locates a device, entity, or endpoint by its unique identifier.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIObjectFindByUniqueID(_ inUniqueID: MIDIUniqueID, _ outObject: UnsafeMutablePointer<MIDIObjectRef>?, _ outObjectType: UnsafeMutablePointer<MIDIObjectType>?) -> OSStatus
```

#### Return Value

An `OSStatus` error code, including [`kMIDIObjectNotFound`](kmidiobjectnotfound.md) if there is no object with this unique ID.

## Parameters

- `inUniqueID`: The unique ID of the object to search for. You determine the unique ID by querying   for the   property.
- `outObject`: The returned object, or 0 if the object wasn’t found or an error occurred. Cast this pointer to the appropriate type, according to type specified by the   argument.
- `outObjectType`: On exit, the type of object found, or undefined if the system found no objects.

## Topics

### Parameter Types
- [typealias MIDIUniqueID](midiuniqueid.md)
  A MIDI object’s unique identifier.
- [var kMIDIInvalidUniqueID: MIDIUniqueID](kmidiinvaliduniqueid.md)
  An invalid identifier.
- [enum MIDIObjectType](midiobjecttype.md)
  The MIDI object types that the system supports.

## See Also

- [typealias MIDIObjectRef](midiobjectref.md)
  The common base class for many of the framework’s objects.
- [MIDI Object Properties](midi-object-properties.md)
  Configure the properties of MIDI objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectfindbyuniqueid(_:_:_:))*