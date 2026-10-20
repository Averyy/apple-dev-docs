# mNumberChannels

**Framework**: Core Audio Types  
**Kind**: property  
**Role**: Instance Property

The number of interleaved channels in the buffer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mNumberChannels: UInt32
```

```c
UInt32 mNumberChannels;
```

#### Discussion

A value of `1` indicates the buffer is noninterleaved.

## See Also

### Accessing the Audio
- [var mDataByteSize: UInt32](./mdatabytesize.md)
  The number of bytes in the buffer.
- [var mData: UnsafeMutableRawPointer?](./mdata.md)
  A pointer to a buffer of audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiobuffer/mnumberchannels)*