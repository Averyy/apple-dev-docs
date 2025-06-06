# CopyInstrumentInfoFromSoundBank(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CopyInstrumentInfoFromSoundBank(_ inURL: CFURL, _ outInstrumentInfo: UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus
```

## See Also

- [func CopyNameFromSoundBank(CFURL, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](copynamefromsoundbank(_:_:).md)
  Copies the name of a sound bank from a sound bank file at a specified URL.
- [var kInstrumentInfoKey_LSB: String](kinstrumentinfokey_lsb.md)
- [var kInstrumentInfoKey_MSB: String](kinstrumentinfokey_msb.md)
- [var kInstrumentInfoKey_Name: String](kinstrumentinfokey_name.md)
- [var kInstrumentInfoKey_Program: String](kinstrumentinfokey_program.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/copyinstrumentinfofromsoundbank(_:_:))*