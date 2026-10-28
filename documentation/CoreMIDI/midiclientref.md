# MIDIClientRef

**Framework**: Core MIDI  
**Kind**: typealias  
**Role**: Type Alias

An object that maintains per-client state.

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
typealias MIDIClientRef = MIDIObjectRef
```

```c
typedef MIDIObjectRef MIDIClientRef;
```

## Discussion

A client object derives from [`MIDIObjectRef`](./midiobjectref.md). It doesn’t have an owning object.

## See Also

### Client management
- [Incorporating MIDI 2 into your apps](./incorporating-midi-2-into-your-apps.md)
  Add precision and improve musical control for your MIDI apps.
- [func MIDIClientCreate(CFString, MIDINotifyProc?, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIClientRef>) -> OSStatus](./midiclientcreate%28_,_,_,_%29.md)
  Creates a MIDI client.
- [func MIDIClientCreateWithBlock(CFString, UnsafeMutablePointer<MIDIClientRef>, MIDINotifyBlock?) -> OSStatus](./midiclientcreatewithblock%28_,_,_%29.md)
  Creates a MIDI client with a callback block.
- [func MIDIClientDispose(MIDIClientRef) -> OSStatus](./midiclientdispose%28_%29.md)
  Disposes of a MIDI client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiclientref)*