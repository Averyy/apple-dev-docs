# AudioFileComponentGetPropertyProc

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- macOS ?+

## Declaration

```swift
typealias AudioFileComponentGetPropertyProc = (UnsafeMutableRawPointer, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func AudioFileComponentGetProperty(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetproperty(_:_:_:_:).md)
- [func AudioFileComponentGetPropertyInfo(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](audiofilecomponentgetpropertyinfo(_:_:_:_:).md)
- [func AudioFileComponentSetProperty(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiofilecomponentsetproperty(_:_:_:_:).md)
- [typealias AudioFileComponentGetPropertyInfoProc](audiofilecomponentgetpropertyinfoproc.md)
- [typealias AudioFileComponentSetPropertyProc](audiofilecomponentsetpropertyproc.md)
- [Audio File Component Specific Properties](1404186-audio-file-component-specific-pr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetpropertyproc)*