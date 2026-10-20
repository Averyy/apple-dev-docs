# AudioCodecAppendInputBufferList(_:_:_:_:_:)

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
func AudioCodecAppendInputBufferList(_ inCodec: AudioCodec, _ inBufferList: UnsafePointer<AudioBufferList>, _ ioNumberPackets: UnsafeMutablePointer<UInt32>, _ inPacketDescription: UnsafePointer<AudioStreamPacketDescription>?, _ outBytesConsumed: UnsafeMutablePointer<UInt32>) -> OSStatus
```

```c
extern OSStatus AudioCodecAppendInputBufferList(AudioCodec inCodec, const AudioBufferList *inBufferList, UInt32 *ioNumberPackets, const AudioStreamPacketDescription *inPacketDescription, UInt32 *outBytesConsumed);
```

## See Also

### Configuring Buffers
- [func AudioCodecProduceOutputBufferList(AudioCodec, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<UInt32>) -> OSStatus](./audiocodecproduceoutputbufferlist%28_,_,_,_,_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecappendinputbufferlist(_:_:_:_:_:))*