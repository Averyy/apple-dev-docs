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
- `completionHandler`: A callback the system invokes with the following data: - **`sampleBuffer`**: A sample buffer that contains the media sample to consume, or `nil` if an error occurs.
- **`sampleBufferSequenceNumber`**: The sequence number of the current sample.
- **`discontinuity`**: A flag that indicates if there’s a discontinuity in the stream.
- **`hasMoreSampleBuffers`**: A Boolean value that indicates whether there are more buffers available.
- **`error`**: An optional error. If an error occurs, it contains the details of the failure.

## See Also

- [func send(CMSampleBuffer, discontinuity: CMIOExtensionStream.DiscontinuityFlags, hostTimeInNanoseconds: UInt64)](cmioextensionstream/send(_:discontinuity:hosttimeinnanoseconds:).md)
  Sends a media sample to stream client.
- [CMIOExtensionStream.DiscontinuityFlags](cmioextensionstream/discontinuityflags.md)
  Constants that specify the types of discontinuities that can occur in a media stream.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremediaio/cmioextensionstream/consumesamplebuffer(from:completionhandler:))*