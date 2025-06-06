# AudioFileWriteBytes(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Writes bytes of audio data to an audio file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileWriteBytes(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafeRawPointer) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

In most cases, you should use [`AudioFileWritePackets(_:_:_:_:_:_:_:)`](audiofilewritepackets(_:_:_:_:_:_:_:).md) instead of this function.

## Parameters

- `inAudioFile`: The audio file to which you want to write bytes of data.
- `inUseCache`: Set to   if you want to cache the data. Otherwise, set to  .
- `inStartingByte`: The byte offset where the audio data should be written.
- `ioNumBytes`: On input, a pointer the number of bytes to write. On output, a pointer to the number of bytes actually written.
- `inBuffer`: A pointer to a buffer containing the bytes to be written.

## See Also

- [func AudioFileReadBytes(AudioFileID, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilereadbytes(_:_:_:_:_:).md)
  Reads bytes of audio data from an audio file.
- [func AudioFileReadPacketData(AudioFileID, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](audiofilereadpacketdata(_:_:_:_:_:_:_:).md)
  Reads packets of audio data from an audio file.
- [func AudioFileWritePackets(AudioFileID, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilewritepackets(_:_:_:_:_:_:_:).md)
  Writes packets of audio data to an audio data file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilewritebytes(_:_:_:_:_:))*