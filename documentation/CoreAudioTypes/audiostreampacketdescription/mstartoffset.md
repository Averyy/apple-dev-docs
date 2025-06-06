# mStartOffset

**Framework**: Core Audio Types  
**Kind**: property

The number of bytes from the start of the buffer to the beginning of the packet.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mStartOffset: Int64
```

#### Discussion

For example, if the data buffer contains 5 bytes of data, with one byte per packet, then the start offset for the last packet is 4. There are 4 bytes in the buffer before the start of the last packet.

## See Also

- [var mDataByteSize: UInt32](audiostreampacketdescription/mdatabytesize.md)
  The number of bytes in the packet.
- [var mVariableFramesInPacket: UInt32](audiostreampacketdescription/mvariableframesinpacket.md)
  The number of sample frames of data in the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiostreampacketdescription/mstartoffset)*