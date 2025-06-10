# AudioFileWritePacketsWithDependencies(_:_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
func AudioFileWritePacketsWithDependencies(_ inAudioFile: AudioFileID, _ inUseCache: Bool, _ inNumBytes: UInt32, _ inPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>?, _ inPacketDependencies: UnsafePointer<AudioStreamPacketDependencyDescription>, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafeRawPointer) -> OSStatus
```

#### Return Value

A result code. See Result Codes.

#### Discussion

For all uncompressed formats, `packets == frames`.

## Parameters

- `inAudioFile`: The audio file to write to.
- `inUseCache`: Set to   if you want to cache the data. Otherwise, set to  .
- `inNumBytes`: The number of bytes of audio data being written.
- `inPacketDescriptions`: A pointer to an array of packet descriptions for the audio data.   Not all formats require packet descriptions. If no packet descriptions   are required, for instance, if you are writing CBR data,  pass  .
- `inPacketDependencies`: A pointer to an array of packet dependencies for the audio data.   This must not be  .  To write packets without dependencies,   use   instead.
- `inStartingPacket`: The packet index for the placement of the first provided packet.
- `ioNumPackets`: On input, a pointer to the number of packets to write.   On output, a pointer to the number of packets actually written.
- `inBuffer`: A pointer to user-allocated memory containing the new audio data   to write to the audio data file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilewritepacketswithdependencies(_:_:_:_:_:_:_:_:))*