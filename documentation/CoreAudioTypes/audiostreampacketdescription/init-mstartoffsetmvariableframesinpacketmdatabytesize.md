# init(mStartOffset:mVariableFramesInPacket:mDataByteSize:)

**Framework**: Core Audio Types  
**Kind**: init

Creates an audio stream basic description with the start offset, and the number of sample frames and bytes in the packet that you specify.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(mStartOffset: Int64, mVariableFramesInPacket: UInt32, mDataByteSize: UInt32)
```

## Parameters

- `mStartOffset`: The number of bytes from the start of the buffer to the beginning of the packet.
- `mVariableFramesInPacket`: The number of sample frames of data in the packet. For formats with a constant number of frames per packet, set this to  .
- `mDataByteSize`: The number of bytes in the packet.

## See Also

- [init()](audiostreampacketdescription/init.md)
  Creates an audio stream basic description.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiostreampacketdescription/init(mstartoffset:mvariableframesinpacket:mdatabytesize:))*