# AudioConverterReset(_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Resets an audio converter object, clearing and flushing its buffers.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioConverterReset(_ inAudioConverter: AudioConverterRef) -> OSStatus
```

```c
extern OSStatus AudioConverterReset(AudioConverterRef inAudioConverter);
```

## Return Value

A  result code.

## Discussion

Call this function after a discontinuity in the source audio stream being provided to the converter.

## Parameters

- `inAudioConverter`: The audio converter object to reset.

## See Also

### Managing Audio Converter Objects
- [func AudioConverterNew(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](./audioconverternew%28_,_,_%29.md)
  Creates a new audio converter object based on specified audio formats.
- [func AudioConverterNewSpecific(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafePointer<AudioClassDescription>, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](./audioconverternewspecific%28_,_,_,_,_%29.md)
  Creates a new audio converter object using a specified codec.
- [func AudioConverterDispose(AudioConverterRef) -> OSStatus](./audioconverterdispose%28_%29.md)
  Disposes of an audio converter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterreset(_:))*