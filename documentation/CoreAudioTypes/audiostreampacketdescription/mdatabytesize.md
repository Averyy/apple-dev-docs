# mDataByteSize

**Framework**: Core Audio Types  
**Kind**: property  
**Role**: Instance Property

The number of bytes in the packet.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mDataByteSize: UInt32
```

```c
UInt32 mDataByteSize;
```

## See Also

### Inspecting an audio stream packet description
- [var mStartOffset: Int64](./mstartoffset.md)
  The number of bytes from the start of the buffer to the beginning of the packet.
- [var mVariableFramesInPacket: UInt32](./mvariableframesinpacket.md)
  The number of sample frames of data in the packet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiostreampacketdescription/mdatabytesize)*