# AudioFileComponentExtensionIsThisFormat(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentExtensionIsThisFormat(_ inComponent: AudioFileComponent, _ inExtension: CFString, _ outResult: UnsafeMutablePointer<UInt32>) -> OSStatus
```

## See Also

- [func AudioFileComponentFileDataIsThisFormat(AudioFileComponent, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentfiledataisthisformat(_:_:_:_:).md)
- [typealias AudioFileComponentExtensionIsThisFormatProc](audiofilecomponentextensionisthisformatproc.md)
- [typealias AudioFileComponentFileDataIsThisFormatProc](audiofilecomponentfiledataisthisformatproc.md)
- [typealias GetPropertyFDF](getpropertyfdf.md)
- [typealias GetPropertyInfoFDF](getpropertyinfofdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentextensionisthisformat(_:_:_:))*