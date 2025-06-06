# AudioFileComponentGetGlobalInfo(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentGetGlobalInfo(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func AudioFileComponentGetGlobalInfoSize(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentgetglobalinfosize(_:_:_:_:_:).md)
- [typealias AudioFileComponentGetGlobalInfoProc](audiofilecomponentgetglobalinfoproc.md)
- [typealias AudioFileComponentGetGlobalInfoSizeProc](audiofilecomponentgetglobalinfosizeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetglobalinfo(_:_:_:_:_:_:))*