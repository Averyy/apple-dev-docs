# AudioFileStreamSeek(_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Provides a byte offset for a specified packet in the data stream.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileStreamSeek(_ inAudioFileStream: AudioFileStreamID, _ inPacketOffset: Int64, _ outDataByteOffset: UnsafeMutablePointer<Int64>, _ ioFlags: UnsafeMutablePointer<AudioFileStreamSeekFlags>) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

After you call this function, the parser assumes the next data passed to the [`AudioFileStreamParseBytes(_:_:_:_:)`](audiofilestreamparsebytes(_:_:_:_:).md) function starts from the byte offset returned in the `outDataByteOffset` parameter.

## Parameters

- `inAudioFileStream`: The ID of the parser to which you wish to provide a byte offset. The parser ID is returned by the   function.
- `inPacketOffset`: The number of packets from the beginning of the file of the packet whose byte offset you wish to have returned.
- `outDataByteOffset`: On output, the absolute byte offset of the packet whose offset you specify in the   parameter. For audio file formats that do not contain packet tables, the returned offset may be an estimate.
- `ioFlags`: On output, if the   parameter returns an estimate, this parameter returns the constant  . Currently, no input flags are defined for this call.

## See Also

- [func AudioFileStreamParseBytes(AudioFileStreamID, UInt32, UnsafeRawPointer?, AudioFileStreamParseFlags) -> OSStatus](audiofilestreamparsebytes(_:_:_:_:).md)
  Passes audio file stream data to the parser.
- [func AudioFileStreamOpen(UnsafeMutableRawPointer?, AudioFileStream_PropertyListenerProc, AudioFileStream_PacketsProc, AudioFileTypeID, UnsafeMutablePointer<AudioFileStreamID?>) -> OSStatus](audiofilestreamopen(_:_:_:_:_:).md)
  Creates and opens a new audio file stream parser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilestreamseek(_:_:_:_:))*