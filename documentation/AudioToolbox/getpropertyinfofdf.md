# GetPropertyInfoFDF

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
typealias GetPropertyInfoFDF = (UnsafeMutableRawPointer, AudioFilePropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<UInt32>?) -> OSStatus
```

```c
typedef int (*)(void *, unsigned int, unsigned int *, unsigned int *) GetPropertyInfoFDF;
```

## See Also

### Checking the File Format
- [func AudioFileComponentFileDataIsThisFormat(AudioFileComponent, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentfiledataisthisformat%28_,_,_,_%29.md)
- [func AudioFileComponentExtensionIsThisFormat(AudioFileComponent, CFString, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentextensionisthisformat%28_,_,_%29.md)
- [typealias AudioFileComponentExtensionIsThisFormatProc](./audiofilecomponentextensionisthisformatproc.md)
- [typealias AudioFileComponentFileDataIsThisFormatProc](./audiofilecomponentfiledataisthisformatproc.md)
- [typealias GetPropertyFDF](./getpropertyfdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/getpropertyinfofdf)*