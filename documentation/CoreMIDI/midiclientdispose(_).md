# MIDIClientDispose(_:)

**Framework**: Core MIDI  
**Kind**: func  
**Role**: Function

Disposes of a MIDI client.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- macOS 10.0+
- visionOS 1.0+

## Declaration

```swift
func MIDIClientDispose(_ client: MIDIClientRef) -> OSStatus
```

```c
extern OSStatus MIDIClientDispose(MIDIClientRef client);
```

## Return Value

An `OSStatus` result code.

## Discussion

Don’t explicitly dispose of your client; the system automatically disposes all clients when an app terminates. However, if you call this method to dispose the last or only client owned by an app, the MIDI server may exit if there are no other clients remaining in the system. If this occurs, all subsequent calls by your app to [`MIDIClientCreate(_:_:_:_:)`](./midiclientcreate%28_,_,_,_%29.md) and [`MIDIClientCreateWithBlock(_:_:_:)`](./midiclientcreatewithblock%28_,_,_%29.md) fail.

## Parameters

- `client`: The client to dispose of.

## See Also

### Client management
- [Incorporating MIDI 2 into your apps](./incorporating-midi-2-into-your-apps.md)
  Add precision and improve musical control for your MIDI apps.
- [func MIDIClientCreate(CFString, MIDINotifyProc?, UnsafeMutableRawPointer?, UnsafeMutablePointer<MIDIClientRef>) -> OSStatus](./midiclientcreate%28_,_,_,_%29.md)
  Creates a MIDI client.
- [func MIDIClientCreateWithBlock(CFString, UnsafeMutablePointer<MIDIClientRef>, MIDINotifyBlock?) -> OSStatus](./midiclientcreatewithblock%28_,_,_%29.md)
  Creates a MIDI client with a callback block.
- [typealias MIDIClientRef](./midiclientref.md)
  An object that maintains per-client state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremidi/midiclientdispose(_:))*