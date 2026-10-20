# AudioFileComponentOpenWithCallbacks(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentOpenWithCallbacks(_ inComponent: AudioFileComponent, _ inClientData: UnsafeMutableRawPointer, _ inReadFunc: AudioFile_ReadProc, _ inWriteFunc: AudioFile_WriteProc, _ inGetSizeFunc: AudioFile_GetSizeProc, _ inSetSizeFunc: AudioFile_SetSizeProc) -> OSStatus
```

```c
extern OSStatus AudioFileComponentOpenWithCallbacks(AudioFileComponent inComponent, void *inClientData, AudioFile_ReadProc inReadFunc, AudioFile_WriteProc inWriteFunc, AudioFile_GetSizeProc inGetSizeFunc, AudioFile_SetSizeProc inSetSizeFunc);
```

## See Also

### Opening and Closing Audio Files
- [func AudioFileComponentCreateURL(AudioFileComponent, CFURL, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus](./audiofilecomponentcreateurl%28_,_,_,_%29.md)
- [func AudioFileComponentOpenURL(AudioFileComponent, CFURL, Int8, Int32) -> OSStatus](./audiofilecomponentopenurl%28_,_,_,_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentopenwithcallbacks(_:_:_:_:_:_:))*