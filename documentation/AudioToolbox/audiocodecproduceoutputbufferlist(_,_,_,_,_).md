# AudioCodecProduceOutputBufferList(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func  
**Role**: Function

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func AudioCodecProduceOutputBufferList(_ inCodec: AudioCodec, _ ioBufferList: UnsafeMutablePointer<AudioBufferList>, _ ioNumberPackets: UnsafeMutablePointer<UInt32>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>?, _ outStatus: UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
extern OSStatus AudioCodecProduceOutputBufferList(AudioCodec inCodec, AudioBufferList *ioBufferList, UInt32 *ioNumberPackets, AudioStreamPacketDescription *outPacketDescription, UInt32 *outStatus);
```

## See Also

### Configuring Buffers
- [func AudioCodecAppendInputBufferList(AudioCodec, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiocodecappendinputbufferlist%28_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecproduceoutputbufferlist(_:_:_:_:_:))*