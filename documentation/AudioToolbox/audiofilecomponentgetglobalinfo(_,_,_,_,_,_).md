# AudioFileComponentGetGlobalInfo(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentGetGlobalInfo(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

```c
extern OSStatus AudioFileComponentGetGlobalInfo(AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 inSpecifierSize, const void *inSpecifier, UInt32 *ioPropertyDataSize, void *outPropertyData);
```

## See Also

### Getting the Global Information
- [func AudioFileComponentGetGlobalInfoSize(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentgetglobalinfosize%28_,_,_,_,_%29.md)
- [typealias AudioFileComponentGetGlobalInfoProc](./audiofilecomponentgetglobalinfoproc.md)
- [typealias AudioFileComponentGetGlobalInfoSizeProc](./audiofilecomponentgetglobalinfosizeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetglobalinfo(_:_:_:_:_:_:))*