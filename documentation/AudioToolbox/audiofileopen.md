# AudioFileOpen

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.2+ - Deprecated in 10.6

> **Deprecated**: Deprecated. Use [`AudioFileOpenURL(_:_:_:_:)`](./audiofileopenurl%28_,_,_,_%29.md) instead.

## Declaration

```c
extern OSStatus AudioFileOpen(const struct FSRef *inFileRef, AudioFilePermissions inPermissions, AudioFileTypeID inFileTypeHint, AudioFileID*outAudioFile);
```

#### Return Value

A result code. See Result Codes.

#### Discussion

This deprecated function opens an existing audio file specified by a file system reference.

## Parameters

- `inFileRef`: A pointer to the audio file you want to open.
- `inPermissions`: The read-write permissions you want to assign to the file. Use the permission constants in [`AudioFilePermissions`](./audiofilepermissions.md).
- `inFileTypeHint`: A hint to indicate the file type of the designated file. For files without filename extensions and with types not easily or uniquely determined from the data (such as ADTS,AC3), use this hint to indicate the file type. Otherwise, pass `0`. Only use this hint in macOS versions 10.3.1 or greater. In all earlier versions, any attempt to open these files fails.
- `outAudioFile`: On output, a pointer to the newly opened file.

## See Also

### Related Documentation
- [func AudioFileOpenURL(CFURL, AudioFilePermissions, AudioFileTypeID, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](./audiofileopenurl%28_,_,_,_%29.md)
  Open an existing audio file specified by a URL.
### Functions
- [AudioFileCreate](./audiofilecreate.md)
- [AudioFileInitialize](./audiofileinitialize.md)
- [func AudioFileReadPackets(AudioFileID, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](./audiofilereadpackets%28_,_,_,_,_,_,_%29.md)
  Reads a fixed duration of audio data from an audio file.
- [MusicSequenceLoadSMFDataWithFlags](./musicsequenceloadsmfdatawithflags.md)
- [MusicSequenceLoadSMFWithFlags](./musicsequenceloadsmfwithflags.md)
- [MusicSequenceSaveMIDIFile](./musicsequencesavemidifile.md)
- [MusicSequenceSaveSMFData](./musicsequencesavesmfdata.md)
- [MusicTrackNewExtendedControlEvent](./musictracknewextendedcontrolevent.md)
- [func AudioComponentGetIcon(AudioComponent, Float) -> UIImage?](./audiocomponentgeticon%28_,_%29.md)
  The UIImage of the audio component’s icon.
- [func AudioComponentGetLastActiveTime(AudioComponent) -> CFAbsoluteTime](./audiocomponentgetlastactivetime%28_%29.md)
  The time at which the application publishing the component was last active.
- [AudioFileComponentCreate](./audiofilecomponentcreate.md)
- [AudioFileComponentDataIsThisFormat](./audiofilecomponentdataisthisformat.md)
- [AudioFileComponentFileIsThisFormat](./audiofilecomponentfileisthisformat.md)
- [AudioFileComponentInitialize](./audiofilecomponentinitialize.md)
- [AudioFileComponentOpenFile](./audiofilecomponentopenfile.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileopen)*