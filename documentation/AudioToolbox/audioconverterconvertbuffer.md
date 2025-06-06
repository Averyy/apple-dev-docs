# AudioConverterConvertBuffer(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Converts audio data from one linear PCM format to another.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioConverterConvertBuffer(_ inAudioConverter: AudioConverterRef, _ inInputDataSize: UInt32, _ inInputData: UnsafeRawPointer, _ ioOutputDataSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutableRawPointer) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

This function is for the special case of converting from one linear PCM format to another. This function cannot perform sample rate conversions and cannot be used for conversion to or from most compressed formats. To perform these types of conversion, use [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) instead.

## Parameters

- `inAudioConverter`: The audio converter to use for format conversion.
- `inInputDataSize`: The size, in bytes, of the audio data input buffer.
- `inInputData`: The audio data to convert.
- `ioOutputDataSize`: On input, the size, in bytes, of the buffer available for the converted data. On output, the number of bytes written to the output buffer (pointed to by the   parameter).
- `outOutputData`: On output, the converted audio data.

## See Also

- [Encoding and decoding audio](encoding-and-decoding-audio.md)
  Convert audio formats to efficiently manage data and quality.
- [func AudioConverterFillComplexBuffer(AudioConverterRef, AudioConverterComplexInputDataProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<AudioStreamPacketDescription>?) -> OSStatus](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md)
  Converts audio data supplied by a callback function, supporting non-interleaved and packetized formats.
- [func AudioConverterConvertComplexBuffer(AudioConverterRef, UInt32, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audioconverterconvertcomplexbuffer(_:_:_:_:).md)
  Converts audio data from one linear PCM format to another, where both use the same sample rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterconvertbuffer(_:_:_:_:_:))*