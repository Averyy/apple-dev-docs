# AudioFileComponentReadPacketsProc

**Framework**: Audio Toolbox  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AudioFileComponentReadPacketsProc = (UnsafeMutableRawPointer, DarwinBoolean, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus
```

```c
typedef int (*)(void *, unsigned char, unsigned int *, struct AudioStreamPacketDescription *, long long, unsigned int *, void *) AudioFileComponentReadPacketsProc;
```

## See Also

### Reading and Writing Data
- [func AudioFileComponentReadBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentreadbytes%28_,_,_,_,_%29.md)
- [func AudioFileComponentReadPacketData(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentreadpacketdata%28_,_,_,_,_,_,_%29.md)
- [func AudioFileComponentReadPackets(AudioFileComponent, Bool, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](./audiofilecomponentreadpackets%28_,_,_,_,_,_,_%29.md)
- [func AudioFileComponentWriteBytes(AudioFileComponent, Bool, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](./audiofilecomponentwritebytes%28_,_,_,_,_%29.md)
- [func AudioFileComponentWritePackets(AudioFileComponent, Bool, UInt32, UnsafePointer<AudioStreamPacketDescription>?, Int64, UnsafeMutablePointer<UInt32>, UnsafeRawPointer) -> OSStatus](./audiofilecomponentwritepackets%28_,_,_,_,_,_,_%29.md)
- [typealias AudioFileComponentReadBytesProc](./audiofilecomponentreadbytesproc.md)
- [typealias AudioFileComponentReadPacketDataProc](./audiofilecomponentreadpacketdataproc.md)
- [typealias AudioFileComponentWriteBytesProc](./audiofilecomponentwritebytesproc.md)
- [typealias AudioFileComponentWritePacketsProc](./audiofilecomponentwritepacketsproc.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilecomponentreadpacketsproc)*