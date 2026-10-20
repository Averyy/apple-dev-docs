# AudioFileComponentGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentGetProperty(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func AudioFileComponentGetPropertyInfo(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](audiofilecomponentgetpropertyinfo(_:_:_:_:).md)
- [func AudioFileComponentSetProperty(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiofilecomponentsetproperty(_:_:_:_:).md)
- [typealias AudioFileComponentGetPropertyInfoProc](audiofilecomponentgetpropertyinfoproc.md)
- [typealias AudioFileComponentGetPropertyProc](audiofilecomponentgetpropertyproc.md)
- [typealias AudioFileComponentSetPropertyProc](audiofilecomponentsetpropertyproc.md)
- [Audio File Component Specific Properties](1404186-audio-file-component-specific-pr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetproperty(_:_:_:_:))*