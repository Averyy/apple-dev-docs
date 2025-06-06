# AudioFileComponentFileDataIsThisFormat(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentFileDataIsThisFormat(_ inComponent: AudioFileComponent, _ inDataByteSize: UInt32, _ inData: UnsafeRawPointer, _ outResult: UnsafeMutablePointer<UInt32>) -> OSStatus
```

## See Also

- [func AudioFileComponentExtensionIsThisFormat(AudioFileComponent, CFString, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentextensionisthisformat(_:_:_:).md)
- [typealias AudioFileComponentExtensionIsThisFormatProc](audiofilecomponentextensionisthisformatproc.md)
- [typealias AudioFileComponentFileDataIsThisFormatProc](audiofilecomponentfiledataisthisformatproc.md)
- [typealias GetPropertyFDF](getpropertyfdf.md)
- [typealias GetPropertyInfoFDF](getpropertyinfofdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentfiledataisthisformat(_:_:_:_:))*