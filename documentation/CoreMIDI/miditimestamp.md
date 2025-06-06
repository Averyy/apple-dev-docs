# MIDITimeStamp

**Framework**: Core MIDI  
**Kind**: typealias

The time on the host clock when the event occurred.

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
typealias MIDITimeStamp = UInt64
```

#### Discussion

The system determines the timestamp using `mach_absolute_time()`.

## See Also

- [func MIDIPacketNext(UnsafePointer<MIDIPacket>) -> UnsafeMutablePointer<MIDIPacket>](midipacketnext(_:).md)
  Advances a MIDI packet pointer to the next packet in a package list.
- [struct MIDIPacket](midipacket.md)
  A collection of simultaneous MIDI events.
- [struct MIDIPacketList](midipacketlist.md)
  A list of MIDI events the system sends to or receives from an endpoint.
- [struct UnsafeMutableMIDIPacketListPointer](unsafemutablemidipacketlistpointer.md)
- [struct UnsafeMutableMIDIPacketPointer](unsafemutablemidipacketpointer.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/miditimestamp)*