# MusicDeviceStopNote(_:_:_:_:)

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
func MusicDeviceStopNote(_ inUnit: MusicDeviceComponent, _ inGroupID: MusicDeviceGroupID, _ inNoteInstanceID: NoteInstanceID, _ inOffsetSampleFrame: UInt32) -> OSStatus
```

## See Also

- [func MusicDeviceMIDIEvent(MusicDeviceComponent, UInt32, UInt32, UInt32, UInt32) -> OSStatus](musicdevicemidievent(_:_:_:_:_:).md)
- [func MusicDeviceMIDIEventList(MusicDeviceComponent, UInt32, UnsafePointer<MIDIEventList>) -> OSStatus](musicdevicemidieventlist(_:_:_:).md)
- [func MusicDeviceStartNote(MusicDeviceComponent, MusicDeviceInstrumentID, MusicDeviceGroupID, UnsafeMutablePointer<NoteInstanceID>, UInt32, UnsafePointer<MusicDeviceNoteParams>) -> OSStatus](musicdevicestartnote(_:_:_:_:_:_:).md)
- [func MusicDeviceSysEx(MusicDeviceComponent, UnsafePointer<UInt8>, UInt32) -> OSStatus](musicdevicesysex(_:_:_:).md)
- [typealias MusicDeviceComponent](musicdevicecomponent.md)
- [typealias MusicDeviceGroupID](musicdevicegroupid.md)
- [typealias MusicDeviceInstrumentID](musicdeviceinstrumentid.md)
- [typealias MusicDeviceMIDIEventProc](musicdevicemidieventproc.md)
- [typealias MusicDeviceStartNoteProc](musicdevicestartnoteproc.md)
- [typealias MusicDeviceStopNoteProc](musicdevicestopnoteproc.md)
- [typealias MusicDeviceSysExProc](musicdevicesysexproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicdevicestopnote(_:_:_:_:))*