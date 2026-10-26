# MusicSequenceLoadSMFDataWithFlags

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.3+ - Deprecated in 10.5

## Declaration

```c
extern OSStatus MusicSequenceLoadSMFDataWithFlags(MusicSequence inSequence, CFDataRef inData, MusicSequenceLoadFlags inFlags);
```

## See Also

### Functions
- [AudioFileCreate](./audiofilecreate.md)
- [AudioFileInitialize](./audiofileinitialize.md)
- [AudioFileOpen](./audiofileopen.md)
- [func AudioFileReadPackets(AudioFileID, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](./audiofilereadpackets%28_,_,_,_,_,_,_%29.md)
  Reads a fixed duration of audio data from an audio file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/musicsequenceloadsmfdatawithflags)*