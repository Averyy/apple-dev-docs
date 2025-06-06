# CopyNameFromSoundBank(_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Copies the name of a sound bank from a sound bank file at a specified URL.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CopyNameFromSoundBank(_ inURL: CFURL, _ outName: UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus
```

#### Return Value

A result code.

## Parameters

- `inURL`: A URL that points to the sound bank whose name you want to get.
- `outName`: The name of the sound bank.

## See Also

- [func CopyInstrumentInfoFromSoundBank(CFURL, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](copyinstrumentinfofromsoundbank(_:_:).md)
- [var kInstrumentInfoKey_LSB: String](kinstrumentinfokey_lsb.md)
- [var kInstrumentInfoKey_MSB: String](kinstrumentinfokey_msb.md)
- [var kInstrumentInfoKey_Name: String](kinstrumentinfokey_name.md)
- [var kInstrumentInfoKey_Program: String](kinstrumentinfokey_program.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/copynamefromsoundbank(_:_:))*