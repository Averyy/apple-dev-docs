# MusicDeviceMIDIEventProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
typealias MusicDeviceMIDIEventProc = (UnsafeMutableRawPointer, UInt32, UInt32, UInt32, UInt32) -> OSStatus
```

```c
typedef int (*)(void *, unsigned int, unsigned int, unsigned int, unsigned int) __attribute__((nonblocking)) MusicDeviceMIDIEventProc;
```

## See Also

### Interacting with Music Devices
- [func MusicDeviceMIDIEvent(MusicDeviceComponent, UInt32, UInt32, UInt32, UInt32) -> OSStatus](./musicdevicemidievent%28_,_,_,_,_%29.md)
- [func MusicDeviceMIDIEventList(MusicDeviceComponent, UInt32, UnsafePointer<MIDIEventList>) -> OSStatus](./musicdevicemidieventlist%28_,_,_%29.md)
- [func MusicDeviceStartNote(MusicDeviceComponent, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafeMutablePointer<NoteInstanceID>, UInt32, UnsafePointer<MusicDeviceNoteParams>) -> OSStatus](./musicdevicestartnote%28_,_,_,_,_,_%29.md)
- [func MusicDeviceStopNote(MusicDeviceComponent, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus](./musicdevicestopnote%28_,_,_,_%29.md)
- [func MusicDeviceSysEx(MusicDeviceComponent, UnsafePointer<UInt8>, UInt32) -> OSStatus](./musicdevicesysex%28_,_,_%29.md)
- [typealias MusicDeviceComponent](./musicdevicecomponent.md)
- [typealias MusicDeviceGroupID](./musicdevicegroupid.md)
- [typealias MusicDeviceInstrumentID](./musicdeviceinstrumentid.md)
- [typealias MusicDeviceStartNoteProc](./musicdevicestartnoteproc.md)
- [typealias MusicDeviceStopNoteProc](./musicdevicestopnoteproc.md)
- [typealias MusicDeviceSysExProc](./musicdevicesysexproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicdevicemidieventproc)*