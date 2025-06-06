# MIDISourceCreateWithProtocol(_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Creates a virtual source in a client.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func MIDISourceCreateWithProtocol(_ client: MIDIClientRef, _ name: CFString, _ protocol: MIDIProtocolID, _ outSrc: UnsafeMutablePointer<MIDIEndpointRef>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

Drivers don’t need to call this function. When they create devices and entities, the system automatically creates sources and destinations at that time. After creating a virtual source, use [`MIDIReceivedEventList(_:_:)`](midireceivedeventlist(_:_:).md) to transmit MIDI messages from your virtual source to any clients connected to the virtual source.

> 💡 **Tip**:  After creating a virtual source, assign it the same unique ID it had the last time your app created it. Doing so permits other clients to retain persistent references to your virtual source.

 After creating a virtual source, assign it the same unique ID it had the last time your app created it. Doing so permits other clients to retain persistent references to your virtual source.

## Parameters

- `client`: The client to own the virtual source.
- `name`: The name of the virtual source.
- `protocol`: The MIDI protocol variant to send from this source. The system automatically converts messages from this protocol to the protocol of the destination.
- `outSrc`: On successful return, a pointer to the newly created source.

## See Also

- [func MIDIEndpointDispose(MIDIEndpointRef) -> OSStatus](midiendpointdispose(_:).md)
  Disposes of a virtual source or destination.
- [func MIDIEndpointGetEntity(MIDIEndpointRef, UnsafeMutablePointer<MIDIEntityRef>?) -> OSStatus](midiendpointgetentity(_:_:).md)
  Returns an endpoint’s entity.
- [func MIDIEndpointGetRefCons(MIDIEndpointRef, UnsafeMutablePointer<UnsafeMutableRawPointer>?, UnsafeMutablePointer<UnsafeMutableRawPointer>?) -> OSStatus](midiendpointgetrefcons(_:_:_:).md)
  Returns contextual data assigned to an endpoint.
- [func MIDIEndpointSetRefCons(MIDIEndpointRef, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> OSStatus](midiendpointsetrefcons(_:_:_:).md)
  Sets contextual data on an endpoint.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midisourcecreatewithprotocol(_:_:_:_:))*