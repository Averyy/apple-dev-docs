# mData

**Framework**: Core Audio Types  
**Kind**: property  
**Role**: Instance Property

A pointer to a buffer of audio data.

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
var mData: UnsafeMutableRawPointer?
```

```c
void * mData;
```

## See Also

### Accessing the Audio
- [var mNumberChannels: UInt32](./mnumberchannels.md)
  The number of interleaved channels in the buffer.
- [var mDataByteSize: UInt32](./mdatabytesize.md)
  The number of bytes in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiobuffer/mdata)*