# MIDIEndpointRef

**Framework**: Core MIDI  
**Kind**: typealias

A MIDI source or destination an entity owns.

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
typealias MIDIEndpointRef = MIDIObjectRef
```

#### Discussion

An endpoint object derives from [`MIDIObjectRef`](midiobjectref.md). It’s owned by a [`MIDIEntityRef`](midientityref.md), unless it’s a virtual endpoint, in which case it has no owner. An entity may have any number of MIDI endpoints, which contain sources and destinations of 16-channel MIDI streams.

## See Also

- [func MIDIEndpointDispose(MIDIEndpointRef) -> OSStatus](midiendpointdispose(_:).md)
  Disposes of a virtual source or destination.
- [func MIDIEndpointGetEntity(MIDIEndpointRef, UnsafeMutablePointer<MIDIEntityRef>?) -> OSStatus](midiendpointgetentity(_:_:).md)
  Returns an endpoint’s entity.
- [func MIDIEndpointGetRefCons(MIDIEndpointRef, UnsafeMutablePointer<UnsafeMutableRawPointer>?, UnsafeMutablePointer<UnsafeMutableRawPointer>?) -> OSStatus](midiendpointgetrefcons(_:_:_:).md)
  Returns contextual data assigned to an endpoint.
- [func MIDIEndpointSetRefCons(MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus](midiendpointsetrefcons(_:_:_:).md)
  Sets contextual data on an endpoint.
- [func MIDISourceCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](midisourcecreatewithprotocol(_:_:_:_:).md)
  Creates a virtual source in a client.
- [func MIDIGetSource(Int) -> MIDIEndpointRef](midigetsource(_:).md)
  Returns a source in the system.
- [func MIDIGetNumberOfSources() -> Int](midigetnumberofsources().md)
  Returns the number of sources in the system.
- [func MIDIDestinationCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIEndpointRef>, MIDIReceiveBlock) -> OSStatus](mididestinationcreatewithprotocol(_:_:_:_:_:).md)
  Creates a virtual destination in a client.
- [func MIDIGetDestination(Int) -> MIDIEndpointRef](midigetdestination(_:).md)
  Returns a destination in the system.
- [func MIDIGetNumberOfDestinations() -> Int](midigetnumberofdestinations().md)
  Returns the number of destinations in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiendpointref)*