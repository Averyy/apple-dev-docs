# AudioFileComponentOpenURL(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.5+

## Declaration

```swift
func AudioFileComponentOpenURL(_ inComponent: AudioFileComponent, _ inFileRef: CFURL, _ inPermissions: Int8, _ inFileDescriptor: Int32) -> OSStatus
```

```c
extern OSStatus AudioFileComponentOpenURL(AudioFileComponent inComponent, CFURLRef inFileRef, SInt8 inPermissions, int inFileDescriptor);
```

## See Also

### Opening and Closing Audio Files
- [func AudioFileComponentCreateURL(AudioFileComponent, CFURL, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus](./audiofilecomponentcreateurl%28_,_,_,_%29.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentopenurl(_:_:_:_:))*