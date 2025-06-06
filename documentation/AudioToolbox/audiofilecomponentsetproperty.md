# AudioFileComponentSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentSetProperty(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus
```

## See Also

- [func AudioFileComponentGetProperty(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetproperty(_:_:_:_:).md)
- [func AudioFileComponentGetPropertyInfo(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](audiofilecomponentgetpropertyinfo(_:_:_:_:).md)
- [typealias AudioFileComponentGetPropertyInfoProc](audiofilecomponentgetpropertyinfoproc.md)
- [typealias AudioFileComponentGetPropertyProc](audiofilecomponentgetpropertyproc.md)
- [typealias AudioFileComponentSetPropertyProc](audiofilecomponentsetpropertyproc.md)
- [Audio File Component Specific Properties](1404186-audio-file-component-specific-pr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentsetproperty(_:_:_:_:))*