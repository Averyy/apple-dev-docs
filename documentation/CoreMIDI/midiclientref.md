# MIDIClientRef

**Framework**: Core MIDI  
**Kind**: typealias

An object that maintains per-client state.

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
typealias MIDIClientRef = MIDIObjectRef
```

#### Discussion

A client object derives from [`MIDIObjectRef`](midiobjectref.md). It doesn’t have an owning object.

## See Also

- [Incorporating MIDI 2 into your apps](incorporating-midi-2-into-your-apps.md)
  Add precision and improve musical control for your MIDI apps.
- [func MIDIClientCreate(CFString, MIDINotifyProc?, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIClientRef>) -> OSStatus](midiclientcreate(_:_:_:_:).md)
  Creates a MIDI client.
- [func MIDIClientCreateWithBlock(CFString, UnsafeMutablePointer<MIDIClientRef>, MIDINotifyBlock?) -> OSStatus](midiclientcreatewithblock(_:_:_:).md)
  Creates a MIDI client with a callback block.
- [func MIDIClientDispose(MIDIClientRef) -> OSStatus](midiclientdispose(_:).md)
  Disposes of a MIDI client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiclientref)*