# AudioFileComponentWritePackets(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentWritePackets(_ inComponent: AudioFileComponent, _ inUseCache: Bool, _ inNumBytes: UInt32, _ inPacketDescriptions: UnsafePointer<AudioStreamPacketDescription>?, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ inBuffer: UnsafeRawPointer) -> OSStatus
```

## See Also

- [func AudioFileComponentReadBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadbytes(_:_:_:_:_:).md)
- [func AudioFileComponentReadPacketData(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadpacketdata(_:_:_:_:_:_:_:).md)
- [func AudioFileComponentReadPackets(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadpackets(_:_:_:_:_:_:_:).md)
- [func AudioFileComponentWriteBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilecomponentwritebytes(_:_:_:_:_:).md)
- [typealias AudioFileComponentReadBytesProc](audiofilecomponentreadbytesproc.md)
- [typealias AudioFileComponentReadPacketDataProc](audiofilecomponentreadpacketdataproc.md)
- [typealias AudioFileComponentReadPacketsProc](audiofilecomponentreadpacketsproc.md)
- [typealias AudioFileComponentWriteBytesProc](audiofilecomponentwritebytesproc.md)
- [typealias AudioFileComponentWritePacketsProc](audiofilecomponentwritepacketsproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentwritepackets(_:_:_:_:_:_:_:))*