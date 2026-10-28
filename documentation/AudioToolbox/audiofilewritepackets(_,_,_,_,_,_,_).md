# AudioFileWritePackets(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

Writes packets of audio data to an audio data file.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioFileWritePackets(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inNumBytes: UInt32, _ inPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>?, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafeRawPointer) -> OSStatus
```

```c
extern OSStatus AudioFileWritePackets(AudioFileID inAudioFile, Boolean inUseCache, UInt32 inNumBytes, const AudioStreamPacketDescription *inPacketDescriptions, SInt64 inStartingPacket, UInt32 *ioNumPackets, const void *inBuffer);
```

## Return Value

A result code. See Result Codes.

## Discussion

For all uncompressed formats, this function equates packets with frames.

## Parameters

- `inAudioFile`: The audio file to write to.
- `inUseCache`: Set to `true` if you want to cache the data. Otherwise, set to `false`.
- `inNumBytes`: The number of bytes of audio data being written.
- `inPacketDescriptions`: A pointer to an array of packet descriptions for the audio data. Not all formats require packet descriptions. If no packet descriptions are required, for instance, if you are writing CBR data,  pass `NULL`.
- `inStartingPacket`: The packet index for the placement of the first provided packet.
- `ioNumPackets`: On input, a pointer to the number of packets to write. On output, a pointer to the number of packets actually written.
- `inBuffer`: A pointer to user-allocated memory containing the new audio data to write to the audio data file.

## See Also

### Related Documentation
- [func AudioFileReadPackets(AudioFileID, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](./audiofilereadpackets%28_,_,_,_,_,_,_%29.md)
  Reads a fixed duration of audio data from an audio file.
### Reading and Writing Audio Files
- [func AudioFileReadBytes(AudioFileID, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilereadbytes%28_,_,_,_,_%29.md)
  Reads bytes of audio data from an audio file.
- [func AudioFileWriteBytes(AudioFileID, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](./audiofilewritebytes%28_,_,_,_,_%29.md)
  Writes bytes of audio data to an audio file.
- [func AudioFileReadPacketData(AudioFileID, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer?) -> OSStatus](./audiofilereadpacketdata%28_,_,_,_,_,_,_%29.md)
  Reads packets of audio data from an audio file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilewritepackets(_:_:_:_:_:_:_:))*