# mNumberChannels

**Framework**: Core Audio Types  
**Kind**: property

The number of interleaved channels in the buffer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mNumberChannels: UInt32
```

#### Discussion

A value of `1` indicates the buffer is noninterleaved.

## See Also

- [var mDataByteSize: UInt32](audiobuffer/mdatabytesize.md)
  The number of bytes in the buffer.
- [var mData: UnsafeMutableRawPointer?](audiobuffer/mdata.md)
  A pointer to a buffer of audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiobuffer/mnumberchannels)*