# AudioFileComponentReadPackets(_:_:_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentReadPackets(_ inComponent: AudioFileComponent, _ inUseCache: Bool, _ outNumBytes: UnsafeMutablePointer<UInt32>, _ outPacketDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?, _ inStartingPacket: Int64, _ ioNumPackets: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutableRawPointer) -> OSStatus
```

## See Also

- [func AudioFileComponentReadBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadbytes(_:_:_:_:_:).md)
- [func AudioFileComponentReadPacketData(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadpacketdata(_:_:_:_:_:_:_:).md)
- [func AudioFileComponentWriteBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilecomponentwritebytes(_:_:_:_:_:).md)
- [func AudioFileComponentWritePackets(AudioFileComponent, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilecomponentwritepackets(_:_:_:_:_:_:_:).md)
- [typealias AudioFileComponentReadBytesProc](audiofilecomponentreadbytesproc.md)
- [typealias AudioFileComponentReadPacketDataProc](audiofilecomponentreadpacketdataproc.md)
- [typealias AudioFileComponentReadPacketsProc](audiofilecomponentreadpacketsproc.md)
- [typealias AudioFileComponentWriteBytesProc](audiofilecomponentwritebytesproc.md)
- [typealias AudioFileComponentWritePacketsProc](audiofilecomponentwritepacketsproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentreadpackets(_:_:_:_:_:_:_:))*