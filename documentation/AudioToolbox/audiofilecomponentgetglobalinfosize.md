# AudioFileComponentGetGlobalInfoSize(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentGetGlobalInfoSize(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inSpecifierSize: UInt32, _ inSpecifier: UnsafeRawPointer?, _ outPropertySize: UnsafeMutablePointer<UInt32>) -> OSStatus
```

## See Also

- [func AudioFileComponentGetGlobalInfo(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetglobalinfo(_:_:_:_:_:_:).md)
- [typealias AudioFileComponentGetGlobalInfoProc](audiofilecomponentgetglobalinfoproc.md)
- [typealias AudioFileComponentGetGlobalInfoSizeProc](audiofilecomponentgetglobalinfosizeproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetglobalinfosize(_:_:_:_:_:))*