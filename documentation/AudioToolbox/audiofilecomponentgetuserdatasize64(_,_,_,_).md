# AudioFileComponentGetUserDataSize64(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 14.0+

## Declaration

```swift
func AudioFileComponentGetUserDataSize64(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ outUserDataSize: UnsafeMutablePointer<UInt64>) -> OSStatus
```

```c
extern OSStatus AudioFileComponentGetUserDataSize64(AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex, UInt64 *outUserDataSize);
```

## See Also

### Functions
- [func AudioComponentValidateWithResults(AudioComponent, CFDictionary?, (AudioComponentValidationResult, CFDictionary) -> Void) -> OSStatus](./audiocomponentvalidatewithresults%28_,_,_%29.md)
- [func AudioConverterNewWithOptions(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, AudioConverterOptions, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](./audioconverternewwithoptions%28_,_,_,_%29.md)
- [func AudioConverterPrepare(UInt32, UnsafeMutableRawPointer?, ((OSStatus) -> Void)?)](./audioconverterprepare%28_,_,_%29.md)
- [func AudioFileComponentGetUserDataAtOffset(AudioFileComponent, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetuserdataatoffset%28_,_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetuserdatasize64(_:_:_:_:))*