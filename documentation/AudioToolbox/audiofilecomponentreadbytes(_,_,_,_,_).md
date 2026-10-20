# AudioFileComponentReadBytes(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- macOS 10.4+

## Declaration

```swift
func AudioFileComponentReadBytes(_ inComponent: AudioFileComponent, _ inUseCache: Bool, _ inStartingByte: Int64, _ ioNumBytes: UnsafeMutablePointer<UInt32>, _ outBuffer: UnsafeMutableRawPointer) -> OSStatus
```

```c
extern OSStatus AudioFileComponentReadBytes(AudioFileComponent inComponent, Boolean inUseCache, SInt64 inStartingByte, UInt32 *ioNumBytes, void *outBuffer);
```

## See Also

### Reading and Writing Data
- [func AudioFileComponentReadPacketData(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentreadpacketdata%28_,_,_,_,_,_,_%29.md)
- [func AudioFileComponentReadPackets(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentreadpackets%28_,_,_,_,_,_,_%29.md)
- [func AudioFileComponentWriteBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](./audiofilecomponentwritebytes%28_,_,_,_,_%29.md)
- [func AudioFileComponentWritePackets(AudioFileComponent, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](./audiofilecomponentwritepackets%28_,_,_,_,_,_,_%29.md)
- [typealias AudioFileComponentReadBytesProc](./audiofilecomponentreadbytesproc.md)
- [typealias AudioFileComponentReadPacketDataProc](./audiofilecomponentreadpacketdataproc.md)
- [typealias AudioFileComponentReadPacketsProc](./audiofilecomponentreadpacketsproc.md)
- [typealias AudioFileComponentWriteBytesProc](./audiofilecomponentwritebytesproc.md)
- [typealias AudioFileComponentWritePacketsProc](./audiofilecomponentwritepacketsproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentreadbytes(_:_:_:_:_:))*