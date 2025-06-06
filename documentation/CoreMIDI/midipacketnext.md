# MIDIPacketNext(_:)

**Framework**: Core MIDI  
**Kind**: func

Advances a MIDI packet pointer to the next packet in a package list.

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
func MIDIPacketNext(_ pkt: UnsafePointer<MIDIPacket>) -> UnsafeMutablePointer<MIDIPacket>
```

#### Return Value

The subsequent packet in the [`MIDIPacketList`](midipacketlist.md).

## Parameters

- `pkt`: A pointer to a MIDI packet in a MIDI packet list.

## See Also

- [struct MIDIPacket](midipacket.md)
  A collection of simultaneous MIDI events.
- [struct MIDIPacketList](midipacketlist.md)
  A list of MIDI events the system sends to or receives from an endpoint.
- [typealias MIDITimeStamp](miditimestamp.md)
  The time on the host clock when the event occurred.
- [struct UnsafeMutableMIDIPacketListPointer](unsafemutablemidipacketlistpointer.md)
- [struct UnsafeMutableMIDIPacketPointer](unsafemutablemidipacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midipacketnext(_:))*