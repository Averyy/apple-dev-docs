# AudioFileComponentGetGlobalInfoSize(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentGetGlobalInfoSize(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ outPropertySize: UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
extern OSStatus AudioFileComponentGetGlobalInfoSize(AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 inSpecifierSize, const void *inSpecifier, UInt32 *outPropertySize);
```

## See Also

### Getting the Global Information
- [func AudioFileComponentGetGlobalInfo(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetglobalinfo%28_,_,_,_,_,_%29.md)
- [typealias AudioFileComponentGetGlobalInfoProc](./audiofilecomponentgetglobalinfoproc.md)
- [typealias AudioFileComponentGetGlobalInfoSizeProc](./audiofilecomponentgetglobalinfosizeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetglobalinfosize(_:_:_:_:_:))*