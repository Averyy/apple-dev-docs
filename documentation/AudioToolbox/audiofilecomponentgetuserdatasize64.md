# AudioFileComponentGetUserDataSize64(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 14.0+

## Declaration

```swift
func AudioFileComponentGetUserDataSize64(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ outUserDataSize: UnsafeMutablePointer<UInt64>) -> OSStatus
```

## See Also

- [func AudioComponentValidateWithResults(AudioComponent, CFDictionary?, (AudioComponentValidationResult, CFDictionary) -> Void) -> OSStatus](audiocomponentvalidatewithresults(_:_:_:).md)
- [func AudioConverterNewWithOptions(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, AudioConverterOptions, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](audioconverternewwithoptions(_:_:_:_:).md)
- [func AudioConverterPrepare(UInt32, UnsafeMutableRawPointer?, ((OSStatus) -> Void)?)](audioconverterprepare(_:_:_:).md)
- [func AudioFileComponentGetUserDataAtOffset(AudioFileComponent, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetuserdataatoffset(_:_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetuserdatasize64(_:_:_:_:))*