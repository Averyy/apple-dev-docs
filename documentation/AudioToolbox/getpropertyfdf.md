# GetPropertyFDF

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
typealias GetPropertyFDF = (UnsafeMutableRawPointer, AudioFilePropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func AudioFileComponentFileDataIsThisFormat(AudioFileComponent, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentfiledataisthisformat(_:_:_:_:).md)
- [func AudioFileComponentExtensionIsThisFormat(AudioFileComponent, CFString, UnsafeMutablePointer<UInt32>) -> OSStatus](audiofilecomponentextensionisthisformat(_:_:_:).md)
- [typealias AudioFileComponentExtensionIsThisFormatProc](audiofilecomponentextensionisthisformatproc.md)
- [typealias AudioFileComponentFileDataIsThisFormatProc](audiofilecomponentfiledataisthisformatproc.md)
- [typealias GetPropertyInfoFDF](getpropertyinfofdf.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/getpropertyfdf)*