# AudioFileComponentGetPropertyInfo(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentGetPropertyInfo(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ outPropertySize: UnsafeMutablePointer<UInt32>?, _ outWritable: UnsafeMutablePointer<UInt32>?) -> OSStatus
```

## See Also

- [func AudioFileComponentGetProperty(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetproperty(_:_:_:_:).md)
- [func AudioFileComponentSetProperty(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiofilecomponentsetproperty(_:_:_:_:).md)
- [typealias AudioFileComponentGetPropertyInfoProc](audiofilecomponentgetpropertyinfoproc.md)
- [typealias AudioFileComponentGetPropertyProc](audiofilecomponentgetpropertyproc.md)
- [typealias AudioFileComponentSetPropertyProc](audiofilecomponentsetpropertyproc.md)
- [Audio File Component Specific Properties](1404186-audio-file-component-specific-pr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetpropertyinfo(_:_:_:_:))*