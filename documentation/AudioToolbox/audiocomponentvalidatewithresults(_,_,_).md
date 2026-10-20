# AudioComponentValidateWithResults(_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func AudioComponentValidateWithResults(_ inComponent: AudioComponent, _ inValidationParameters: CFDictionary?, _ inCompletionHandler: @escaping (AudioComponentValidationResult, CFDictionary) -> Void) -> OSStatus
```

```c
extern OSStatus AudioComponentValidateWithResults(AudioComponent inComponent, CFDictionaryRef inValidationParameters, void (^inCompletionHandler)(AudioComponentValidationResult , CFDictionaryRef ));
```

## See Also

### Functions
- [func AudioConverterNewWithOptions(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, AudioConverterOptions, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](./audioconverternewwithoptions%28_,_,_,_%29.md)
- [func AudioConverterPrepare(UInt32, UnsafeMutableRawPointer?, ((OSStatus) -> Void)?)](./audioconverterprepare%28_,_,_%29.md)
- [func AudioFileComponentGetUserDataAtOffset(AudioFileComponent, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentgetuserdataatoffset%28_,_,_,_,_,_%29.md)
- [func AudioFileComponentGetUserDataSize64(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](./audiofilecomponentgetuserdatasize64%28_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocomponentvalidatewithresults(_:_:_:))*