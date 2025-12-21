# AudioConverterFillComplexBufferWithPacketDependencies(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func AudioConverterFillComplexBufferWithPacketDependencies(_ inAudioConverter: AudioConverterRef, _ inInputDataProc: AudioConverterComplexInputDataProc, _ inInputDataProcUserData: UnsafeMutableRawPointer?, _ ioOutputDataPacketSize: UnsafeMutablePointer<UInt32>, _ outOutputData: UnsafeMutablePointer<AudioBufferList>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?, _ outPacketDependencies: UnsafeMutablePointer<AudioStreamPacketDependencyDescription>) -> OSStatus
```

#### Return Value

A result code.

#### Discussion

Converts audio data supplied by a callback function, supporting non-interleaved and packetized formats, and also supporting packet dependency descriptions.

For output formats that use packet dependency descriptions, this must be used instead of AudioConverterFillComplexBuffer, which will return an error for such formats.

## Parameters

- `inAudioConverter`: The audio converter to use for format conversion.
- `inInputDataProc`: A callback function that supplies audio data to convert.   This callback is invoked repeatedly as the converter is ready for   new input data.
- `inInputDataProcUserData`: Custom data for use by your application when receiving a   callback invocation.
- `ioOutputDataPacketSize`: On input, the size of the output buffer (in the    parameter), expressed in number packets in the audio converter’s   output format.  On output, the number of packets of converted data   that were written to the output buffer.
- `outOutputData`: The converted output data is written to this buffer. On entry, the   buffers’   fields (which must all be the same) reflect   buffer capacity.  On exit,   is set to the number of   bytes written.
- `outPacketDescriptions`: If not  , and if the audio converter’s output format uses packet   descriptions, this must point to a block of memory capable of holding   the number of packet descriptions specified in the    parameter.  (See   for functions that   let you determine whether an audio format uses packet descriptions).   If not   on output and if the audio converter’s output format   uses packet descriptions, then this parameter contains an array of   packet descriptions.
- `outPacketDependencies`: Should point to a memory block capable of holding the number of   packet dependency description structures specified in the    parameter.  Must not be  .  This array   will be filled out only by encoders that produce a format which has a   non-zero value for  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconverterfillcomplexbufferwithpacketdependencies(_:_:_:_:_:_:_:))*