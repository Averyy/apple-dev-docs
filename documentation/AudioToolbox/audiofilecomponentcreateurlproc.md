# AudioFileComponentCreateURLProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AudioFileComponentCreateURLProc = (UnsafeMutableRawPointer, CFURL, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus
```

```c
typedef int (*)(void *, const struct __CFURL *, const struct AudioStreamBasicDescription *, unsigned int) AudioFileComponentCreateURLProc;
```

## See Also

### Opening and Closing Audio Files
- [func AudioFileComponentCreateURL(AudioFileComponent, CFURL, UnsafePointer<AudioStreamBasicDescription>, UInt32) -> OSStatus](./audiofilecomponentcreateurl%28_,_,_,_%29.md)
- [func AudioFileComponentOpenURL(AudioFileComponent, CFURL, Int8, Int32) -> OSStatus](./audiofilecomponentopenurl%28_,_,_,_%29.md)
- [func AudioFileComponentOpenWithCallbacks(AudioFileComponent, UnsafeMutableRawPointer, AudioFile_ReadProc, AudioFile_WriteProc, AudioFile_GetSizeProc, AudioFile_SetSizeProc) -> OSStatus](./audiofilecomponentopenwithcallbacks%28_,_,_,_,_,_%29.md)
- [func AudioFileComponentCloseFile(AudioFileComponent) -> OSStatus](./audiofilecomponentclosefile%28_%29.md)
- [func AudioFileComponentOptimize(AudioFileComponent) -> OSStatus](./audiofilecomponentoptimize%28_%29.md)
- [typealias AudioFileComponent](./audiofilecomponent.md)
- [typealias AudioFileComponentPropertyID](./audiofilecomponentpropertyid.md)
- [typealias AudioFileComponentOpenWithCallbacksProc](./audiofilecomponentopenwithcallbacksproc.md)
- [typealias AudioFileComponentOpenURLProc](./audiofilecomponentopenurlproc.md)
- [typealias AudioFileComponentCloseProc](./audiofilecomponentcloseproc.md)
- [typealias AudioFileComponentOptimizeProc](./audiofilecomponentoptimizeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentcreateurlproc)*