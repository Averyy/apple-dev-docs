# MusicDeviceStopNote(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func MusicDeviceStopNote(_ inUnit: MusicDeviceComponent, _ inGroupID: MusicDeviceGroupID, _ inNoteInstanceID: NoteInstanceID, _ inOffsetSampleFrame: UInt32) -> OSStatus
```

```c
extern OSStatus MusicDeviceStopNote(MusicDeviceComponent inUnit, MusicDeviceGroupID inGroupID, NoteInstanceID inNoteInstanceID, UInt32 inOffsetSampleFrame);
```

## See Also

### Interacting with Music Devices
- [func MusicDeviceMIDIEvent(MusicDeviceComponent, UInt32, UInt32, UInt32, UInt32) -> OSStatus](./musicdevicemidievent%28_,_,_,_,_%29.md)
- [func MusicDeviceMIDIEventList(MusicDeviceComponent, UInt32, UnsafePointer<MIDIEventList>) -> OSStatus](./musicdevicemidieventlist%28_,_,_%29.md)
- [func MusicDeviceStartNote(MusicDeviceComponent, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafeMutablePointer<NoteInstanceID>, UInt32, UnsafePointer<MusicDeviceNoteParams>) -> OSStatus](./musicdevicestartnote%28_,_,_,_,_,_%29.md)
- [func MusicDeviceSysEx(MusicDeviceComponent, UnsafePointer<UInt8>, UInt32) -> OSStatus](./musicdevicesysex%28_,_,_%29.md)
- [typealias MusicDeviceComponent](./musicdevicecomponent.md)
- [typealias MusicDeviceGroupID](./musicdevicegroupid.md)
- [typealias MusicDeviceInstrumentID](./musicdeviceinstrumentid.md)
- [typealias MusicDeviceMIDIEventProc](./musicdevicemidieventproc.md)
- [typealias MusicDeviceStartNoteProc](./musicdevicestartnoteproc.md)
- [typealias MusicDeviceStopNoteProc](./musicdevicestopnoteproc.md)
- [typealias MusicDeviceSysExProc](./musicdevicesysexproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicdevicestopnote(_:_:_:_:))*