# AudioFileComponentGetGlobalInfoSizeProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AudioFileComponentGetGlobalInfoSizeProc = (UnsafeMutableRawPointer, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
typedef int (*)(void *, unsigned int, unsigned int, const void *, unsigned int *) AudioFileComponentGetGlobalInfoSizeProc;
```

## See Also

### Getting the Global Information
- [func AudioFileComponentGetGlobalInfo(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetglobalinfo%28_,_,_,_,_,_%29.md)
- [func AudioFileComponentGetGlobalInfoSize(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentgetglobalinfosize%28_,_,_,_,_%29.md)
- [typealias AudioFileComponentGetGlobalInfoProc](./audiofilecomponentgetglobalinfoproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetglobalinfosizeproc)*