# AudioConverterConvertComplexBuffer(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Converts audio data from one linear PCM format to another, where both use the same sample rate.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioConverterConvertComplexBuffer(_ inAudioConverter: AudioConverterRef, _ inNumberPCMFrames: UInt32, _ inInputData: UnsafePointer<AudioBufferList>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

This function is appropriate for linear PCM-to-linear PCM audio data format conversion where there is no sample rate conversion.

> ❗ **Important**:  This function fails for conversions where there is a variation between the input and output data buffer sizes. This includes sample rate conversions and conversions involving most compressed formats. In these cases, instead use the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) function.

 This function fails for conversions where there is a variation between the input and output data buffer sizes. This includes sample rate conversions and conversions involving most compressed formats. In these cases, instead use the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) function.

## Parameters

- `inAudioConverter`: The audio converter to use for the format conversion.
- `inNumberPCMFrames`: The number of linear PCM frames to convert.
- `inInputData`: The source audio buffer list.
- `outOutputData`: The destination audio buffer list.

## See Also

- [Encoding and decoding audio](encoding-and-decoding-audio.md)
  Convert audio formats to efficiently manage data and quality.
- [func AudioConverterConvertBuffer(AudioConverterRef, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audioconverterconvertbuffer(_:_:_:_:_:).md)
  Converts audio data from one linear PCM format to another.
- [func AudioConverterFillComplexBuffer(AudioConverterRef, AudioConverterComplexInputDataProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<AudioStreamPacketDescription>?) -> OSStatus](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md)
  Converts audio data supplied by a callback function, supporting non-interleaved and packetized formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterconvertcomplexbuffer(_:_:_:_:))*