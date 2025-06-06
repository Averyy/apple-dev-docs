# MIDIEndpointGetRefCons(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Returns contextual data assigned to an endpoint.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIEndpointGetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafeMutablePointer<UnsafeMutableRawPointer>?, _ ref2: UnsafeMutablePointer<UnsafeMutableRawPointer>?) -> OSStatus
```

#### Return Value

An OSStatus result code.

## Parameters

- `endpt`: The endpoint with the   to return.
- `ref1`: On exit, the first  .
- `ref2`: On exit, the second  .

## See Also

- [func MIDIEndpointDispose(MIDIEndpointRef) -> OSStatus](midiendpointdispose(_:).md)
  Disposes of a virtual source or destination.
- [func MIDIEndpointGetEntity(MIDIEndpointRef, UnsafeMutablePointer<MIDIEntityRef>?) -> OSStatus](midiendpointgetentity(_:_:).md)
  Returns an endpoint’s entity.
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
- [typealias MIDIEndpointRef](midiendpointref.md)
  A MIDI source or destination an entity owns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiendpointgetrefcons(_:_:_:))*