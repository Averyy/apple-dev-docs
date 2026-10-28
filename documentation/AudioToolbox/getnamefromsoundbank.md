# GetNameFromSoundBank

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Gets the name of a sound bank from a sound bank file.

**Availability**:
- macOS 10.2+ - Deprecated in 10.5

## Declaration

```c
extern OSStatus GetNameFromSoundBank(const struct FSRef *inSoundBankRef, CFStringRef*outName);
```

## Return Value

A result code.

## Discussion

The caller is responsible for releasing the sound bank name.

## Parameters

- `inSoundBankRef`: The sound bank whose name you want to get.
- `outName`: The name of the sound bank.

## See Also

### Instrument Functions
- [func CopyNameFromSoundBank(CFURL, UnsafeMutablePointer<Unmanaged<CFString>?>) -> OSStatus](./copynamefromsoundbank%28_,_%29.md)
  Copies the name of a sound bank from a sound bank file at a specified URL.
- [func CopyInstrumentInfoFromSoundBank(CFURL, UnsafeMutablePointer<Unmanaged<CFArray>?>) -> OSStatus](./copyinstrumentinfofromsoundbank%28_,_%29.md)
- [var kInstrumentInfoKey_LSB: String](./kinstrumentinfokey_lsb.md)
- [var kInstrumentInfoKey_MSB: String](./kinstrumentinfokey_msb.md)
- [var kInstrumentInfoKey_Name: String](./kinstrumentinfokey_name.md)
- [var kInstrumentInfoKey_Program: String](./kinstrumentinfokey_program.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/getnamefromsoundbank)*