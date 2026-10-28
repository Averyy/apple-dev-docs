# AudioFileInitialize

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.2+ - Deprecated in 10.6

> **Deprecated**: Deprecated. Use [`AudioFileInitializeWithCallbacks(_:_:_:_:_:_:_:_:_:)`](./audiofileinitializewithcallbacks%28_,_,_,_,_,_,_,_,_%29.md) instead.

## Declaration

```c
extern OSStatus AudioFileInitialize(const struct FSRef *inFileRef, AudioFileTypeID inFileType, const AudioStreamBasicDescription *inFormat, AudioFileFlags inFlags, AudioFileID*outAudioFile);
```

## Return Value

A result code. See Result Codes.

## Discussion

This deprecated function deletes the content of an existing audio file to let you write over it.

## Parameters

- `inFileRef`: A pointer to the audio file you want to initialize.
- `inFileType`: The type of audio file to initialize the file to.
- `inFormat`: A pointer to the structure that describes the format of the data.
- `inFlags`: Flags for creating or opening the file. Currently set to `0`.
- `outAudioFile`: On output, a pointer to the newly created audio file.

## See Also

### Functions
- [AudioFileCreate](./audiofilecreate.md)
- [AudioFileOpen](./audiofileopen.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileinitialize)*