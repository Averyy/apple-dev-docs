# MIDIClientCreateWithBlock(_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Creates a MIDI client with a callback block.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- visionOS 1.0+

## Declaration

```swift
func MIDIClientCreateWithBlock(_ name: CFString, _ outClient: UnsafeMutablePointer<MIDIClientRef>, _ notifyBlock: MIDINotifyBlock?) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

## Parameters

- `name`: The client’s name.
- `outClient`: On successful return, points to the newly created MIDI client.
- `notifyBlock`: An optional block on which the client receives notifications of changes to the system. This system calls this block on an arbitrary thread. Thread-safety is the block’s responsibility.

## Topics

### Callbacks
- [typealias MIDINotifyBlock](midinotifyblock.md)
  A callback block for notifying clients of state changes.
- [struct MIDINotification](midinotification.md)
  A message that describes a system state change.

## See Also

- [Incorporating MIDI 2 into your apps](incorporating-midi-2-into-your-apps.md)
  Add precision and improve musical control for your MIDI apps.
- [func MIDIClientCreate(CFString, MIDINotifyProc?, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIClientRef>) -> OSStatus](midiclientcreate(_:_:_:_:).md)
  Creates a MIDI client.
- [func MIDIClientDispose(MIDIClientRef) -> OSStatus](midiclientdispose(_:).md)
  Disposes of a MIDI client.
- [typealias MIDIClientRef](midiclientref.md)
  An object that maintains per-client state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiclientcreatewithblock(_:_:_:))*