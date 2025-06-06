# MIDIClientCreate(_:_:_:_:)

**Framework**: Core MIDI  
**Kind**: func

Creates a MIDI client.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIClientCreate(_ name: CFString, _ notifyProc: MIDINotifyProc?, _ notifyRefCon: UnsafeMutableRawPointer?, _ outClient: UnsafeMutablePointer<MIDIClientRef>) -> OSStatus
```

#### Return Value

An `OSStatus` result code.

#### Discussion

The system invokes the callback function on the same run loop that you created the client on.

## Parameters

- `name`: The client’s name.
- `notifyProc`: An optional callback function through which the client receives notifications of changes to the system.
- `notifyRefCon`: A void pointer.
- `outClient`: On successful return, points to the newly created MIDI client.

## Topics

### Callbacks
- [typealias MIDINotifyProc](midinotifyproc.md)
  A callback function for notifying clients of state changes.
- [struct MIDINotification](midinotification.md)
  A message that describes a system state change.

## See Also

- [Incorporating MIDI 2 into your apps](incorporating-midi-2-into-your-apps.md)
  Add precision and improve musical control for your MIDI apps.
- [func MIDIClientCreateWithBlock(CFString, UnsafeMutablePointer<MIDIClientRef>, MIDINotifyBlock?) -> OSStatus](midiclientcreatewithblock(_:_:_:).md)
  Creates a MIDI client with a callback block.
- [func MIDIClientDispose(MIDIClientRef) -> OSStatus](midiclientdispose(_:).md)
  Disposes of a MIDI client.
- [typealias MIDIClientRef](midiclientref.md)
  An object that maintains per-client state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiclientcreate(_:_:_:_:))*