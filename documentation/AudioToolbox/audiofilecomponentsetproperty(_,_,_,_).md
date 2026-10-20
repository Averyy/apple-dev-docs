# AudioFileComponentSetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentSetProperty(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ inPropertyDataSize: UInt32, _ inPropertyData: UnsafeRawPointer) -> OSStatus
```

```c
extern OSStatus AudioFileComponentSetProperty(AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 inPropertyDataSize, const void *inPropertyData);
```

## See Also

### Accessing Properties
- [func AudioFileComponentGetProperty(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetproperty%28_,_,_,_%29.md)
- [func AudioFileComponentGetPropertyInfo(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](./audiofilecomponentgetpropertyinfo%28_,_,_,_%29.md)
- [typealias AudioFileComponentGetPropertyInfoProc](./audiofilecomponentgetpropertyinfoproc.md)
- [typealias AudioFileComponentGetPropertyProc](./audiofilecomponentgetpropertyproc.md)
- [typealias AudioFileComponentSetPropertyProc](./audiofilecomponentsetpropertyproc.md)
- [Audio File Component Specific Properties](./api-1404186-audio-file-component-specific-pr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentsetproperty(_:_:_:_:))*