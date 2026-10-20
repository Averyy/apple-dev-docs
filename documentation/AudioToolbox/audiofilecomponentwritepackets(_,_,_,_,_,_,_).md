# AudioFileComponentWritePackets(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentWritePackets(_ inComponent: AudioFileComponent, _ inUseCache: Bool, _ inNumBytes: UInt32, _ inPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>?, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafeRawPointer) -> OSStatus
```

```c
extern OSStatus AudioFileComponentWritePackets(AudioFileComponent inComponent, Boolean inUseCache, UInt32 inNumBytes, const AudioStreamPacketDescription *inPacketDescriptions, SInt64 inStartingPacket, UInt32 *ioNumPackets, const void *inBuffer);
```

## See Also

### Reading and Writing Data
- [func AudioFileComponentReadBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentreadbytes%28_,_,_,_,_%29.md)
- [func AudioFileComponentReadPacketData(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentreadpacketdata%28_,_,_,_,_,_,_%29.md)
- [func AudioFileComponentReadPackets(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentreadpackets%28_,_,_,_,_,_,_%29.md)
- [func AudioFileComponentWriteBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](./audiofilecomponentwritebytes%28_,_,_,_,_%29.md)
- [typealias AudioFileComponentReadBytesProc](./audiofilecomponentreadbytesproc.md)
- [typealias AudioFileComponentReadPacketDataProc](./audiofilecomponentreadpacketdataproc.md)
- [typealias AudioFileComponentReadPacketsProc](./audiofilecomponentreadpacketsproc.md)
- [typealias AudioFileComponentWriteBytesProc](./audiofilecomponentwritebytesproc.md)
- [typealias AudioFileComponentWritePacketsProc](./audiofilecomponentwritepacketsproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentwritepackets(_:_:_:_:_:_:_:))*