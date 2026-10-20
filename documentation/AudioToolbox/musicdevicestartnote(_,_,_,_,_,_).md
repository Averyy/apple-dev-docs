# MusicDeviceStartNote(_:_:_:_:_:_:)

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
func MusicDeviceStartNote(_ inUnit: MusicDeviceComponent, _ inInstrument: MusicDeviceInstrumentID, _ inGroupID: MusicDeviceGroupID, _ outNoteInstanceID: UnsafeMutablePointer<NoteInstanceID>, _ inOffsetSampleFrame: UInt32, _ inParams: UnsafePointer<MusicDeviceNoteParams>) -> OSStatus
```

```c
extern OSStatus MusicDeviceStartNote(MusicDeviceComponent inUnit, MusicDeviceInstrumentID inInstrument, MusicDeviceGroupID inGroupID, NoteInstanceID *outNoteInstanceID, UInt32 inOffsetSampleFrame, const MusicDeviceNoteParams *inParams);
```

## See Also

### Interacting with Music Devices
- [func MusicDeviceMIDIEvent(MusicDeviceComponent, UInt32, UInt32, UInt32, UInt32) -> OSStatus](./musicdevicemidievent%28_,_,_,_,_%29.md)
- [func MusicDeviceMIDIEventList(MusicDeviceComponent, UInt32, UnsafePointer<MIDIEventList>) -> OSStatus](./musicdevicemidieventlist%28_,_,_%29.md)
- [func MusicDeviceStopNote(MusicDeviceComponent, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus](./musicdevicestopnote%28_,_,_,_%29.md)
- [func MusicDeviceSysEx(MusicDeviceComponent, UnsafePointer<UInt8>, UInt32) -> OSStatus](./musicdevicesysex%28_,_,_%29.md)
- [typealias MusicDeviceComponent](./musicdevicecomponent.md)
- [typealias MusicDeviceGroupID](./musicdevicegroupid.md)
- [typealias MusicDeviceInstrumentID](./musicdeviceinstrumentid.md)
- [typealias MusicDeviceMIDIEventProc](./musicdevicemidieventproc.md)
- [typealias MusicDeviceStartNoteProc](./musicdevicestartnoteproc.md)
- [typealias MusicDeviceStopNoteProc](./musicdevicestopnoteproc.md)
- [typealias MusicDeviceSysExProc](./musicdevicesysexproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicdevicestartnote(_:_:_:_:_:_:))*