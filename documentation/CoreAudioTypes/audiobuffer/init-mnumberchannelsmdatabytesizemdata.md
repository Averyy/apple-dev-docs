# init(mNumberChannels:mDataByteSize:mData:)

**Framework**: Core Audio Types  
**Kind**: init

Creates an audio buffer with audio data.

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
init(mNumberChannels: UInt32, mDataByteSize: UInt32, mData: UnsafeMutableRawPointer?)
```

## Parameters

- `mNumberChannels`: The number of interleaved channels in the buffer.
- `mDataByteSize`: The number of bytes in the buffer.
- `mData`: A pointer to a buffer of audio data.

## See Also

- [init()](audiobuffer/init.md)
  Creates an empty audio buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiobuffer/init(mnumberchannels:mdatabytesize:mdata:))*