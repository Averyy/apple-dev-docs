# AudioFileComponentGetPropertyProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AudioFileComponentGetPropertyProc = (UnsafeMutableRawPointer, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus
```

```c
typedef int (*)(void *, unsigned int, unsigned int *, void *) AudioFileComponentGetPropertyProc;
```

## See Also

### Accessing Properties
- [func AudioFileComponentGetProperty(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetproperty%28_,_,_,_%29.md)
- [func AudioFileComponentGetPropertyInfo(AudioFileComponent, AudioFileComponentPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus](./audiofilecomponentgetpropertyinfo%28_,_,_,_%29.md)
- [func AudioFileComponentSetProperty(AudioFileComponent, AudioFileComponentPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](./audiofilecomponentsetproperty%28_,_,_,_%29.md)
- [typealias AudioFileComponentGetPropertyInfoProc](./audiofilecomponentgetpropertyinfoproc.md)
- [typealias AudioFileComponentSetPropertyProc](./audiofilecomponentsetpropertyproc.md)
- [Audio File Component Specific Properties](./api-1404186-audio-file-component-specific-pr.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetpropertyproc)*