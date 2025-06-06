# AudioFileStreamParseBytes(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Passes audio file stream data to the parser.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileStreamParseBytes(_ inAudioFileStream: AudioFileStreamID, _ inDataByteSize: UInt32, _ inData: UnsafeRawPointer?, _ inFlags: AudioFileStreamParseFlags) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

Streamed audio file data is expected to be passed to the parser in the same sequence in which it appears in the audio file, from the beginning of the audio file stream, without gaps. However, if you called the [`AudioFileStreamSeek(_:_:_:_:)`](audiofilestreamseek(_:_:_:_:).md) function, the parser assumes that the data passed to the [`AudioFileStreamParseBytes(_:_:_:_:)`](audiofilestreamparsebytes(_:_:_:_:).md) function starts from the byte offset returned by the [`AudioFileStreamSeek(_:_:_:_:)`](audiofilestreamseek(_:_:_:_:).md) function.

When you provide data to the parser, the parser looks for property data and audio data packets and, when it has data ready, calls your [`AudioFileStream_PropertyListenerProc`](audiofilestream_propertylistenerproc.md) and [`AudioFileStream_PacketsProc`](audiofilestream_packetsproc.md) callback functions to process the data. You should provide at least more than a single packet’s worth of audio file data, but it is better to provide a few packets to a few seconds data at a time.

## Parameters

- `inAudioFileStream`: The ID of the parser to which you wish to pass data. The parser ID is returned by the   function.
- `inDataByteSize`: The number of bytes of data to be parsed.
- `inData`: The data to be parsed.
- `inFlags`: An audio file stream flag. If there is a discontinuity from the last data you passed to the parser, set the    flag.

## See Also

- [typealias AudioFileStream_PropertyListenerProc](audiofilestream_propertylistenerproc.md)
  Invoked by an audio file stream parser when it finds a property value in the audio file stream.
- [func AudioFileStreamSeek(AudioFileStreamID, Int64, UnsafeMutablePointer<Int64>, UnsafeMutablePointer<AudioFileStreamSeekFlags>) -> OSStatus](audiofilestreamseek(_:_:_:_:).md)
  Provides a byte offset for a specified packet in the data stream.
- [func AudioFileStreamOpen(UnsafeMutableRawPointer?, AudioFileStream_PropertyListenerProc, AudioFileStream_PacketsProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus](audiofilestreamopen(_:_:_:_:_:).md)
  Creates and opens a new audio file stream parser.
- [typealias AudioFileStream_PacketsProc](audiofilestream_packetsproc.md)
  Invoked by an audio file stream parser when it finds audio data in the audio file stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamparsebytes(_:_:_:_:))*