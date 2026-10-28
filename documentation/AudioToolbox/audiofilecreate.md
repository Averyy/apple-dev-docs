# AudioFileCreate

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.2+ - Deprecated in 10.6

> **Deprecated**: Deprecated. Use [`AudioFileCreateWithURL(_:_:_:_:_:)`](./audiofilecreatewithurl%28_,_,_,_,_%29.md) instead.

## Declaration

```c
extern OSStatus AudioFileCreate(const struct FSRef *inParentRef, CFStringRef inFileName, AudioFileTypeID inFileType, const AudioStreamBasicDescription *inFormat, AudioFileFlags inFlags, struct FSRef *outNewFileRef, AudioFileID*outAudioFile);
```

## Return Value

A result code. See Result Codes.

## Discussion

This deprecated function uses an `FSRef` type rather than the `CFURLRef` type used by the [`AudioFileCreateWithURL(_:_:_:_:_:)`](./audiofilecreatewithurl%28_,_,_,_,_%29.md) function.

## Parameters

- `inParentRef`: A pointer to the directory where the new file should be created.
- `inFileName`: The name of the file to be created.
- `inFileType`: The type of audio file to create. See [`AudioFileTypeID`](./audiofiletypeid.md) for constants that can be used.
- `inFormat`: A pointer to the structure that describes the format of the data.
- `inFlags`: Relevant flags for creating or opening the file. Currently set to `0`.
- `outNewFileRef`: On output, a pointer to the location of the newly created file.
- `outAudioFile`: On output, a pointer to the newly created audio file.

## See Also

### Related Documentation
- [func AudioFileCreateWithURL(CFURL, AudioFileTypeID, UnsafePointer<AudioStreamBasicDescription>, AudioFileFlags, UnsafeMutablePointer<AudioFileID?>) -> OSStatus](./audiofilecreatewithurl%28_,_,_,_,_%29.md)
  Creates a new audio file, or initializes an existing file, specified by a URL.
### Functions
- [AudioFileInitialize](./audiofileinitialize.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecreate)*