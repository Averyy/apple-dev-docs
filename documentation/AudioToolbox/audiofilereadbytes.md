# AudioFileReadBytes(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

Reads bytes of audio data from an audio file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileReadBytes(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutableRawPointer) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

In most cases, you should use [`AudioFileReadPackets(_:_:_:_:_:_:_:)`](audiofilereadpackets(_:_:_:_:_:_:_:).md) instead of this function.

This function returns `eofErr` when the read operation encounters the end of the file.  Note that Audio File Services only reads one 32-bit chunk of a file at a time.

## Parameters

- `inAudioFile`: The audio file whose bytes of audio data you want to read.
- `inUseCache`: Set to   if you want to cache the data. You should cache reads and writes if you read or write the same portion of a file multiple times. To request that the data not be cached, if possible, set to  . You should not cache reads and writes if you read or write data from a file only once.
- `inStartingByte`: The byte offset of the audio data you want to be returned.
- `ioNumBytes`: On input, a pointer to the number of bytes to read. On output, a pointer to the number of bytes actually read.
- `outBuffer`: A pointer to user-allocated memory large enough for the requested bytes.

## See Also

- [func AudioFileWriteBytes(AudioFileID, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilewritebytes(_:_:_:_:_:).md)
  Writes bytes of audio data to an audio file.
- [func AudioFileReadPacketData(AudioFileID, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](audiofilereadpacketdata(_:_:_:_:_:_:_:).md)
  Reads packets of audio data from an audio file.
- [func AudioFileWritePackets(AudioFileID, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilewritepackets(_:_:_:_:_:_:_:).md)
  Writes packets of audio data to an audio data file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilereadbytes(_:_:_:_:_:))*