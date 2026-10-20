# AudioFileComponentFileDataIsThisFormatProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AudioFileComponentFileDataIsThisFormatProc = (UnsafeMutableRawPointer, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
typedef int (*)(void *, unsigned int, const void *, unsigned int *) AudioFileComponentFileDataIsThisFormatProc;
```

## See Also

### Checking the File Format
- [func AudioFileComponentFileDataIsThisFormat(AudioFileComponent, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentfiledataisthisformat%28_,_,_,_%29.md)
- [func AudioFileComponentExtensionIsThisFormat(AudioFileComponent, CFString, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentextensionisthisformat%28_,_,_%29.md)
- [typealias AudioFileComponentExtensionIsThisFormatProc](./audiofilecomponentextensionisthisformatproc.md)
- [typealias GetPropertyFDF](./getpropertyfdf.md)
- [typealias GetPropertyInfoFDF](./getpropertyinfofdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentfiledataisthisformatproc)*