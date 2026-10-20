# AudioFileComponentGetGlobalInfoProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AudioFileComponentGetGlobalInfoProc = (UnsafeMutableRawPointer, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus
```

```c
typedef int (*)(void *, unsigned int, unsigned int, const void *, unsigned int *, void *) AudioFileComponentGetGlobalInfoProc;
```

## See Also

### Getting the Global Information
- [func AudioFileComponentGetGlobalInfo(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetglobalinfo%28_,_,_,_,_,_%29.md)
- [func AudioFileComponentGetGlobalInfoSize(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentgetglobalinfosize%28_,_,_,_,_%29.md)
- [typealias AudioFileComponentGetGlobalInfoSizeProc](./audiofilecomponentgetglobalinfosizeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetglobalinfoproc)*