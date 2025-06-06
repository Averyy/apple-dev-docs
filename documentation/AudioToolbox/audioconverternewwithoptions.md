# AudioConverterNewWithOptions(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+

## Declaration

```swift
func AudioConverterNewWithOptions(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ inOptions: AudioConverterOptions, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus
```

## See Also

- [func AudioComponentValidateWithResults(AudioComponent, CFDictionary?, (AudioComponentValidationResult, CFDictionary) -> Void) -> OSStatus](audiocomponentvalidatewithresults(_:_:_:).md)
- [func AudioConverterPrepare(UInt32, UnsafeMutableRawPointer?, ((OSStatus) -> Void)?)](audioconverterprepare(_:_:_:).md)
- [func AudioFileComponentGetUserDataAtOffset(AudioFileComponent, UInt32, UInt32, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentgetuserdataatoffset(_:_:_:_:_:_:).md)
- [func AudioFileComponentGetUserDataSize64(AudioFileComponent, UInt32, UInt32, UnsafeMutablePointer<UInt64>) -> OSStatus](audiofilecomponentgetuserdatasize64(_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverternewwithoptions(_:_:_:_:))*