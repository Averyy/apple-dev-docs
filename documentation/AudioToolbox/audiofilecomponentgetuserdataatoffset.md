# AudioFileComponentGetUserDataAtOffset(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 14.0+

## Declaration

```swift
func AudioFileComponentGetUserDataAtOffset(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ inOffset: Int64, _ ioUserDataSize: UnsafeMutablePointer<UInt32>, _ outUserData: UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func AudioComponentValidateWithResults(AudioComponent, CFDictionary?, (AudioComponentValidationResult, CFDictionary) -> Void) -> OSStatus](audiocomponentvalidatewithresults(_:_:_:).md)
- [func AudioConverterNewWithOptions(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, AudioConverterOptions, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](audioconverternewwithoptions(_:_:_:_:).md)
- [func AudioConverterPrepare(UInt32, UnsafeMutableRawPointer?, ((OSStatus) -> Void)?)](audioconverterprepare(_:_:_:).md)
- [func AudioFileComponentGetUserDataSize64(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](audiofilecomponentgetuserdatasize64(_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetuserdataatoffset(_:_:_:_:_:_:))*