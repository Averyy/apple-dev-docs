# AudioCodecAppendInputBufferList(_:_:_:_:_:)

**Framework**: Audio Toolbox  
**Kind**: func

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

## See Also

- [func AudioCodecProduceOutputBufferList(AudioCodec, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<UInt32>) -> OSStatus](audiocodecproduceoutputbufferlist(_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecappendinputbufferlist(_:_:_:_:_:))*