# AudioConverterFillComplexBuffer(_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Converts audio data supplied by a callback function, supporting non-interleaved and packetized formats.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioConverterFillComplexBuffer(_ inAudioConverter: AudioConverterRef, _ inInputDataProc: AudioConverterComplexInputDataProc, _ inInputDataProcUserData: UnsafeMutableRawPointer?, _ ioOutputDataPacketSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>?) -> OSStatus
```

#### Return Value

A  result code.

#### Discussion

Use this function for all audio data format conversions except for the special case of converting from one linear PCM format to another with no sample rate conversion.

## Parameters

- `inAudioConverter`: The audio converter to use for format conversion.
- `inInputDataProc`: A callback function that supplies audio data to convert. This callback is invoked repeatedly as the converter is ready for new input data.
- `inInputDataProcUserData`: Custom data for use by your application when receiving a callback invocation.
- `ioOutputDataPacketSize`: On input, the size of the output buffer (in the   parameter), expressed in number packets in the audio converter’s output format. On output, the number of packets of converted data that were written to the output buffer.
- `outOutputData`: On output, the converted audio data.
- `outPacketDescription`: On input, must point to a block of memory capable of holding the number of packet descriptions specified in the   parameter. (See   for functions that let you determine whether an audio format uses packet descriptions). If not   on output and if the audio converter’s output format uses packet descriptions, then this parameter contains an array of packet descriptions.

## See Also

- [Encoding and decoding audio](encoding-and-decoding-audio.md)
  Convert audio formats to efficiently manage data and quality.
- [func AudioConverterConvertBuffer(AudioConverterRef, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audioconverterconvertbuffer(_:_:_:_:_:).md)
  Converts audio data from one linear PCM format to another.
- [func AudioConverterConvertComplexBuffer(AudioConverterRef, UInt32, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audioconverterconvertcomplexbuffer(_:_:_:_:).md)
  Converts audio data from one linear PCM format to another, where both use the same sample rate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterfillcomplexbuffer(_:_:_:_:_:_:))*