# MIDIDestinationCreateWithProtocol(_:_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Creates a virtual destination in a client.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIDestinationCreateWithProtocol(_ client: MIDIClientRef, _ name: CFString, _ protocol: MIDIProtocolID, _ outDest: UnsafeMutablePointer<MIDIEndpointRef>, _ readBlock: @escaping MIDIReceiveBlock) -> OSStatus
```

```c
extern OSStatus MIDIDestinationCreateWithProtocol(MIDIClientRef client, CFStringRef name, MIDIProtocolID protocol, MIDIEndpointRef *outDest, MIDIReceiveBlock readBlock);
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Drivers don’t need to call this function. When they create devices and entities, the system automatically creates sources and destinations at that time. See [`kMIDIPropertyAdvanceScheduleTimeMuSec`](./kmidipropertyadvancescheduletimemusec.md) for information about the relationship between when a sender sends MIDI data to the destination and when it’s received.

The system calls the read block on a separate high-priority thread owned by Core MIDI.

> 💡 **Tip**:  After creating a virtual source, assign it the same unique ID it had the last time your app created it. Doing so permits other clients to retain persistent references to your virtual source.

## Parameters

- `client`: The client that owns the virtual destination.
- `name`: The name of the virtual destination.
- `protocol`: The MIDI protocol variant to deliver to the destination. The system automatically converts messages to this protocol as needed.
- `outDest`: On successful return, a pointer to the newly created destination.
- `readBlock`: A callback block the system invokes when a client sends MIDI data to the virtual destination.

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
- [func MIDIGetDestination(Int) -> MIDIEndpointRef](./midigetdestination%28_%29.md)
  Returns a destination in the system.
- [func MIDIGetNumberOfDestinations() -> Int](./midigetnumberofdestinations%28%29.md)
  Returns the number of destinations in the system.
- [typealias MIDIEndpointRef](./midiendpointref.md)
  A MIDI source or destination an entity owns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/mididestinationcreatewithprotocol(_:_:_:_:_:))*