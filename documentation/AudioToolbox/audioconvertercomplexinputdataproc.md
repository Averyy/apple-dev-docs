# AudioConverterComplexInputDataProc

**Framework**: Audio Toolbox  
**Kind**: typealias

Supplies input data to the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) function.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioConverterComplexInputDataProc = (AudioConverterRef, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UnsafeMutablePointer<AudioStreamPacketDescription>?>?, UnsafeMutableRawPointer?) -> OSStatus
```

#### Discussion

If you named your callback function `MyAudioConverterComplexInputDataProc`, you would declare it like this:

##### Discussion

This callback supplies input audio data to the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) function.

The audio converter object requests a minimum number of packets in the `ioNumberDataPackets` parameter. Your callback may provide one or more packets. If the number you provide is less than the minimum requested, the converter will invoke your callback again in the near future.

You write your callback to manipulate the fields of the `AudioBufferList` structure, in the `ioData` parameter, to point to one or more buffers of audio data. You use a single buffer for interleaved PCM data, or multiple buffers for non-interleaved PCM data. Your callback is responsible for not freeing or altering the buffer(s) until invoked again.

If your callback returns an error, it must return zero packets of data. Upon receiving zero packets, the `AudioConverterFillComplexBuffer` function delivers any pending output, stops producing further output, and returns the error code. You can use this mechanism when an input callback has temporarily run out of data but has not yet reached the end of the input audio stream.

## Parameters

- `inAudioConverter`: The audio converter object that invoked this callback to obtain new data to convert.
- `ioNumberDataPackets`: On input, the minimum number of packets of input audio data the converter needs for its current conversion cycle. On output, the number of packets of audio data provided for conversion, or   if there is no more data to convert.
- `ioData`: On output, point the fields of the   structure, passed by this parameter, to the audio data you are providing to be converted.
- `outDataPacketDescription`: If not   on input,  the audio converter expects this callback to provide an array of   structures on output, one for each packet of audio data you are providing in the   parameter.
- `inUserData`: On input, the custom application data you provided to the   function.

## See Also

- [typealias AudioConverterInputDataProc](audioconverterinputdataproc.md)
  Deprecated. Use [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) instead.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioconvertercomplexinputdataproc)*