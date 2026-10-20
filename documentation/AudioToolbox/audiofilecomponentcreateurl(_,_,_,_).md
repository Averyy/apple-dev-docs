# AudioFileComponentCreateURL(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func AudioFileComponentCreateURL(_ inComponent: AudioFileComponent, _ inFileRef: CFURL, _ inFormat: UnsafePointer<AudioStreamBasicDescription>, _ inFlags: UInt32) -> OSStatus
```

```c
extern OSStatus AudioFileComponentCreateURL(AudioFileComponent inComponent, CFURLRef inFileRef, const AudioStreamBasicDescription *inFormat, UInt32 inFlags);
```

## See Also

### Opening and Closing Audio Files
- [func AudioFileComponentOpenURL(AudioFileComponent, CFURL, Int8, Int32) -> OSStatus](./audiofilecomponentopenurl%28_,_,_,_%29.md)
- [func AudioFileComponentOpenWithCallbacks(AudioFileComponent, UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc) -> OSStatus](./audiofilecomponentopenwithcallbacks%28_,_,_,_,_,_%29.md)
- [func AudioFileComponentCloseFile(AudioFileComponent) -> OSStatus](./audiofilecomponentclosefile%28_%29.md)
- [func AudioFileComponentOptimize(AudioFileComponent) -> OSStatus](./audiofilecomponentoptimize%28_%29.md)
- [typealias AudioFileComponent](./audiofilecomponent.md)
- [typealias AudioFileComponentPropertyID](./audiofilecomponentpropertyid.md)
- [typealias AudioFileComponentCreateURLProc](./audiofilecomponentcreateurlproc.md)
- [typealias AudioFileComponentOpenWithCallbacksProc](./audiofilecomponentopenwithcallbacksproc.md)
- [typealias AudioFileComponentOpenURLProc](./audiofilecomponentopenurlproc.md)
- [typealias AudioFileComponentCloseProc](./audiofilecomponentcloseproc.md)
- [typealias AudioFileComponentOptimizeProc](./audiofilecomponentoptimizeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentcreateurl(_:_:_:_:))*