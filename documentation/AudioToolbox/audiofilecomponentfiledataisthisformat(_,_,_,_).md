# AudioFileComponentFileDataIsThisFormat(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentFileDataIsThisFormat(_ inComponent: AudioFileComponent, _ inDataByteSize: UInt32, _ inData: UnsafeRawPointer, _ outResult: UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
extern OSStatus AudioFileComponentFileDataIsThisFormat(AudioFileComponent inComponent, UInt32 inDataByteSize, const void *inData, UInt32 *outResult);
```

## See Also

### Checking the File Format
- [func AudioFileComponentExtensionIsThisFormat(AudioFileComponent, CFString, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiofilecomponentextensionisthisformat%28_,_,_%29.md)
- [typealias AudioFileComponentExtensionIsThisFormatProc](./audiofilecomponentextensionisthisformatproc.md)
- [typealias AudioFileComponentFileDataIsThisFormatProc](./audiofilecomponentfiledataisthisformatproc.md)
- [typealias GetPropertyFDF](./getpropertyfdf.md)
- [typealias GetPropertyInfoFDF](./getpropertyinfofdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentfiledataisthisformat(_:_:_:_:))*