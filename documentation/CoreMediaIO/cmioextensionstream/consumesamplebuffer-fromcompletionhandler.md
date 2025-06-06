# consumeSampleBuffer(from:completionHandler:)

**Framework**: Core Media I/O  
**Kind**: method

Consumes a sample buffer from a client.

**Availability**:
- Mac Catalyst 15.4+
- macOS 12.3+

## Declaration

```swift
func consumeSampleBuffer(from client: CMIOExtensionClient) async throws -> (CMSampleBuffer, UInt64, CMIOExtensionStream.DiscontinuityFlags, Bool)
```

## Parameters

- `client`: The client with a sample to process.
- `completionHandler`: A callback the system invokes with the following data:

## See Also

- [func send(CMSampleBuffer, discontinuity: CMIOExtensionStream.DiscontinuityFlags, hostTimeInNanoseconds: UInt64)](cmioextensionstream/send(_:discontinuity:hosttimeinnanoseconds:).md)
  Sends a media sample to stream client.
- [CMIOExtensionStream.DiscontinuityFlags](cmioextensionstream/discontinuityflags.md)
  Constants that specify the types of discontinuities that can occur in a media stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/consumesamplebuffer(from:completionhandler:))*