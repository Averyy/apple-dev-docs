# AudioFileComponentWriteBytesProc

**Framework**: Audio Toolbox  
**Kind**: typealias

**Availability**:
- macOS ?+

## Declaration

```swift
typealias AudioFileComponentWriteBytesProc = (UnsafeMutableRawPointer, DarwinBoolean, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus
```

## See Also

- [func AudioFileComponentReadBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadbytes(_:_:_:_:_:).md)
- [func AudioFileComponentReadPacketData(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadpacketdata(_:_:_:_:_:_:_:).md)
- [func AudioFileComponentReadPackets(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiofilecomponentreadpackets(_:_:_:_:_:_:_:).md)
- [func AudioFileComponentWriteBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilecomponentwritebytes(_:_:_:_:_:).md)
- [func AudioFileComponentWritePackets(AudioFileComponent, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](audiofilecomponentwritepackets(_:_:_:_:_:_:_:).md)
- [typealias AudioFileComponentReadBytesProc](audiofilecomponentreadbytesproc.md)
- [typealias AudioFileComponentReadPacketDataProc](audiofilecomponentreadpacketdataproc.md)
- [typealias AudioFileComponentReadPacketsProc](audiofilecomponentreadpacketsproc.md)
- [typealias AudioFileComponentWritePacketsProc](audiofilecomponentwritepacketsproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentwritebytesproc)*