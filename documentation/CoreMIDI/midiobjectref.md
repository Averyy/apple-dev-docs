# MIDIObjectRef

**Framework**: Core MIDI  
**Kind**: typealias

The common base class for many of the framework’s objects.

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
typealias MIDIObjectRef = UInt32
```

#### Discussion

MIDI Objects have properties, and often have an owning object, from which they inherit any properties they don’t define themselves.

Developers may add their own private properties, with names that begin with their company’s inverted domain name, but with underscores instead of dots. For example, `com_apple_APrivateAppleProperty`.

## See Also

- [func MIDIObjectFindByUniqueID(MIDIUniqueID, UnsafeMutablePointer<MIDIObjectRef>?, UnsafeMutablePointer<MIDIObjectType>?) -> OSStatus](midiobjectfindbyuniqueid(_:_:_:).md)
  Locates a device, entity, or endpoint by its unique identifier.
- [MIDI Object Properties](midi-object-properties.md)
  Configure the properties of MIDI objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiobjectref)*