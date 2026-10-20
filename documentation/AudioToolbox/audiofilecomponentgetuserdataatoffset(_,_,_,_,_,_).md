# AudioFileComponentGetUserDataAtOffset(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 14.0+

## Declaration

```swift
func AudioFileComponentGetUserDataAtOffset(_ inComponent: AudioFileComponent, _ inUserDataID: UInt32, _ inIndex: UInt32, _ inOffset: Int64, _ ioUserDataSize: UnsafeMutablePointer<UInt32>, _ outUserData: UnsafeMutableRawPointer) -> OSStatus
```

```c
extern OSStatus AudioFileComponentGetUserDataAtOffset(AudioFileComponent inComponent, UInt32 inUserDataID, UInt32 inIndex, SInt64 inOffset, UInt32 *ioUserDataSize, void *outUserData);
```

## See Also

### Functions
- [func AudioComponentValidateWithResults(AudioComponent, CFDictionary?, (AudioComponentValidationResult, CFDictionary) -> Void) -> OSStatus](./audiocomponentvalidatewithresults%28_,_,_%29.md)
- [func AudioConverterNewWithOptions(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, AudioConverterOptions, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](./audioconverternewwithoptions%28_,_,_,_%29.md)
- [func AudioConverterPrepare(UInt32, UnsafeMutableRawPointer?, ((OSStatus) -> Void)?)](./audioconverterprepare%28_,_,_%29.md)
- [func AudioFileComponentGetUserDataSize64(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](./audiofilecomponentgetuserdatasize64%28_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentgetuserdataatoffset(_:_:_:_:_:_:))*