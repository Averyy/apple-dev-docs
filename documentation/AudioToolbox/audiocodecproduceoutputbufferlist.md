# AudioCodecProduceOutputBufferList(_:_:_:_:_:)

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
func AudioCodecProduceOutputBufferList(_ inCodec: AudioCodec, _ ioBufferList: UnsafeMutablePointer<AudioBufferList>, _ ioNumberPackets: UnsafeMutablePointer<UInt32>, _ outPacketDescription: UnsafeMutablePointer<AudioStreamPacketDescription>?, _ outStatus: UnsafeMutablePointer<UInt32>) -> OSStatus
```

## See Also

- [func AudioCodecAppendInputBufferList(AudioCodec, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<UInt32>) -> OSStatus](audiocodecappendinputbufferlist(_:_:_:_:_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiocodecproduceoutputbufferlist(_:_:_:_:_:))*