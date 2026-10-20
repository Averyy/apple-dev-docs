# MusicDeviceStartNote(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

## See Also

- [func MusicDeviceMIDIEvent(MusicDeviceComponent, UInt32, UInt32, UInt32, UInt32) -> OSStatus](musicdevicemidievent(_:_:_:_:_:).md)
- [func MusicDeviceMIDIEventList(MusicDeviceComponent, UInt32, UnsafePointer<MIDIEventList>) -> OSStatus](musicdevicemidieventlist(_:_:_:).md)
- [func MusicDeviceStopNote(MusicDeviceComponent, MusicDeviceGroupID, NoteInstanceID, UInt32) -> OSStatus](musicdevicestopnote(_:_:_:_:).md)
- [func MusicDeviceSysEx(MusicDeviceComponent, UnsafePointer<UInt8>, UInt32) -> OSStatus](musicdevicesysex(_:_:_:).md)
- [typealias MusicDeviceComponent](musicdevicecomponent.md)
- [typealias MusicDeviceGroupID](musicdevicegroupid.md)
- [typealias MusicDeviceInstrumentID](musicdeviceinstrumentid.md)
- [typealias MusicDeviceMIDIEventProc](musicdevicemidieventproc.md)
- [typealias MusicDeviceStartNoteProc](musicdevicestartnoteproc.md)
- [typealias MusicDeviceStopNoteProc](musicdevicestopnoteproc.md)
- [typealias MusicDeviceSysExProc](musicdevicesysexproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicdevicestartnote(_:_:_:_:_:_:))*