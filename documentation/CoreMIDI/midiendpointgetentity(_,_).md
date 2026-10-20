# MIDIEndpointGetEntity(_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Returns an endpoint’s entity.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.2+
- visionOS 1.0+

## Declaration

```swift
func MIDIEndpointGetEntity(_ inEndpoint: MIDIEndpointRef, _ outEntity: UnsafeMutablePointer<MIDIEntityRef>?) -> OSStatus
```

```c
extern OSStatus MIDIEndpointGetEntity(MIDIEndpointRef inEndpoint, MIDIEntityRef *outEntity);
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Virtual sources and destinations don’t have entities.

## Parameters

- `inEndpoint`: The endpoint to query.
- `outEntity`: On exit, the endpoint’s owning entity, or `NULL` if none.

## See Also

### Endpoint management
- [func MIDIEndpointDispose(MIDIEndpointRef) -> OSStatus](./midiendpointdispose%28_%29.md)
  Disposes of a virtual source or destination.
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
- [typealias MIDIEndpointRef](./midiendpointref.md)
  A MIDI source or destination an entity owns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiendpointgetentity(_:_:))*