# AudioConverterPrepare(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func AudioConverterPrepare(_ inFlags: UInt32, _ ioReserved: UnsafeMutableRawPointer?, _ inCompletionBlock: ((OSStatus) -> Void)?)
```

```c
extern void AudioConverterPrepare(UInt32 inFlags, void *ioReserved, void (^inCompletionBlock)(OSStatus ));
```

## See Also

### Functions
- [func AudioComponentValidateWithResults(AudioComponent, CFDictionary?, (AudioComponentValidationResult, CFDictionary) -> Void) -> OSStatus](./audiocomponentvalidatewithresults%28_,_,_%29.md)
- [func AudioConverterNewWithOptions(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, AudioConverterOptions, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](./audioconverternewwithoptions%28_,_,_,_%29.md)
- [func AudioFileComponentGetUserDataAtOffset(AudioFileComponent, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetuserdataatoffset%28_,_,_,_,_,_%29.md)
- [func AudioFileComponentGetUserDataSize64(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](./audiofilecomponentgetuserdatasize64%28_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterprepare(_:_:_:))*