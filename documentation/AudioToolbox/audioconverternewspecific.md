# AudioConverterNewSpecific(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Creates a new audio converter object using a specified codec.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioConverterNewSpecific(_ inSourceFormat: UnsafePointer<AudioStreamBasicDescription>, _ inDestinationFormat: UnsafePointer<AudioStreamBasicDescription>, _ inNumberClassDescriptions: UInt32, _ inClassDescriptions: UnsafePointer<AudioClassDescription>, _ outAudioConverter: UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus
```

#### Return Value

A  result code.

#### Discussion

This function is identical to [`AudioConverterNew(_:_:_:)`](audioconverternew(_:_:_:).md) function, except that your application may explicitly choose which codec to instantiate if there is more than one choice.

## Parameters

- `inSourceFormat`: The format of the source audio to be converted.
- `inDestinationFormat`: The destination format to which the audio is to be converted.
- `inNumberClassDescriptions`: The number of class descriptions supplied in the   parameter.
- `inClassDescriptions`: A list of   objects that specify the codec to use.
- `outAudioConverter`: On return, a new audio converter object.

## See Also

- [func AudioConverterNew(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](audioconverternew(_:_:_:).md)
  Creates a new audio converter object based on specified audio formats.
- [func AudioConverterReset(AudioConverterRef) -> OSStatus](audioconverterreset(_:).md)
  Resets an audio converter object, clearing and flushing its buffers.
- [func AudioConverterDispose(AudioConverterRef) -> OSStatus](audioconverterdispose(_:).md)
  Disposes of an audio converter object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverternewspecific(_:_:_:_:_:))*