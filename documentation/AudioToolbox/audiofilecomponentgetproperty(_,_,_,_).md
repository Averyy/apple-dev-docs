# AudioFileComponentGetProperty(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentGetProperty(_ inComponent: AudioFileComponent, _ inPropertyID: AudioFileComponentPropertyID, _ ioPropertyDataSize: UnsafeMutablePointer<UInt32>, _ outPropertyData: UnsafeMutableRawPointer) -> OSStatus
```

```c
extern OSStatus AudioFileComponentGetProperty(AudioFileComponent inComponent, AudioFileComponentPropertyID inPropertyID, UInt32 *ioPropertyDataSize, void *outPropertyData);
```

## See Also

### Accessing Properties
- [func AudioFileComponentGetPropertyInfo(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](./audiofilecomponentgetpropertyinfo%28_,_,_,_%29.md)
- [func AudioFileComponentSetProperty(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./audiofilecomponentsetproperty%28_,_,_,_%29.md)
- [typealias AudioFileComponentGetPropertyInfoProc](./audiofilecomponentgetpropertyinfoproc.md)
- [typealias AudioFileComponentGetPropertyProc](./audiofilecomponentgetpropertyproc.md)
- [typealias AudioFileComponentSetPropertyProc](./audiofilecomponentsetpropertyproc.md)
- [Audio File Component Specific Properties](./api-1404186-audio-file-component-specific-pr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetproperty(_:_:_:_:))*