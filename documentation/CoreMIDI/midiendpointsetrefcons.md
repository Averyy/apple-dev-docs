# MIDIEndpointSetRefCons(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Sets contextual data on an endpoint.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIEndpointSetRefCons(_ endpt: MIDIEndpointRef, _ ref1: UnsafeMutableRawPointer?, _ ref2: UnsafeMutableRawPointer?) -> OSStatus
```

#### Return Value

An OSStatus result code.

#### Discussion

Drivers need an efficient way to translate from a [`MIDIEndpointRef`](midiendpointref.md) (source or destination) to their own internal data structures corresponding to that endpoint. This function provides a way for the driver to assign its own data to endpoints.

The data you set isn’t persistent and needs to be reintialized in each call to [`Start`](mididriverinterface/start.md).

A typical use is for one `refCon` to refer to a device, and a second to refer to a port on the device.

## Parameters

- `endpt`: The endpoint to set the data on.
- `ref1`: The first  .
- `ref2`: The second  .

## See Also

- [func MIDIEndpointDispose(MIDIEndpointRef) -> OSStatus](midiendpointdispose(_:).md)
  Disposes of a virtual source or destination.
- [func MIDIEndpointGetEntity(MIDIEndpointRef, UnsafeMutablePointer<MIDIEntityRef>?) -> OSStatus](midiendpointgetentity(_:_:).md)
  Returns an endpoint’s entity.
- [func MIDIEndpointGetRefCons(MIDIEndpointRef, UnsafeMutablePointer<UnsafeMutableRawPointer>?, UnsafeMutablePointer<UnsafeMutableRawPointer>?) -> OSStatus](midiendpointgetrefcons(_:_:_:).md)
  Returns contextual data assigned to an endpoint.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiendpointsetrefcons(_:_:_:))*