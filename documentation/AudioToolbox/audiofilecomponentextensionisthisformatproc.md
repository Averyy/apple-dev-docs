# AudioFileComponentExtensionIsThisFormatProc

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- macOS ?+

## Declaration

```swift
typealias AudioFileComponentExtensionIsThisFormatProc = (UnsafeMutableRawPointer, CFString, UnsafeMutablePointer<UInt32>) -> OSStatus
```

## See Also

- [func AudioFileComponentFileDataIsThisFormat(AudioFileComponent, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentfiledataisthisformat(_:_:_:_:).md)
- [func AudioFileComponentExtensionIsThisFormat(AudioFileComponent, CFString, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentextensionisthisformat(_:_:_:).md)
- [typealias AudioFileComponentFileDataIsThisFormatProc](audiofilecomponentfiledataisthisformatproc.md)
- [typealias GetPropertyFDF](getpropertyfdf.md)
- [typealias GetPropertyInfoFDF](getpropertyinfofdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentextensionisthisformatproc)*