# AudioConverterDispose(_:)

**Framework**: Audio Toolbox  
**Kind**: func

Disposes of an audio converter object.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioConverterDispose(_ inAudioConverter: AudioConverterRef) -> OSStatus
```

#### Return Value

A  result code.

#### Discussion

## Parameters

- `inAudioConverter`: The audio converter object to dispose of.

## See Also

- [func AudioConverterNew(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](audioconverternew(_:_:_:).md)
  Creates a new audio converter object based on specified audio formats.
- [func AudioConverterNewSpecific(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafePointer<AudioClassDescription>, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](audioconverternewspecific(_:_:_:_:_:).md)
  Creates a new audio converter object using a specified codec.
- [func AudioConverterReset(AudioConverterRef) -> OSStatus](audioconverterreset(_:).md)
  Resets an audio converter object, clearing and flushing its buffers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterdispose(_:))*