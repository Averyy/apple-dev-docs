# MIDIEndpointRef

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

A MIDI source or destination an entity owns.

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
typealias MIDIEndpointRef = MIDIObjectRef
```

```c
typedef MIDIObjectRef MIDIEndpointRef;
```

## Discussion

An endpoint object derives from [`MIDIObjectRef`](./midiobjectref.md). It’s owned by a [`MIDIEntityRef`](./midientityref.md), unless it’s a virtual endpoint, in which case it has no owner. An entity may have any number of MIDI endpoints, which contain sources and destinations of 16-channel MIDI streams.

## See Also

### Endpoint management
- [func MIDIEndpointDispose(MIDIEndpointRef) -> OSStatus](./midiendpointdispose%28_%29.md)
  Disposes of a virtual source or destination.
- [func MIDIEndpointGetEntity(MIDIEndpointRef, UnsafeMutablePointer<MIDIEntityRef>?) -> OSStatus](./midiendpointgetentity%28_,_%29.md)
  Returns an endpoint’s entity.
- [func MIDIEndpointGetRefCons(MIDIEndpointRef, UnsafeMutablePointer<UnsafeMutableRawPointer>?, UnsafeMutablePointer<UnsafeMutableRawPointer>?) -> OSStatus](./midiendpointgetrefcons%28_,_,_%29.md)
  Returns contextual data assigned to an endpoint.
- [func MIDIEndpointSetRefCons(MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus](./midiendpointsetrefcons%28_,_,_%29.md)
  Sets contextual data on an endpoint.
- [func MIDISourceCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus](./midisourcecreatewithprotocol%28_,_,_,_%29.md)
  Creates a virtual source in a client.
- [func MIDIGetSource(Int) -> MIDIEndpointRef](./midigetsource%28_%29.md)
  Returns a source in the system.
- [func MIDIGetNumberOfSources() -> Int](./midigetnumberofsources%28%29.md)
  Returns the number of sources in the system.
- [func MIDIDestinationCreateWithProtocol(MIDIClientRef, CFString, MIDIProtocolID, UnsafeMutablePointer<MIDIEndpointRef>, MIDIReceiveBlock) -> OSStatus](./mididestinationcreatewithprotocol%28_,_,_,_,_%29.md)
  Creates a virtual destination in a client.
- [func MIDIGetDestination(Int) -> MIDIEndpointRef](./midigetdestination%28_%29.md)
  Returns a destination in the system.
- [func MIDIGetNumberOfDestinations() -> Int](./midigetnumberofdestinations%28%29.md)
  Returns the number of destinations in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiendpointref)*