# send(_:discontinuity:hostTimeInNanoseconds:)

**Framework**: Core Media I/O  
**Kind**: method

Sends a media sample to stream client.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func send(_ sampleBuffer: CMSampleBuffer, discontinuity: CMIOExtensionStream.DiscontinuityFlags, hostTimeInNanoseconds: UInt64)
```

#### Discussion

Specify sample buffer timestamps that are relative to the clock timebase specified by the [`clockType`](cmioextensionstream/clocktype-swift.property.md) property.

> ❗ **Important**:  Attempting to send a sample buffer from a sink stream throws an exception.

 Attempting to send a sample buffer from a sink stream throws an exception.

## Parameters

- `sampleBuffer`: A sample buffer that contains the media data to send.
- `discontinuity`: A flag that indicates whether the sample buffer represents a discontinuity boundary.
- `hostTimeInNanoseconds`: The host time in nanoseconds when the stream captured the buffer.

## See Also

- [func consumeSampleBuffer(from: CMIOExtensionClient, completionHandler: (CMSampleBuffer?, UInt64, CMIOExtensionStream.DiscontinuityFlags, Bool, (any Error)?) -> Void)](cmioextensionstream/consumesamplebuffer(from:completionhandler:).md)
  Consumes a sample buffer from a client.
- [CMIOExtensionStream.DiscontinuityFlags](cmioextensionstream/discontinuityflags.md)
  Constants that specify the types of discontinuities that can occur in a media stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/send(_:discontinuity:hosttimeinnanoseconds:))*